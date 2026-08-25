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


class DisplacementThreeTone(Experiment):
    """Cavity spectroscopy"""

    ############################# DEFINE PRIMARY DATASETS ##############################
    # these Datasets form the "raw" experimental data and will be streamed by the OPX
    # they must be specified at experiment runtime

    primary_datasets = ["I", "Q"]

    ############################## DEFINE PRIMARY SWEEPS ###############################
    # these Sweeps are uniquely associated with the Experiment subclass
    # these Sweeps must be specified at experiment runtime

    primary_sweeps = ["cav_ampx"]

    ############################ DEFINE THE PULSE SEQUENCE #############################
    # ensure that you import 'qua' from 'qcore' and not from 'qm' library
    # attributes accessed via 'self' must be defined in 'if __name__ == "__main__"' code

    def sequence(self):
        """QUA sequence that defines this Experiment subclass"""
        #qua.reset_phase(self.cavity)
        #qua.reset_frame(self.cavity)
       
        
        # There are two cavity modes here, please check which mode is used.
        self.Malaysia_cavity.play(self.Malaysia_cavity_pulse, ampx=self.cav_ampx)
        
        qua.align(self.Malaysia_cavity, self.qubit)
        self.cavity.play(self.cavity_pulse)
        qua.align(self.cavity, self.qubit)
        # qua.wait(32, self.qubit)
        self.qubit.play(self.qubit_pulse)
        qua.align(self.qubit, self.resonator)
        # qua.align()
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
        "Malaysia_cavity": "fock_drive",
        "cavity": "cavity",
        "qubit": "qubit",
        "resonator": "rr",
    }

    ################################### PULSE MAP ######################################
    # key: name of the Pulse as defined by the Experiment subclass
    # value: name of the Pulse as defined by the user in modes.yml

    pulses = {
        "Malaysia_cavity_pulse": "three_tone_cav_constant_2000",
        "cavity_pulse": "cav_gaussian_pulse_1600",
        "qubit_pulse": "qubit_gaussian_pi_pulse_1200",
        "readout_pulse": "rr_readout_pulse",
    }

    ############################## CONTROL PARAMETERS ############# #####################

    parameters = {
        "wait_time": 500_000,
        "ro_ampx": 1,
        # "cav_ampx": 0.05,
        "fetch_interval": 1,
        "plot_single_shot": False,
        
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this Experiment run
    N.num = 1500000

    # set the qubit frequency sweep for this Experiment run
    
    # FREQ.start =-200e6
    # FREQ.stop =100e6 
    # FREQ.num = 1201
    #PULSE_LENGTH = Sweep(name="cav_pulse_length", start=16, stop=400, step=16, dtype=int)
    # Q_AMPX = Sweep(name="cav_ampx", start=0, stop=1, num=5)
    PHASE.plot = True
    MAG.plot = True
    Q.plot = True
    I.plot = True
    SINGLE_SHOT.plot = False
    
    CAV_AMP = Sweep(name="cav_ampx", start=0.1, stop=2, step=0.05)
        
    sweeps = [N, CAV_AMP]
    # sweeps = [N, Q_AMPX, FREQ]
    #SINGLE_SHOT.plot_args["plot_type"] = "image"

    ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass
    I.fitfn = "displacement_cal"
    Q.fitfn = "displacement_cal"
    MAG.fitfn = "displacement_cal"
    PHASE.fitfn = "displacement_cal"

    PHASE.datafn_args = {"delay": 2.792e-7, "freq": RR.int_freq}
    
   
    datasets = [I, Q, MAG, PHASE]
    ######################## INITIALIZE AND RUN EXPERIMENT #############################

    expt = DisplacementThreeTone(FOLDER, modes, pulses, sweeps, datasets, **parameters)
    expt.run()
            # time.sleep(60)
