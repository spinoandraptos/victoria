import sys


from qm import qua as qm_qua
import numpy as np
from config.experiment_config import FOLDER, N, FREQ, I, Q, MAG, PHASE, MODES_CONFIG, RR
from qcore.libs.qua_macros import QuaVariable
from qcore import Experiment, qua, Sweep
from qcore.helpers import Stage

import time

class Snail_T2(Experiment):
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
        
        factor = qm_qua.declare(qm_qua.fixed)
        qm_qua.assign(factor, self.detuning * 1e-9)

        """QUA sequence that defines this Experiment subclass"""
        qua.reset_frame(self.snail)
        qua.reset_phase(self.snail)
        
        self.snail.play(self.snail_pulse) # pi/2
        qua.wait(self.time_delay, self.snail)  # Half wait
        # qua.wait(self.time_delay / 2, self.snail)  # Half wait
        # self.snail.play(self.snail_echo_pulse)
        # qua.wait(self.time_delay / 2, self.snail)  # Half wait
        qm_qua.assign(self.phase, qm_qua.Cast.mul_fixed_by_int(factor, self.time_delay))
        self.snail.play(self.snail_pulse, phase=self.phase) # pi/2
            
        qua.align(self.cavity, self.snail)
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
    }

    ################################### PULSE MAP ######################################
    # key: name of the Pulse as defined by the Experiment subclass
    # value: name of the Pulse as defined by the user in modes.yml

    pulses = {
        "cavity_pulse":"cav_constant_48_ecd",
        "qubit_pulse": "qubit_gaussian_pi_2000",
        "snail_pulse": "snail_drive_constant_pi2",
        "snail_echo_pulse": "snail_drive_constant_pi",
        "readout_pulse": "rr_readout_pulse",
    }

    ############################## CONTROL PARAMETERS ############# #####################

    parameters = {
        "wait_time": 180_000,
        "detuning":6e6,
        "phase": QuaVariable(
            value=0.0,
            dtype=qm_qua.fixed,
            tag="phase",
            buffer=True,
            stream=True,
        ),
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
    N.num = 10000    
    DELAY = Sweep(name="time_delay", start=16, stop=5000, step=50, dtype=int)

    PHASE.plot = True
    MAG.plot = True
    Q.plot = True
    I.plot = True
    # SINGLE_SHOT.plot = False
    
    sweeps = [N, DELAY]
    #SINGLE_SHOT.plot_args["plot_type"] = "image"

    ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass
    
    I.fitfn = "exp_decay_sine"
    Q.fitfn = "exp_decay_sine"
    MAG.fitfn = "exp_decay_sine"
    PHASE.fitfn = "exp_decay_sine"

    PHASE.datafn_args = {"delay": 2.792e-7, "freq": RR.int_freq}
    
   
    datasets = [I, Q, MAG, PHASE]
    ######################## INITIALIZE AND RUN EXPERIMENT #############################
    

    expt = Snail_T2(FOLDER, modes, pulses, sweeps, datasets, **parameters)
    
    # expt.run(simulate=True)
    expt.run()