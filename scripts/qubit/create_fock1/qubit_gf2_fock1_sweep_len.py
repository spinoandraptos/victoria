import sys
from config.experiment_config import FOLDER, N, FREQ, I, Q, MAG, PHASE, RR, FREQ2

from qcore import Experiment, qua, Sweep
import numpy as np

class qubit_gf2_fock1_sweep_len(Experiment):
    """Qubit spectroscopy"""

    ############################# DEFINE PRIMARY DATASETS ##############################
    # these Datasets form the "raw" experimental data and will be streamed by the OPX
    # they must be specified at experiment runtime

    primary_datasets = ["I", "Q"]

    ############################## DEFINE PRIMARY SWEEPS ###############################
    # these Sweeps are uniquely associated with the Experiment subclass
    # these Sweeps must be specified at experiment runtime

    primary_sweeps = ["length_drive"]

    ############################ DEFINE THE PULSE SEQUENCE #############################
    # ensure that you import 'qua' from 'qcore' and not from 'qm' library
    # attributes accessed via 'self' must be defined in 'if __name__ == "__main__"' code

    def sequence(self):
        """QUA sequence that defines this Experiment subclass"""
        # qua.reset_phase(self.qubit_gf2)
        # qua.reset_frame(self.qubit_gf2)
        # qua.update_frequency(self.qubit, self.qubit_frequency)
        # qua.align()
        
        self.qubit_gf2.play(self.qubit_gf2_drive)
        qua.align()
        # qua.update_frequency(self.drive) 
        # self.qubit_ef.play(self.qubit_ef_drive) 
        # qua.align(self.qubit_ef, self.drive)
        
        self.drive.play(self.stark_drive, duration=self.length_drive/4) # divide by 4 to convert seconds to clock cycle# fixed freq #, ampx=2.0 max , duration=self.length_drive
        # self.drive.play(self.stark_drive, duration=self.length_drive) # fixed freq #, ampx=2.0 max , duration=self.length_drive
        # self.snail.play(self.snail_pulse, duration=self.length_snail, ampx= self.snail_ampx)
        # self.qubit_gf2.play(self.qubit_gf2_drive)
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
        "qubit_gf2": "qubit_GF2",
        "resonator": "rr",
        "drive": "drive",
    }

    ################################### PULSE MAP ######################################
    # key: name of the Pulse as defined by the Experiment subclass
    # value: name of the Pulse as defined by the user in modes.yml

    pulses = {
        "stark_drive": "drive_constant_160",
        "qubit_gf2_drive": "qubitGF2_gaussian_pi_192",
        "readout_pulse": "rr_readout_pulse",
    }

    ############################## CONTROL PARAMETERS ##################################

    parameters = {
        "wait_time": 1_000_000,
        "ro_ampx": 1.0,
        "qubit_drive_ampx": 1,
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this E xperiment run
    N.num = 500000

    # set the qubit frequency sweep for this Experiment run
    DEL = Sweep(name="length_drive", start=4, stop=4000, step=40, dtype=int)
    # DEL = Sweep(name="length_drive", start=16, stop=64, step=8, dtype=int)
    # FREQ2.name = "drive_frequency"
    # FREQ2.start =-60e6  # 40e6
    # FREQ2.stop = -40e6  # 60e6 #the 60e6 is from the lo used to generate ef pulse
    # FREQ2.num = 101

    
    # D_AMPX = Sweep(
    #     name="d_ampx",
    #     # points=[0.01, 0.05, 0.08, 0.1, 0.2, 0.3, 0.4, 0.5]#0.25,0.5,0.75]
    #     #points=[0.1, 0.2, 0.3, 0.4, 0.5]
    #     points=[0.0,0.5, 1, ]#0.25,0.5,0.75]
    # ) 
    

    sweeps = [N,  DEL]

    ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass

    PHASE.datafn_args = {"delay": 2.792e-7, "freq": RR.int_freq}
    PHASE.plot = True
    MAG.plot = True
    Q.plot = True
    I.plot = True
    I.fitfn, Q.fitfn, MAG.fitfn = (
    "sine",
    "sine",
    "sine",
    # "sine",
    # "sine_gf",
    # "sine_gf",
    # "sine_gf",
)
    #I.plot = True
    # Q.plot_args["plot_type"] = "image"
    #I.plot_args["plot_type"] = "image"
    # SINGLE_SHOT.plot_args["plot_type"] = "image"
    # SINGLE_SHOT.plot = True
    datasets = [I, Q, MAG, PHASE]


    ######################## INITIALIZE AND RUN EXPERIMENT #############################
    expt = qubit_gf2_fock1_sweep_len(FOLDER, modes, pulses, sweeps, datasets, **parameters)
    expt.run() #simulate=False
