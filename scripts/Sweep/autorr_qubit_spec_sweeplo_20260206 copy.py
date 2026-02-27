""" """
import sys
# The directory containing the 'config' folder
FOLDER = "C:/Users/qcrew/Documents/eunice/"

# Add the FOLDER itself to sys.path, not the file path
if FOLDER not in sys.path:
    sys.path.insert(0, FOLDER)

from config.experiment_config import FOLDER, N, FREQ, I, Q, MAG, PHASE, RR
from qcore.helpers import Stage
from qcore.pulses import *
from qcore import Experiment, qua, Sweep
from config.experiment_config import MODES_CONFIG
import time
import os

os.environ["HDF5_USE_FILE_LOCKING"] = "FALSE"
import h5py
from datetime import datetime
import subprocess
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Create a StartupInfo object
info = subprocess.STARTUPINFO()

# Set flags to use the wShowWindow attribute
info.dwFlags |= subprocess.STARTF_USESHOWWINDOW

# Set the window state to hidden
info.wShowWindow = subprocess.SW_HIDE


# -----------------------------------
# Do not modify: script defaults
# -----------------------------------
def lorentzian(f, f0, gamma, a, b):
    return a - b / (1 + ((f - f0) / gamma) ** 2)


def gaussian(f, f0, sig, ofs, amp):
    return ofs + amp * np.exp(-((f - f0) ** 2) / (2 * sig**2))


# -----------------------------------

# -----------------------------------
tol = 1e6  # Hz tolerance for convergence
N_stable = 3  # how many stable readings in a row
# -----------------------------------


def estimate_RR_peak(fname):
    with h5py.File(fname, "r", locking=False) as f:
        mag = f["Magnitude"][:]
        freq = f["resonator_frequency"][:]

    avg_mag = mag.mean(axis=0)  # shape (201,)

    # Estimate the resonator peak from Lorentzian fit
    p0 = [freq[np.argmin(avg_mag)], 1e6, np.max(avg_mag), np.ptp(avg_mag)]
    params, _ = curve_fit(lorentzian, freq, avg_mag, p0=p0)
    f0, gamma, a, b = params
    print(f"Fitted RR at {f0/1e6:.6g} MHz")
    return f0


def find_RR(lo_rr, yoko_target):

    date, _ = datetime.now().strftime("%Y-%m-%d %H-%M-%S").split()
    ROOT = Path(__file__).resolve().parents[2]
    DATA_DIR = ROOT / "data" / date
    file_path = Path(f"{DATA_DIR}/RR_LO_sweep.txt")
    # 2. Automatically create the folder if it doesn't exist
    file_path.parent.mkdir(parents=True, exist_ok=True)

    history = []
    stable_count = 0
    converged = False

    # Next, perform RRspec and identify the correct LO for RR
    # Run RRspec experiment
    RRspec_proc = subprocess.Popen(
        [
            "C:/Users/qcrew/Documents/eunice/.venv/Scripts/python.exe",
            "scripts/readout/rr_spec_auto.py",
        ],
        startupinfo=info,
        creationflags=subprocess.CREATE_NO_WINDOW,  # Also prevents console pop-ups
    )

    time.sleep(4)

    # Find all RRspec files
    files = [f for f in DATA_DIR.glob("*RRspec*.hdf5")]

    if not files:
        raise RuntimeError(f"No RRspec files found in data folder {DATA_DIR}")

    # Pick the latest by modification time
    fname = max(files, key=lambda f: f.stat().st_mtime)

    # IF the RR peak lies within current range, find stable peak
    try:
        while True:
            time.sleep(2)  # wait for new data, update every 4s
            f_min = estimate_RR_peak(fname)
            history.append(f_min)

            if len(history) > 1:
                if abs(history[-1] - history[-2]) < tol:
                    stable_count += 1
                else:
                    stable_count = 0
            # Either the peak converges or too many measurements (no clear peak)
            if stable_count >= N_stable:
                converged = True
                RR_LO_adjustment = (history[-1] + history[-2] + history[-3]) / 3 + 50e6
                lo_rr += RR_LO_adjustment
                print(f"RR converged at {lo_rr/1e9:.6g} GHz, stopping measurement")

                # 3. Write/Append the data
                with open(file_path, "a") as f:
                    f.write(
                        f"RR_LO:{lo_rr}, Yoko:{yoko_target}\n"
                    )

                RRspec_proc.terminate()

                break
            if len(history) >= 30:
                converged = False
                print("No peak detected, stopping measurement")
                RRspec_proc.terminate()
                break

            # TODO: Handle edge case 1, If no peak found, update LO to new sweep range and repeat RRspec
            # TODO: Handle edge case 2, If multiple peaks, how?

    finally:
        if RRspec_proc.poll() is None:
            RRspec_proc.kill()
        return lo_rr


class QubitSpec(Experiment):
    """Qubit spectroscopy"""

    ############################# DEFINE PRIMARY DATASETS ##############################
    # these Datasets form the "raw" experimental data and will be streamed by the OPX
    # they must be specified at experiment runtime

    primary_datasets = ["I", "Q"]

    ############################## DEFINE PRIMARY SWEEPS ###############################
    # these Sweeps are uniquely associated with the Experiment subclass
    # these Sweeps must be specified at experiment runtime

    primary_sweeps = ["qubit_frequency"]

    ############################ DEFINE THE PULSE SEQUENCE #############################
    # ensure that you import 'qua' from 'qcore' and not from 'qm' library
    # attributes accessed via 'self' must be defined in 'if __name__ == "__main__"' code

    def sequence(self):
        """QUA sequence that defines this Experiment subclass"""
        qua.reset_phase(self.resonator)
        qua.update_frequency(self.qubit, self.qubit_frequency)
        #qua.update_frequency(self.resonator, self.resonator_frequency)
        self.qubit.play(self.qubit_drive)#, ampx=self.qubit_drive_ampx)
        qua.align()
        self.resonator.measure(
            self.readout_pulse, (self.I, self.Q), ampx=self.ro_ampx, demod_type="dual"
        )
        qua.wait(self.wait_time, self.resonator)


