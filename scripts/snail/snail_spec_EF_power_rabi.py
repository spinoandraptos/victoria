import sys


from qm import qua as qm_qua
import numpy as np
from config.experiment_config import FOLDER, N, FREQ, I, Q, MAG, PHASE, MODES_CONFIG, RR
from qcore import Experiment, qua, Sweep
from qcore.helpers import Stage

import time

class Snail_Power_Rabi(Experiment):
    """Cavity spectroscopy"""

    ############################# DEFINE PRIMARY DATASETS ##############################
    # these Datasets form the "raw" experimental data and will be streamed by the OPX
    # they must be specified at experiment runtime

    primary_datasets = ["I", "Q"]

    ############################## DEFINE PRIMARY SWEEPS ###############################
    # these Sweeps are uniquely associated with the Experiment subclass
    # these Sweeps must be specified at experiment runtime

    primary_sweeps = ["snailEF_ampx"]

    ############################ DEFINE THE PULSE SEQUENCE #############################
    # ensure that you import 'qua' from 'qcore' and not from 'qm' library
    # attributes accessed via 'self' must be defined in 'if __name__ == "__main__"' code

    def sequence(self):
        """QUA sequence that defines this Experiment subclass"""
        
        self.snail.play(self.snail_pulse, ampx = self.snail_ampx)
        qua.align(self.snail, self.snailEF)
        self.snailEF.play(self.snail_EF_pulse, ampx = self.snailEF_ampx)
        
        qua.align(self.cavity, self.snailEF)
        self.cavity.play(self.cavity_pulse, ampx = self.cav_ampx)
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
        "cavity": "cavity",
        "qubit": "qubit",
        "resonator": "rr",
        "snail": "snail_drive",
        "snailEF": "snail_drive_EF",
    }

    ################################### PULSE MAP ######################################
    # key: name of the Pulse as defined by the Experiment subclass
    # value: name of the Pulse as defined by the user in modes.yml

    pulses = {
        "cavity_pulse":"cav_constant_48_ecd",
        "qubit_pulse": "qubit_gaussian_pi_2000",
        "snail_pulse": "snail_drive_constant_pi",
        "snail_EF_pulse": "snail_drive_EF_constant_pi",
        "readout_pulse": "rr_readout_pulse",
    }

    ############################## CONTROL PARAMETERS ############# #####################

    parameters = {
        "wait_time": 100_000,
        "ro_ampx": 1,
        "snail_ampx": 1, 
        "cav_ampx": 1,
        "fetch_interval": 1,
        "plot_single_shot": False,
        
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this Experiment run
    N.num = 20000

    # set the qubit frequency sweep for this Experiment run
    
    # FREQ.name = "snail_frequency"
    # FREQ.start =-250e6
    # FREQ.stop =-150e6 
    # FREQ.num = 101
    AMPX = Sweep(name="snailEF_ampx", start=-2.5, stop=2.5, step=0.1, dtype=float)
    # QB_AMPX = Sweep(
    #     name="qb_ampx",
    #     points=[0.0, 1.0],
    # )
    PHASE.plot = True
    MAG.plot = True
    Q.plot = True
    I.plot = True
    # SINGLE_SHOT.plot = False
    
    
    
    sweeps = [N, AMPX]
    #SINGLE_SHOT.plot_args["plot_type"] = "image"

    ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass
    
    I.fitfn, Q.fitfn, MAG.fitfn = (
        "sine",
        "sine",
        "sine",
        # "sine_gf",
        # "sine_gf",
        # "sine_gf",
    )

    PHASE.datafn_args = {"delay": 2.792e-7, "freq": RR.int_freq}
    
   
    datasets = [I, Q, MAG, PHASE]
    ######################## INITIALIZE AND RUN EXPERIMENT #############################
    

    expt = Snail_Power_Rabi(FOLDER, modes, pulses, sweeps, datasets, **parameters)
    
    # expt.run(simulate=True)
    expt.run()