""" """
import sys
# The directory containing the 'config' folder
FOLDER = "C:/Users/qcrew/Documents/eunice/"

# Add the FOLDER itself to sys.path, not the file path
if FOLDER not in sys.path:
    sys.path.insert(0, FOLDER)

from config.experiment_config import FOLDER, N, I, Q, SINGLE_SHOT, MAG, PHASE, RR
from qcore import Experiment, qua, Sweep
from cmath import phase
from qm import qua as qm_qua
from qcore.libs.qua_macros import QuaVariable
from qcore.helpers import logger
from qm import qua as qm_qua
import time
import numpy as np


class QubitT2_Echo(Experiment):
    """Qubit T2 Virtual Detuning"""

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
        factor = qm_qua.declare(qm_qua.fixed)
        # phase = qm_qua.declare(float)
        qm_qua.assign(factor, self.detuning * 1e-9)

        """QUA sequence that defines this Experiment subclass"""
        qua.reset_frame(self.qubit)
        qua.reset_phase(self.qubit)

        self.qubit.play(self.qubit_drive) # pi/2
        qua.wait(self.time_delay / 2, self.qubit)  # Half wait
        
        self.qubit.play(self.echo_pulse)
        qua.wait(self.time_delay / 2, self.qubit)  # Half wait
        
        qm_qua.assign(self.phase, qm_qua.Cast.mul_fixed_by_int(factor, self.time_delay))
        self.qubit.play(self.qubit_drive, phase=self.phase) # pi/2
        qua.align(self.qubit, self.resonator)
        
        self.resonator.measure(self.readout_pulse, (self.I, self.Q), ampx=self.ro_ampx, demod_type="dual")
        if self.plot_single_shot:  # assign state to G or E
            qm_qua.assign(self.single_shot,qm_qua.Cast.to_fixed(self.I > self.readout_pulse.threshold),)
        qua.wait(self.wait_time, self.resonator)

if __name__ == "__main__":
    """ """

    #################################### MODE MAP ######################################
    # key: name of the Mode as defined by the Experiment subclass
    # value: name of the Mode as defined by the user in modes.yml
    modes = {
        "qubit": "qubit",
        "resonator": "rr",
    }

    ################################### PULSE MAP ######################################
    # key: name of the Pulse as defined by the Experiment subclass
    # value: name of the Pulse as defined by the user in modes.yml
    pulses = {
        "qubit_drive": "qubit_constant_pi2_24",
        "echo_pulse": "qubit_constant_pi_24",
        "readout_pulse": "rr_readout_pulse",
    }

    ############################## CONTROL PARAMETERS ##################################

    parameters = {
        "wait_time": 150_000,
        "ro_ampx": 1,
        "detuning":2e6,
        "phase": QuaVariable(
            value=0.0,
            dtype=qm_qua.fixed,
            tag="phase",
            buffer=True,
            stream=True,
        ),
        "plot_single_shot": False,
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this Experiment run
    N.num = 5000

    # set the qubit frequency sweep for this Experiment run

    # DEL = Sweep(name="time_delay", start=10, stop=140000, step=800, dtype=int)
    DEL = Sweep(name="time_delay", start=16, stop=20_000, step=40, dtype=int)
    sweeps = [N, DEL]

    ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass
    I.fitfn = "exp_decay_sine"
    Q.fitfn = "exp_decay_sine"
    MAG.fitfn = "exp_decay_sine"
    PHASE.fitfn = "exp_decay_sine"
    SINGLE_SHOT.fitfn = "exp_decay_sine"
    print(SINGLE_SHOT.best_fit, SINGLE_SHOT.fit_params)

    # SINGLE_SHOT.fitfn = "exp_decay_sine"
    PHASE.datafn_args = {"delay": 2.792e-7, "freq": RR.int_freq}

    MAG.plot = True
    PHASE.plot = False
    I.plot = True
    Q.plot = True
    SINGLE_SHOT.plot = False
    datasets = [I, Q, MAG, PHASE]

    ######################## INITIALIZE AND RUN EXPERIMENT #############################

    expt = QubitT2_Echo(FOLDER, modes, pulses, sweeps, datasets, **parameters)
    expt.run(simulate=False)
