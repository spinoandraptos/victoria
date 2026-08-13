""" """
""" """
import sys
from config.experiment_config import FOLDER, N, FREQ, I, Q, MAG, PHASE, SINGLE_SHOT, RR

from qcore import Experiment, qua, Sweep
from qm import qua as qm_qua
from qcore.helpers import Stage
from config.experiment_config import MODES_CONFIG
import numpy as np
import time


class NumberSplitting_FOCK1(Experiment):
    """Number splitting"""

    ############################# DEFINE PRIMARY DATASETS ##############################
    # these Datasets form the "raw" experimental data and will be streamed by the OPX
    # they must be specified at experiment runtime

    primary_datasets = ["I", "Q"]

    ############################## DEFINE PRIMARY SWEEPS ###############################
    # these Sweeps are uniquely associated with the Experiment subclass
    # these Sweeps must be specified at experiment runtime

    primary_sweeps = ["fock_drive_frequency"]

    ############################ DEFINE THE PULSE SEQUENCE #############################
    # ensure that you import 'qua' from 'qcore' and not from 'qm' library
    # attributes accessed via 'self' must be defined in 'if __name__ == "__main__"' code

    def sequence(self):
        """QUA sequence that defines this Experiment subclass"""

        # GF transition
        self.qubit_gf2.play(self.qubit_gf2_pi_pulse, ampx= self.drive_ampx)
        qua.align(self.qubit_gf2, self.drive)
        
        # Sideband drive to exchange excitation
        qua.update_frequency(self.drive, self.fock_drive_frequency)
        self.drive.play(self.fock_drive, ampx= self.drive_ampx) # fixed freq #, ampx=2.0 max
        qua.align(self.drive, self.qubit)
        
        # Bring qubit back to ground
        self.qubit.play(self.qubit_pulse)
        qua.align(self.qubit, self.resonator)

        # Measurement
        self.resonator.measure(self.readout_pulse, (self.I, self.Q), ampx=self.ro_ampx, demod_type="dual")
        qua.wait(self.wait_time, self.resonator)


if __name__ == "__main__":
    """ """

    #################################### MODE MAP ######################################
    # key: name of the Mode as defined by the Experiment subclass
    # value: name of the Mode as defined by the user in modes.yml

    modes = {
        # "cavity": "cavity",#"cav",
        "qubit": "qubit",
        "resonator": "rr",
        "qubit_gf2": "qubit_GF2",
        "drive": "fock_drive",
        
    }

    ################################### PULSE MAP ######################################
    # key: name of the Pulse as defined by the Experiment subclass
    # value: name of the Pulse as defined by the user in modes.yml

    pulses = {
        "qubit_pulse": "qubit_gaussian_pi_2000",
        "qubit_gf2_pi_pulse": "qubitGF2_constant_pi_200",
        "readout_pulse": "rr_readout_pulse",
        "fock_drive": "fock_drive_constant_172",
    }

    ############################## CONTROL PARAMETERS ##################################

    parameters = {
        "wait_time": 100_000,#6e6,
        "ro_ampx": 1,
        # "plot_single_shot": True,
        "drive_ampx": 1
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this Experiment run
    N.num = 500000

    # set the qubit frequency sweep for this Experiment run
    FREQ.name = "fock_drive_frequency"
    FREQ.start = -100e6
    FREQ.stop = 100e6
    FREQ.num = 301

    # QD_AMPX = Sweep(name="qubit_drive_ampx", points=[0.0, 1.0])

    # sweeps = [N, FREQ]
    # QD_AMPX = Sweep(name="drive_ampx", points= [0.0, 1.0]) #needs to be floating point numbers 
    sweeps = [N, FREQ]

    ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass

    PHASE.datafn_args = {"delay": 2.792e-7, "freq": RR.int_freq}
    PHASE.plot = True
    I.plot = True
    Q.plot = True
    MAG.plot = True

    I.fitfn = "gaussian"
    Q.fitfn = "gaussian"
    MAG.fitfn = "gaussian"
    datasets = [I, Q, MAG, PHASE]
    # SINGLE_SHOT.fitfn = 'double_gaussian'
    #SINGLE_SHOT.plot_args = {"plot_err": False}

    ######################## INITIALIZE AND RUN EXPERIMENT #############################

    expt = NumberSplitting_FOCK1(FOLDER, modes, pulses, sweeps, datasets, **parameters)
    expt.run()