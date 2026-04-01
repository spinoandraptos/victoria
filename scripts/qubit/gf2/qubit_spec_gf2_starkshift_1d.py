import sys
from config.experiment_config import FOLDER, N, FREQ, I, Q, MAG, PHASE, RR

from qcore import Experiment, qua, Sweep
import numpy as np

class QubitSpec_gf2_Stark1d(Experiment):
    """Qubit spectroscopy"""

    ############################# DEFINE PRIMARY DATASETS ##############################
    # these Datasets form the "raw" experimental data and will be streamed by the OPX
    # they must be specified at experiment runtime

    primary_datasets = ["I", "Q"]

    ############################## DEFINE PRIMARY SWEEPS ###############################
    # these Sweeps are uniquely associated with the Experiment subclass
    # these Sweeps must be specified at experiment runtime

    primary_sweeps = ["qubit_gf2_frequency"]

    ############################ DEFINE THE PULSE SEQUENCE #############################
    # ensure that you import 'qua' from 'qcore' and not from 'qm' library
    # attributes accessed via 'self' must be defined in 'if __name__ == "__main__"' code


    def sequence(self):
        """QUA sequence that defines this Experiment subclass"""
        qua.reset_phase(self.resonator)
        qua.update_frequency(self.qubit_gf2, self.qubit_gf2_frequency)
        #qua.update_frequency(self.resonator, self.resonator_frequency)
        qua.align()
        self.drive.play(self.stark_drive) # fixed freq #, ampx=self.q_ampx
        self.qubit_gf2.play(self.qubit_gf2_drive, ampx=self.qubit_drive_ampx)
        qua.align(self.qubit_gf2, self.resonator)
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
        "qubit_gf2": "qubit_GF2",
        "resonator": "rr",
        "drive": "drive",
    }

    ################################### PULSE MAP ######################################
    # key: name of the Pulse as defined by the Experiment subclass
    # value: name of the Pulse as defined by the user in modes.yml

    pulses = {
        "stark_drive": "drive_gaussian_pi_64",
        "qubit_gf2_drive": "qubitGF_gaussian_pi_64",#"qubit_constant_pulse",#"qubit_constant_pi_1500",
        "readout_pulse": "rr_readout_pulse",
    }

    ############################## CONTROL PARAMETERS ##################################

    parameters = {
        "wait_time": 5000,
        "ro_ampx": 1.0,
        "qubit_drive_ampx": 1,
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this E xperiment run
    N.num = 500000

    # set the qubit frequency sweep for this Experiment run
    FREQ.name = "qubit_gf2_frequency"
    FREQ.start =-200e6  # 40e6
    FREQ.stop = 200e6  # 60e6 #the 60e6 is from the lo used to generate ef pulse
    FREQ.num = 51

    
    # Q_AMPX = Sweep(
    #     name="q_ampx",
    #     # points=[0.01, 0.05, 0.08, 0.1, 0.2, 0.3, 0.4, 0.5]#0.25,0.5,0.75]
    #     #points=[0.1, 0.2, 0.3, 0.4, 0.5]
    #     points=[0.0, 0.05, 0.1, 0.15,0.2,0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]#0.25,0.5,0.75]
    # ) 
    

    sweeps = [N, FREQ]
    # sweeps = [N, Q_AMPX, FREQ]

    ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass

    # PHASE.datafn_args = {"delay": 2.792e-7, "freq": RR.int_freq}
    # PHASE.plot = False
    # MAG.plot = False
    # # Q.plot = False
    # I.plot = False
    # #I.plot = True
    # Q.plot_args["plot_type"] = "image"
    # I.plot_args["plot_type"] = "image"
    # SINGLE_SHOT.plot_args["plot_type"] = "image"
    # SINGLE_SHOT.plot = True
    PHASE.datafn_args = {"delay": 2.792e-7, "freq": RR.int_freq}
    PHASE.plot = True
    I.plot = True
    Q.plot = True
    MAG.plot = True

    I.fitfn = "gaussian"
    Q.fitfn = "gaussian"
    MAG.fitfn = "gaussian"
    datasets = [I, Q, MAG, PHASE]

    ######################## INITIALIZE AND RUN EXPERIMENT #############################
    expt = QubitSpec_gf2_Stark1d(FOLDER, modes, pulses, sweeps, datasets, **parameters)
    expt.run(simulate=False) #simulate=False
