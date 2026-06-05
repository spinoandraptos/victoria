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


class NumberSplittingGF2_FOCK1(Experiment):
    """Number splitting"""

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
        # Generate state in the cavity
        #CREATE fock 1
        self.qubit_gf2.play(self.qubit_gf2_pi_pulse)
        qua.align(self.qubit_gf2, self.drive)
        self.drive.play(self.stark_drive, ampx= self.drive_ampx) # fixed freq #, ampx=2.0 max
     
        
        # self.cavity.play(self.cavity_pulse, ampx = self.cavity_drive_ampx)
        # number splitting
        qua.align()
        # Selective pi pulse
        qua.update_frequency(self.qubit, self.qubit_frequency)
        self.qubit.play(self.qubit_pulse)
        qua.align(self.qubit, self.resonator)
        # qua.align(self.qubit, self.qubit_gf2)
        
        #readout at gf2
        # self.qubit_gf2.play(self.qubit_gf2_pi_pulse, ampx=1.0)
        # self.qubit.play(self.qubit_drive, ampx=self.qubit_pulse_amplitude)
     
        # qua.align(self.qubit_gf2, self.resonator)

        # Measurement
        self.resonator.measure(self.readout_pulse, (self.I, self.Q), ampx=self.ro_ampx, demod_type="dual")
        qua.wait(self.wait_time, self.resonator)


if __name__ == "__main__":
    """ """

    #################################### MODE MAP ######################################
    # key: name of the Mode as defined by the Experiment subclass
    # value: name of the Mode as defined by the user in modes.yml

    modes = {
        "cavity": "cavity",#"cav",
        "qubit": "qubit",
        "resonator": "rr",
        "qubit_gf2": "qubit_GF2",
        "drive": "drive",
        
    }

    ################################### PULSE MAP ######################################
    # key: name of the Pulse as defined by the Experiment subclass
    # value: name of the Pulse as defined by the user in modes.yml

    pulses = {
        "qubit_pulse": "qubit_gaussian_pi_160",
        "qubit_gf2_pi_pulse": "qubitGF2_gaussian_pi_24",
        "readout_pulse": "rr_readout_pulse",
        "cavity_pulse": "cav_constant_240",
        "stark_drive": "drive_constant_fock1",
    }

    ############################## CONTROL PARAMETERS ##################################

    parameters = {
        "wait_time": 1_000_000,#6e6,
        "ro_ampx": 1,
        # "plot_single_shot": True,
        "qubit_drive_ampx": 1
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this Experiment run
    N.num = 500000

    # set the qubit frequency sweep for this Experiment run
    FREQ.name = "qubit_frequency"
    FREQ.start = 120e6
    FREQ.stop = 135e6
    FREQ.num = 251

    # QD_AMPX = Sweep(name="qubit_drive_ampx", points=[0.0, 1.0])

    # sweeps = [N, FREQ]
    QD_AMPX = Sweep(name="drive_ampx", points= [0.0, 1.0]) #needs to be floating point numbers 
    sweeps = [N,  QD_AMPX, FREQ]

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

    expt = NumberSplittingGF2_FOCK1(FOLDER, modes, pulses, sweeps, datasets, **parameters)
    expt.run()