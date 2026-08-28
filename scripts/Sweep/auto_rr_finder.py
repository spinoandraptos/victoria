import os

os.environ["HDF5_USE_FILE_LOCKING"] = "FALSE"
import h5py
import time
from datetime import datetime
import subprocess
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from qcore.helpers import Stage
from config.experiment_config import MODES_CONFIG

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


def estimate_qubit_peak(fname):
    with h5py.File(fname, "r", locking=False) as f:
        mag = f["Magnitude"][:]
        freq = f["qubit_frequency"][:]

    avg_mag = mag.mean(axis=0)  # shape (201,)

    ofs = (avg_mag[0] + avg_mag[-1]) / 2
    sig = abs(freq[-1] - freq[0]) / 10

    # Estimate the qubit peak from Gaussian fit
    p0 = [freq[np.argmin(avg_mag)], sig, ofs, np.ptp(avg_mag)]
    params, _ = curve_fit(gaussian, freq, avg_mag, p0=p0)
    f0, gamma, a, b = params
    print(f"Fitted Qubit at {f0/1e6:.6g} MHz")
    return f0


def find_RR(yoko_val):

    history = []
    stable_count = 0
    converged = False

    with Stage(configpath=MODES_CONFIG, remote=True) as stage:
        qubit, rr, yoko2 = stage.get("qubit", "rr", "yoko2")
        rr_LO =
        settings = {
            "controllers": {
                "con1": {
                    "fems": {
                        2: {
                            "analog_outputs": {
                                1: {
                                    "full_scale_power_dbm": -11, #only in increments of 3s
                                    "upconverters": {1: {"frequency":  rr_LO}},
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
                                    "downconverter_frequency": rr_LO,
                                    "band":1 #3
                                    },  # for down-conversion
                                # 2: {
                                #     "downconverter_frequency": rr_MR_LO,
                                #     "band":1
                                #     },  # for down-conversion
            
                            },
                        },
                        
                    } 
                }
            }
        }      

    # Next, perform RRspec and identify the correct LO for RR
    # Run RRspec experiment
    RRspec_proc = subprocess.Popen(
        [
            "C:/Users/qcrew/Documents/eunice/scripts/python.exe",
            "scripts/readout/rr_spec_auto.py",
            
        ],
        startupinfo=info,
        creationflags=subprocess.CREATE_NO_WINDOW,  # Also prevents console pop-ups
    )

    time.sleep(4)

    date, _ = datetime.now().strftime("%Y-%m-%d %H-%M-%S").split()
    ROOT = Path(__file__).resolve().parents[2]
    DATA_DIR = ROOT / "data" / date

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
                RR_freq += RR_LO_adjustment
                print(f"RR converged at {RR_freq/1e9:.6g} GHz, stopping measurement")
                RRspec_proc.terminate()

                with Stage(configpath=MODES_CONFIG, remote=True) as stage:
                    lo_qubit, lo_rr = stage.get("lo_qubit", "lo_rr")
                    lo_rr.frequency = RR_freq

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


def find_qubit(yoko_val):

    history = []
    stable_count = 0
    converged = False

    with Stage(configpath=MODES_CONFIG, remote=True) as stage:
        qubit, rr, sa, yoko2 = stage.get("qubit", "rr", "sa", "yoko2")
        lo_qubit, lo_rr = stage.get("lo_qubit", "lo_rr")
        qubit_freq = lo_qubit.frequency
        yoko2.ramp(yoko_val, step=1e-4)

    # Next, perform RRspec and identify the correct LO for RR
    # Run RRspec experiment
    RRspec_proc = subprocess.Popen(
        [
            "C:/Users/qcrew/Documents/eunice/sripts/python.exe",
            "scripts/qubit/qubit_spec_auto.py",
        ],
        startupinfo=info,
        creationflags=subprocess.CREATE_NO_WINDOW,  # Also prevents console pop-ups
    )

    time.sleep(3)

    date, _ = datetime.now().strftime("%Y-%m-%d %H-%M-%S").split()
    ROOT = Path(__file__).resolve().parents[2]
    DATA_DIR = ROOT / "data" / date

    # Find all RRspec files
    files = [f for f in DATA_DIR.glob("*QubitSpec*.hdf5")]

    if not files:
        raise RuntimeError(f"No RRspec files found in data folder {DATA_DIR}")

    # Pick the latest by modification time
    fname = max(files, key=lambda f: f.stat().st_mtime)

    # IF the RR peak lies within current range, find stable peak
    try:
        while True:
            time.sleep(2)  # wait for new data, update every 4s
            f_min = estimate_qubit_peak(fname)
            history.append(f_min)

            if len(history) > 1:
                if abs(history[-1] - history[-2]) < tol:
                    stable_count += 1
                else:
                    stable_count = 0
            # Either the peak converges or too many measurements (no clear peak)
            if stable_count >= N_stable:
                converged = True
                qubit_LO_adjustment = (
                    history[-1] + history[-2] + history[-3]
                ) / 3 + 50e6
                qubit_freq += qubit_LO_adjustment
                print(
                    f"Qubit converged at {qubit_freq/1e9:.6g} GHz, stopping measurement"
                )
                RRspec_proc.terminate()

                with Stage(configpath=MODES_CONFIG, remote=True) as stage:
                    lo_qubit, lo_rr = stage.get("lo_qubit", "lo_rr")
                    lo_qubit.frequency = qubit_freq

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


# Run 2 times to ensure -50MHz RR
for i in range(2):
    find_RR(yoko_val=120e-3)

# for i in range(2):
#     find_qubit(yoko_val=20e-3)