if __name__ == "__main__":
    """ """

    #################################### MODE MAP ######################################
    # key: name of the Mode as defined by the Experiment subclass
    # value: name of the Mode as defined by the user in modes.yml

    modes = {
        "qubit": "qubit",
        "resonator": "rr",
    }

    ################################### PULSE MAP ######################################
    # key: name of the Pulse as defined by the Experiment subclass
    # value: name of the Pulse as defined by the user in modes.yml

    pulses = {
        "qubit_drive": "qubit_constant_pi_1500",#"qubit_constant_pulse",#"qubit_constant_pi_1500",
        "readout_pulse": "rr_readout_pulse",
    }

    ############################## CONTROL PARAMETERS ##################################

    parameters = {
        "wait_time": 6000,
        "ro_ampx": 1.0,
        "qubit_drive_ampx": 1,
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this E xperiment run
    N.num = 50000

    # set the qubit frequency sweep for this Experiment run
    FREQ.name = "qubit_frequency"
    FREQ.start = -200e6  # 40e6
    FREQ.stop = 200e6  # 60e6 #the 60e6 is from the lo used to generate ef pulse
    FREQ.num = 301
    

    sweeps = [N, FREQ]

    ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass

    PHASE.datafn_args = {"delay": 2.792e-7, "freq": RR.int_freq}
    PHASE.plot = False
    I.plot = False
    Q.plot = False
    MAG.plot = False
    # PHASE.plot = True
    # I.plot = True
    # Q.plot = True
    # MAG.plot = True

    datasets = [I, Q, MAG, PHASE]

    ######################## INITIALIZE AND RUN EXPERIMENT #############################
    import numpy as np

    flux_list = [0e-3, 20e-3, 40e-3, 60e-3, 80e-3, 90e-3, 100e-3, 110e-3, 120e-3]

    # Corresponding RR frequencies in Hz
    rr_LO_list = [
     3.918421e9, # 0mA
       3.918421e9, # 20mA
        3.918251e9, # 40mA
       3.918011e9, # 60mA
        3.917591e9, # 80mA
        3.917271e9, # 90mA
        3.917031e9, # 100mA
        3.9166310e9, # 110mA
        3.916231e9  # 120mA
     ]
        
     #0mA 3.918421000e9
        #20mA 3.918421000e9
        #40mA 3.918251000e9
        #60mA 3.918011000e9
        #80mA 3.917591000e9
        #90mA 3.917271000e9
        #100mA 3.917031000e9
        #110mA 3.916631000E9
        #120mA 3.916231000

    lo_qubit_values = np.arange(5e9, 6.4e9 + 400e6, 400e6)
    rr_LO = 3.918421000e9
    
    qubit_amps = [0.1, 0.3, 0.6, 0.8, 1.2]
    
    with Stage(configpath=MODES_CONFIG, remote=True) as stage:
        opx1000, yoko, qubit = stage.get("opx1000", "yoko2", "qubit")
        
        for qubit_amp in qubit_amps: 

            qubit.operations = [
                ConstantPulse(
                    name="qubit_constant_pi_1500",
                    length=1500,
                    I_ampx=qubit_amp,
                ),
            ]
            
            for index_f in range(len(flux_list[:])):
                yoko_target = flux_list[index_f]
                
                #lo_rr = find_RR(rr_LO, yoko_target)
                lo_rr = rr_LO_list[index_f]#find_RR(rr_LO, yoko_target)
                
                for index_q in range(len(lo_qubit_values)):
                    print(f"YOKO state before: {yoko.output}")
                    yoko.output = True
                    print(f"YOKO state: {yoko.output}")
                    yoko.ramp(yoko_target, step=0.1e-3)
                    qubit_LO = lo_qubit_values[index_q]
                    settings = {
                                    "controllers": {
                                        "con1": {
                                            "fems": {
                                                2: {
                                                    "analog_outputs": {
                                                        1: {
                                                            "full_scale_power_dbm": -11, #only in increments of 3s
                                                            "upconverters": {1: {"frequency":  lo_rr}},
                                                            "band":1
                                                        },
                                
                                                        7: {
                                                            "full_scale_power_dbm": 16, #7
                                                            "upconverters": {1: {"frequency": qubit_LO}},
                                                            "band":1
                                                        },
                                                    },
                                                    "analog_inputs": {
                                                        1: {
                                                            "downconverter_frequency": lo_rr,
                                                            "band":1 #3
                                                            },  # for down-conversion
                                    
                                                    },
                                                },
                                                
                                            } 
                                        }
                                    }
                                }      
                    opx1000.settings = settings

                    expt = QubitSpec(FOLDER, modes, pulses, sweeps, datasets, **parameters)
                    expt.run()
                    # expt.run(simulate=True)
                    time.sleep(1)  # Sleeps for 1 second; adjust as needed
            yoko.ramp(0e-3, step=1e-4)
