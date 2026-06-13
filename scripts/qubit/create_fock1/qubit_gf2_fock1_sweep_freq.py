import sys
from config.experiment_config import FOLDER, N, FREQ, I, Q, MAG, PHASE, RR, FREQ2

from qcore import Experiment, qua, Sweep
import numpy as np

class qubit_gf2_fock1_sweep_freq(Experiment):
    """Qubit spectroscopy"""

    ############################# DEFINE PRIMARY DATASETS ##############################
    # these Datasets form the "raw" experimental data and will be streamed by the OPX
    # they must be specified at experiment runtime

    primary_datasets = ["I", "Q"]

    ############################## DEFINE PRIMARY SWEEPS ###############################
    # these Sweeps are uniquely associated with the Experiment subclass
    # these Sweeps must be specified at experiment runtime

    primary_sweeps = ["drive_frequency"]

    ############################ DEFINE THE PULSE SEQUENCE #############################
    # ensure that you import 'qua' from 'qcore' and not from 'qm' library
    # attributes accessed via 'self' must be defined in 'if __name__ == "__main__"' code

    def sequence(self):
        """QUA sequence that defines this Experiment subclass"""
        # qua.reset_phase(self.qubit_gf2)
        # qua.reset_frame(self.qubit_gf2)
        # qua.update_frequency(self.qubit, self.qubit_frequency)
        qua.align()
        
        self.qubit_gf2.play(self.qubit_gf2_drive, ampx=1.0)
        qua.align()
        qua.update_frequency(self.drive, self.drive_frequency)
        # self.qubit_ef.play(self.qubit_ef_drive) 
        # qua.align(self.qubit_ef, self.drive)
        
        # self.drive.play(self.stark_drive, ampx=self.d_ampx) # fixed freq #, ampx=2.0 max , duration=self.length_drive
        self.drive.play(self.stark_drive)
        # self.snail.play(self.snail_pulse, duration=self.length_snail, ampx= self.snail_ampx)
        # self.qubit.play(self.qubit_pi)
        # qua.wait(self.time_delay, self.resonator)
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
        "drive": "drive_fock",
    }

    ################################### PULSE MAP ######################################
    # key: name of the Pulse as defined by the Experiment subclass
    # value: name of the Pulse as defined by the user in modes.yml

    pulses = {
        "stark_drive": "drive_constant_2000",
        "qubit_gf2_drive": "qubitGF2_gaussian_pi_16",
        "readout_pulse": "rr_readout_pulse",
    }

    ############################## CONTROL PARAMETERS ##################################

    parameters = {
        
        "wait_time": 500_000,
        "ro_ampx": 1.0,
        "qubit_drive_ampx": 1,
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this E xperiment run
    N.num = 500000

    # set the qubit frequency sweep for this Experiment run
    FREQ.name = "drive_frequency"
    FREQ.start = 60e6  # 40e6
    FREQ.stop = 80e6  # 60e6 #the 60e6 is from the lo used to generate ef pulse
    FREQ.num = 201
    # DEL = Sweep(name="length_drive", start=16, stop=64, step=8, dtype=int)
    # FREQ2.name = "drive_frequency"
    # FREQ2.start =-60e6  # 40e6
    # FREQ2.stop = -40e6  # 60e6 #the 60e6 is from the lo used to generate ef pulse
    # FREQ2.num = 101

    
    # D_AMPX = Sweep(
    #     name="d_ampx",
    #     # points=[0.01, 0.05, 0.08, 0.1, 0.2, 0.3, 0.4, 0.5]#0.25,0.5,0.75]
    #     #points=[0.1, 0.2, 0.3, 0.4, 0.5]
    #     points=[1.0, 1.1, 1.2, 1.3]#0.25,0.5,0.75]
    # ) 
    # DEL = Sweep(name="time_delay", start=16, stop=160, step=20, dtype=int)

    sweeps = [N, FREQ]#[N,  D_AMPX, FREQ]

    ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass

    PHASE.datafn_args = {"delay": 2.792e-7, "freq": RR.int_freq}
    PHASE.plot = True
    MAG.plot = True
    Q.plot = True
    I.plot = True
    I.fitfn = "gaussian"
    Q.fitfn = "gaussian"
    MAG.fitfn = "gaussian"
    datasets = [I, Q, MAG, PHASE]


    ######################## INITIALIZE AND RUN EXPERIMENT #############################
    expt = qubit_gf2_fock1_sweep_freq(FOLDER, modes, pulses, sweeps, datasets, **parameters)
    expt.run(simulate=False) #simulate=False
