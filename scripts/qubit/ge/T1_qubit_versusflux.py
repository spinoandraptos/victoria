import sys


from qm import qua as qm_qua
import numpy as np
from config.experiment_config import FOLDER, N, FREQ, I, Q, MAG, PHASE, MODES_CONFIG, RR
from qcore import Experiment, qua, Sweep
from qcore.helpers import Stage

import time

class QubitT1_versus_flux(Experiment):
    """Cavity spectroscopy"""

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
        self.qubit.play(self.qubit_drive)
        qua.wait(self.time_delay, self.qubit)
        qua.align(self.qubit, self.resonator)
        self.resonator.measure(
            self.readout_pulse, (self.I, self.Q), ampx=self.ro_ampx, demod_type="dual"
        )
        qua.align()
        qua.wait(self.wait_time)


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
        "qubit_drive": "qubit_gaussian_pulse_60",
        "readout_pulse": "rr_readout_pulse",
    }

    ############################## CONTROL PARAMETERS ##################################

    parameters = {
        "wait_time": 10_000,
        "ro_ampx": 1.0,
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this Experiment run
    N.num = 10000

    # set the qubit frequency sweep for this Experiment run

    DEL = Sweep(name="time_delay", start=16, stop=10_000, step=100, dtype=int)
    sweeps = [N, DEL]

    ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass

    PHASE.datafn_args = {"delay": 2.792e-7, "freq": RR.int_freq}
    PHASE.plot = True
    MAG.plot = True
    Q.plot = True
    I.plot = True
    MAG.fitfn = "exp_decay"
    Q.fitfn = "exp_decay"
    I.fitfn = "exp_decay"
    # MAG.fitfn = "exp_decay"
    PHASE.fitfn = "exp_decay"
    # SINGLE_SHOT.plot = False
    
  
    
   
    datasets = [I, Q, MAG, PHASE]
    ######################## INITIALIZE AND RUN EXPERIMENT #############################
    

    # flux_values = np.linspace(start=-20e-3, stop=20e-3, num=801)
    flux_values = np.linspace(start=0e-3, stop=10e-3, num=11)
    for index_f in range(len(flux_values)): 
        with Stage(configpath=MODES_CONFIG, remote=True) as stage:
            (yoko1,) = stage.get("yoko1")
            yoko_target = flux_values[index_f]
            yoko1.ramp(yoko_target, step=0.1e-3)
            expt = QubitT1_versus_flux(FOLDER, modes, pulses, sweeps, datasets, **parameters)
            expt.run()
            # expt.run(simulate=True)
            time.sleep(1)  # Sleeps for 1 second; adjust as needed
    # yoko1.ramp(0e-3, step=1e-4)
