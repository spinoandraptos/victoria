""" """
""" """
import sys
# The directory containing the 'config' folder
FOLDER = "C:/Users/qcrew/Documents/eunice/"

# Add the FOLDER itself to sys.path, not the file path
if FOLDER not in sys.path:
    sys.path.insert(0, FOLDER)

from config.experiment_config import FOLDER, N, FREQ, I, Q, MAG, PHASE, RR, SINGLE_SHOT
from qm import qua as qm_qua
from qcore import Experiment, qua, Sweep
import numpy as np


class OutAndBackChi(Experiment):
    """Dispersive shift between cavity and qubit"""

    ############################# DEFINE PRIMARY DATASETS ##############################
    # these Datasets form the "raw" experimental data and will be streamed by the OPX
    # they must be specified at experiment runtime

    primary_datasets = ["I", "Q"]

    ############################## DEFINE PRIMARY SWEEPS ###############################
    # these Sweeps are uniquely associated with the Experiment subclass
    # these Sweeps must be specified at experiment runtime

    primary_sweeps = ["time_delay"]

    ############################ DEFINE THE PULSE SEQUENCE #############################
    # ensure that you import 'qua' from 'qcore' and not from 'qm' library
    # attributes accessed via 'self' must be defined in 'if __name__ == "__main__"' code

    def sequence(self):
        """QUA sequence that defines this Experiment subclass"""
        qua.reset_phase(self.cavity)
        qua.reset_frame(self.cavity)
        qua.reset_phase(self.qubit)
        qua.reset_frame(self.qubit)

        if self.qubit_in_e:
            self.qubit.play(self.qubit_pi_pulse)
        qua.align()
        self.cavity.play(self.cav_displacement)  # create a coherent state #, ampx=1
        qua.align()  # put qubit into excited state to start rotation of cohstate
        # qua.update_frequency(self.cavity, -50e6 -15.29e3,keep_phase=True)
        qua.wait(self.time_delay, self.cavity)  # wait for state to rotate
        # qua.update_frequency(self.cavity, -50e6 - 9.362e3, keep_phase=True)
        qua.align()
        self.cavity.play(self.cav_displacement, ampx=1, phase=self.disp_phase)
        # )  # displace cavity back
        qua.align()  # qubit and cavity
        self.qubit.play(self.qubit_selective_pi)  # flip qubit if cav is in vac.

        # measurement
        qua.align()
        self.resonator.measure(self.readout_pulse, (self.I, self.Q), demod_type="dual")

        qua.wait(self.wait_time, self.resonator)


if __name__ == "__main__":
    """ """

    #################################### MODE MAP ######################################
    # key: name of the Mode as defined by the Experiment subclass
    # value: name of the Mode as defined by the user in modes.yml

    modes = {
        "qubit": "qubit",
        "cavity": "cavity",
        # "cavity_e": "alice_e",
        "resonator": "rr",
    }

    ################################### PULSE MAP ######################################
    # key: name of the Pulse as defined by the Experiment subclass
    # value: name of the Pulse as defined by the user in modes.yml

    pulses = {
        "cav_displacement":"cav_constant_300", #"cav_gaussian_pulse_100",
        "qubit_pi_pulse": "qubit_gaussian_pi_24",
        "qubit_selective_pi": "qubit_gaussian_pi_1200",
        "readout_pulse": "rr_readout_pulse",
    }

    ############################## CONTROL PARAMETERS ##################################

    parameters = {
        "wait_time": 800_000,
        # "plot_single_shot": True,
        "qubit_in_e": True,
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES ############ #################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this Experiment run
    N.num = 10000

    # set the delay sweep
    DEL = Sweep(name="time_delay", start=16, stop= 4000, num=21, dtype=int)

    DISPL_PHASE = Sweep(name="disp_phase", start=0.1, stop=1, num=31, dtype=float)
    sweeps = [N, DISPL_PHASE, DEL]

    ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass

    # MAG.axes = sweeps[1:]
    # PHASE.axes = sweeps[1:]
    PHASE.datafn_args = {"delay": 2.792e-7, "freq": RR.int_freq}  # 2.792e-7
    PHASE.plot = False
    #MAG.plot = True
    Q.plot = False
    I.plot = False
    #I.plot = True
    MAG.plot_args["plot_type"] = "image"
    #I.plot_args["plot_type"] = "image"
    # SINGLE_SHOT.plot_args["plot_type"] = "image"
    # SINGLE_SHOT.plot = True
    datasets = [I, Q, PHASE, MAG]

    ######################## INITIALIZE AND RUN EXPERIMENT #############################

    expt = OutAndBackChi(FOLDER, modes, pulses, sweeps, datasets, **parameters)
    expt.run()
