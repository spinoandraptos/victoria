""" """
import sys

from config.experiment_config import FOLDER, N, FREQ, I, Q, MAG, PHASE, SINGLE_SHOT, RR

from qcore import Experiment, qua, Sweep
from qm import qua as qm_qua
from qcore.libs.qua_macros import QuaVariable
from qcore.helpers import Stage
from config.experiment_config import MODES_CONFIG
import numpy as np
import time


class CavityT2(Experiment):
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
        
        factor = qm_qua.declare(qm_qua.fixed)
        qm_qua.assign(factor, self.detuning * 1e-9)
        qm_qua.assign(self.phase, qm_qua.Cast.mul_fixed_by_int(factor, self.time_delay))
        qua.align()
		
		#### create the superposition state 0+1 in the cavity
        self.cavity.play(self.cavity_fock01)
        self.qubit.play(self.qubit_fock01)
        qua.align()
		
		#### wait for variable time t ####
        qua.wait(self.time_delay, self.cavity)
        qua.align()
		
		#### displace cavity with rotating angle ####
        self.cavity.play(self.cavity_drive, ampx=0.8, phase = self.phase)
        qua.align(self.cavity, self.qubit) 
		
		#### measure whether cavity is in 0 via selective pi pulse ####
        self.qubit.play(self.sel_qubit_pulse) 
        qua.align(self.qubit, self.resonator)
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
    }

    ################################### PULSE MAP ######################################
    # key: name of the Pulse as defined by the Experiment subclass
    # value: name of the Pulse as defined by the user in modes.yml

    pulses = {
        "cavity_fock01":"",
        "qubit_fock01":"",
        "cavity_drive": "cav_constant_20",
        "sel_qubit_pulse": "qubit_gaussian_pi_8000",
        "readout_pulse": "rr_readout_pulse",
    }

    ############################## CONTROL PARAMETERS ############# #####################

    parameters = {
        "wait_time": 1500_000,
        "ro_ampx": 1,
        "detuning":4e6,
        "phase": QuaVariable(
            value=0.0,
            dtype=qm_qua.fixed,
            tag="phase",
            buffer=True,
            stream=True,
        ),
        "fetch_interval": 1,
        "plot_single_shot": False,
        
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this Experiment run
    N.num = 10000

    # set the qubit frequency sweep for this Experiment run

    DEL = Sweep(name="time_delay", start=4, stop=1_600, step=8, dtype=int)
    sweeps = [N, DEL]

    # DIS_AMPX = Sweep(
    #     name="disp_ampx",
    #     # points=[0.5, 1.75]
    #     points=[0.2, 0.4, 0.6, 0.8, 1.0, 1.2,1.4]
    # ) 
    # sweeps = [N, DIS_AMPX, DEL]

    PHASE.plot = True
    MAG.plot = True
    Q.plot = True
    I.plot = True
    SINGLE_SHOT.plot = False
    
    ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass
    I.fitfn = "gaussian"
    Q.fitfn = "gaussian"
    MAG.fitfn = "gaussian"
    PHASE.fitfn = "gaussian"

    PHASE.datafn_args = {"delay": 2.792e-7, "freq": RR.int_freq}
    
   
    datasets = [I, Q, MAG, PHASE]

    expt = CavityT2(FOLDER, modes, pulses, sweeps, datasets, **parameters)
    # expt.run(simulate=True)
    expt.run()