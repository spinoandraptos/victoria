""" """
import sys
from datetime import datetime
# The directory containing the 'config' folder
FOLDER = "C:/Users/qcrew/Documents/eunice/"

# Add the FOLDER itself to sys.path, not the file path
if FOLDER not in sys.path:
    sys.path.insert(0, FOLDER)
    
from config.experiment_config import FOLDER, N, I, Q, MAG, PHASE, RR
from qcore import Experiment, qua, Sweep


class CavitySWAP1D_len(Experiment):
    """Cavity T1"""

    ############################# DEFINE PRIMARY DATASETS ##############################
    # these Datasets form the "raw" experimental data and will be streamed by the OPX
    # they must be specified at experiment runtime

    primary_datasets = ["I", "Q"]

    ############################## DEFINE PRIMARY SWEEPS ###############################
    # these Sweeps are uniquely associated with the Experiment subclass
    # these Sweeps must be specified at experiment runtime

    primary_sweeps = ["length_snail"]

    ############################ DEFINE THE PULSE SEQUENCE #############################
    # ensure that you import 'qua' from 'qcore' and not from 'qm' library
    # attributes accessed via 'self' must be defined in 'if __name__ == "__main__"' code

    def sequence(self):
        """QUA sequence that defines this Experiment subclass"""
        qua.reset_phase(self.cavity)
        qua.reset_frame(self.cavity)
        # qua.reset_phase(self.qubit)
        qua.reset_phase(self.snail)
        qua.reset_frame(self.snail)
        qua.align()
        self.cavity.play(self.cavity_drive, ampx=1)
        qua.align(self.cavity, self.snail)
        self.snail.play(self.snail_pulse, duration=self.length_snail) # #, ampx= self.snail_ampx
        # qua.wait(self.time_delay, self.cavity)
        qua.align(self.snail, self.qubit)
        self.qubit.play(self.qubit_pulse)
        qua.align(self.qubit, self.resonator)
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
        "cavity": "cavity",
        "qubit": "qubit",
        "resonator": "rr",
        "snail": "snail_drive",
    }

    ################################### PULSE MAP ######################################
    # key: name of the Pulse as defined by the Experiment subclass
    # value: name of the Pulse as defined by the user in modes.yml

    pulses = {
        "cavity_drive": "cav_constant_48_ecd",
        "qubit_pulse": "qubit_gaussian_pi_2000",
        "readout_pulse": "rr_readout_pulse",
        "snail_pulse": "snail_drive_constant_2000",
    }

    ############################## CONTROL PARAMETERS ##################################

    parameters = {
        "wait_time":1_000_000, #30000,
        "ro_ampx": 1,
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this Experiment run
    N.num = 100000

    # set the qubit frequency sweep for this Experiment run

    # DEL = Sweep(name="time_delay", start=16, stop=1200000, step=8000, dtype=int)
    DEL = Sweep(name="length_snail", start=16, stop=100, step=4, dtype=int)
    # SNAIL_AMPX = Sweep(
    #     name="snail_ampx",
    #     points=[
    #        0.05, 0.1 # 0.05, 0.1
    #     ],
    # )
    sweeps = [N, DEL] #, SNAIL_AMPX

    ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass
    MAG.fitfn = "exp_decay_sine"
    PHASE.fitfn = "exp_decay_sine"
    I.fitfn = "exp_decay_sine"
    Q.fitfn = "exp_decay_sine"

    # MAG.axes = sweeps[1:]
    # PHASE.axes = sweeps[1:]
    PHASE.datafn_args = {"delay": 2.792e-7, "freq": RR.int_freq}
    # PHASE.plot = False
    datasets = [I, Q, MAG, PHASE]

    ######################## INITIALIZE AND RUN EXPERIMENT #############################

    expt = CavitySWAP1D_len(FOLDER, modes, pulses, sweeps, datasets, **parameters)
    expt.run()
