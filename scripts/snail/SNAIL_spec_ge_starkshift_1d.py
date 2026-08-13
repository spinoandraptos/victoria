import sys
from config.experiment_config import FOLDER, N, FREQ, I, Q, MAG, PHASE, RR

from qcore import Experiment, qua, Sweep
import numpy as np

class SNAILSpec_ge_Stark_1d(Experiment):
    """Qubit spectroscopy"""

    ############################# DEFINE PRIMARY DATASETS ##############################
    # these Datasets form the "raw" experimental data and will be streamed by the OPX
    # they must be specified at experiment runtime

    primary_datasets = ["I", "Q"]

    ############################## DEFINE PRIMARY SWEEPS ###############################
    # these Sweeps are uniquely associated with the Experiment subclass
    # these Sweeps must be specified at experiment runtime

    primary_sweeps = ["snail_frequency"]

    ############################ DEFINE THE PULSE SEQUENCE #############################
    # ensure that you import 'qua' from 'qcore' and not from 'qm' library
    # attributes accessed via 'self' must be defined in 'if __name__ == "__main__"' code


    def sequence(self):
        """QUA sequence that defines this Experiment subclass"""
        # qua.reset_phase(self.resonator)
        qua.update_frequency(self.snail, self.snail_frequency)
        #qua.update_frequency(self.resonator, self.resonator_frequency)
        qua.align()
        self.drive.play(self.stark_drive, ampx=self.stark_ampx) # fixed freq
        self.snail.play(self.snail_pulse, ampx=2.)
        qua.align()
        self.qubit.play(self.qubit_drive)
        qua.align()
        self.resonator.measure(
            self.readout_pulse, (self.I, self.Q), ampx=self.ro_ampx, demod_type="dual"
        )
        qua.wait(self.wait_time, self.resonator)


if __name__ == "__main__":
    """ """

    #################################### MODE MAP ######################################
    # key: name of the Mode as defined by the Experiment subclass
    # value: name of the Mode as defined by the user in modes.yml

    modes = {
        "drive": "snail_stark_drive",
        "qubit": "qubit",
        "resonator": "rr",
        "snail": "snail_drive",
    }

    ################################### PULSE MAP ######################################
    # key: name of the Pulse as defined by the Experiment subclass
    # value: name of the Pulse as defined by the user in modes.yml

    pulses = {
        "stark_drive": "snail_stark_drive_constant_2000",
        "qubit_drive": "qubit_constant_pi_pulse_1200",#"qubit_constant_pulse",#"qubit_constant_pi_1500",
        "readout_pulse": "rr_readout_pulse",
        "snail_pulse": "snail_drive_constant_2000",
    }

    ############################## CONTROL PARAMETERS ##################################

    parameters = {
        "wait_time": 30_000,
        "ro_ampx": 1.0,
        "qubit_drive_ampx": 1,
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this E xperiment run
    N.num = 500000

    # set the qubit frequency sweep for this Experiment run
    FREQ.name = "snail_frequency"
    FREQ.start = -110e6
    FREQ.stop =-70e6
    FREQ.num = 71
    
    # Q_AMPX = Sweep(
    #     name="q_ampx",
    #     # points=[0.01, 0.05, 0.08, 0.1, 0.2, 0.3, 0.4, 0.5]#0.25,0.5,0.75]
    #     #points=[0.1, 0.2, 0.3, 0.4, 0.5]
    #     #points=[0.0, 0.2, 0.4, 0.6, 0.8, 1.0 ]#0.25,0.5,0.75]
    # )
    STARK_AMPX = Sweep(name="stark_ampx", start=0, stop=1, num=9)
    

    PHASE.plot = True
    MAG.plot = True
    Q.plot = True
    I.plot = True
    # SINGLE_SHOT.plot = False
    
    sweeps = [N, STARK_AMPX, FREQ]
    #SINGLE_SHOT.plot_args["plot_type"] = "image"

    ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass

    I.fitfn = "gaussian"
    Q.fitfn = "gaussian"
    MAG.fitfn = "gaussian"
    PHASE.fitfn = "gaussian"
    
    datasets = [I, Q, MAG, PHASE]

    ######################## INITIALIZE AND RUN EXPERIMENT #############################
    expt = SNAILSpec_ge_Stark_1d(FOLDER, modes, pulses, sweeps, datasets, **parameters)
    expt.run(simulate=False) #simulate=False
