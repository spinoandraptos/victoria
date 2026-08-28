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


class cavity_stark_shift_snail_drive(Experiment):
    """Cavity spectroscopy"""

    ############################# DEFINE PRIMARY DATASETS ##############################
    # these Datasets form the "raw" experimental data and will be streamed by the OPX
    # they must be specified at experiment runtime

    primary_datasets = ["I", "Q"]

    ############################## DEFINE PRIMARY SWEEPS ###############################
    # these Sweeps are uniquely associated with the Experiment subclass
    # these Sweeps must be specified at experiment runtime

    primary_sweeps = ["cavity_frequency"]

    ############################ DEFINE THE PULSE SEQUENCE #############################
    # ensure that you import 'qua' from 'qcore' and not from 'qm' library
    # attributes accessed via 'self' must be defined in 'if __name__ == "__main__"' code

    def sequence(self):
        """QUA sequence that defines this Experiment subclass"""
       
        # There are two cavity modes here, please check which mode is used.
        qua.update_frequency(self.cavity, self.cavity_frequency)
        self.drive.play(self.stark_drive, ampx=self.drive_ampx) # fixed freq
        self.cavity.play(self.cavity_drive)
        qua.align(self.cavity, self.qubit)
        self.qubit.play(self.qubit_pulse)
        qua.align(self.qubit, self.resonator)
        qua.align()
        self.resonator.measure(
            self.readout_pulse, (self.I, self.Q), ampx=self.ro_ampx, demod_type="dual"
        )
        if self.plot_single_shot:  # assign state to G or E
            qm_qua.assign(
                self.single_shot,
                qm_qua.Cast.to_fixed(self.I > self.readout_pulse.threshold),
            )

        qua.wait(self.wait_time, self.resonator)


if __name__ == "__main__":
    """ """

    #################################### MODE MAP ######################################
    # key: name of the Mode as defined by the Experiment subclass
    # value: name of the Mode as defined by the user in modes.yml

    modes = {
        "drive": "snail_drive",
        "cavity": "cavity",
        "qubit": "qubit",
        "resonator": "rr",
    }

    ################################### PULSE MAP ######################################
    # key: name of the Pulse as defined by the Experiment subclass
    # value: name of the Pulse as defined by the user in modes.yml

    pulses = {
        "cavity_drive": "cav_constant_1000",
        "qubit_pulse": "qubit_gaussian_pi_pulse_1200",
        "stark_drive": "snail_drive_constant_starkShift",
        "readout_pulse": "rr_readout_pulse",
    }

    ############################## CONTROL PARAMETERS ############# #####################

    parameters = {
        "wait_time": 300_000,
        "ro_ampx": 1,
        "snail_ampx": 1,
        "fetch_interval": 1,
        "plot_single_shot": False,
        
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this Experiment run
    N.num = 3000

    # set the qubit frequency sweep for this Experiment run
    Q_AMPX = Sweep(
        name="drive_ampx",
        # points=[0.01, 0.05, 0.08, 0.1, 0.2, 0.3, 0.4, 0.5]#0.25,0.5,0.75]
        # points=[1.0,2.0 ]
        points=[0., 0.1, 0.2, 0.4, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.75, 2.0]
        # points=[1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.75, 2.0]
    ) 
    
    FREQ.name = "cavity_frequency"
    FREQ.start =-60e6
    FREQ.stop =-40e6
    FREQ.num = 101
    
    sweeps = [N, FREQ, Q_AMPX]
    # sweeps = [N, FREQ]
    
    PHASE.plot = False
    MAG.plot = False
    Q.plot = False
    I.plot = True
    SINGLE_SHOT.plot = False
    I.plot_args["plot_type"] = "image"

    PHASE.datafn_args = {"delay": 2.792e-7, "freq": RR.int_freq}
    
   
    datasets = [I, Q, MAG, PHASE]
    ######################## INITIALIZE AND RUN EXPERIMENT #############################

    expt = cavity_stark_shift_snail_drive(FOLDER, modes, pulses, sweeps, datasets, **parameters)
    expt.run(simulate = False)

