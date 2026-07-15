""" """
import sys


from qm import qua as qm_qua
import numpy as np
from config.experiment_config import FOLDER, N, FREQ, I, Q, MAG, PHASE, MODES_CONFIG, RR
from qcore import Experiment, qua, Sweep
from qcore.helpers import Stage

import time

class cav_swap_1d_len_fock1_sweep_freq_new(Experiment):
    """Cavity T1"""

    ############################# DEFINE PRIMARY DATASETS ##############################
    # these Datasets form the "raw" experimental data and will be streamed by the OPX
    # they must be specified at experiment runtime

    primary_datasets = ["I", "Q"]

    ############################## DEFINE PRIMARY SWEEPS ###############################
    # these Sweeps are uniquely associated with the Experiment subclass
    # these Sweeps must be specified at experiment runtime

    primary_sweeps = ["length_snail"]

    ############################ DEFINE THE PULSE SEQUENCE #############################
    # ensure that you import 'qua' from 'qcore' and not from 'qm' library
    # attributes accessed via 'self' must be defined in 'if __name__ == "__main__"' code

    def sequence(self):
        """QUA sequence that defines this Experiment subclass"""
        qua.reset_phase(self.cavity)
        # qua.reset_frame(self.cavity)
        # qua.reset_phase(self.qubit)
        qua.reset_phase(self.snail)
        # qua.reset_frame(self.snail)
        qua.align()
        ## create coherent or fock 1
        self.qubit_gf2.play(self.qubit_gf2_drive)
        qua.align()
        self.drive.play(self.stark_drive) 
        #coherent 
        # self.cavity.play(self.cavity_drive, ampx=1)
        # qua.align(self.cavity, self.snail)
        qua.align()
        self.snail.play(self.snail_pulse, duration=self.length_snail) # #, ampx= self.snail_ampx
        # qua.wait(self.time_delay, self.cavity)
        qua.align(self.snail, self.qubit)
        self.qubit.play(self.qubit_pulse)
        qua.align(self.qubit, self.qubit_gf2)
        self.qubit_gf2.play(self.qubit_gf2_drive)
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
        "cavity": "cavity",
        "qubit": "qubit",
        "resonator": "rr",
        "snail": "snail_drive",
        "drive": "drive",
        "qubit_gf2": "qubit_GF2",
    }

    ################################### PULSE MAP ######################################
    # key: name of the Pulse as defined by the Experiment subclass
    # value: name of the Pulse as defined by the user in modes.yml

    pulses = {
        "cavity_drive": "cav_constant_48_ecd",
        "qubit_pulse": "qubit_gaussian_pi_2000",
        "readout_pulse": "rr_readout_pulse",
        "snail_pulse": "snail_drive_constant_2000",
        "stark_drive": "drive_constant_fock1",
        "qubit_gf2_drive": "qubitGF2_gaussian_pi_24",
    }

    ############################## CONTROL PARAMETERS ##################################

    parameters = {
        "wait_time":200_000, #30000,
        "ro_ampx": 1,
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this Experiment run
    N.num = 6000

    # set the qubit frequency sweep for this Experiment run

    # DEL = Sweep(name="time_delay", start=16, stop=1200000, step=8000, dtype=int)
    DEL = Sweep(name="length_snail", start=16, stop=400, step=4, dtype=int)
    # SNAIL_AMPX = Sweep(
    #     name="snail_ampx",
    #     points=[
    #        0.05, 0.1 # 0.05, 0.1
    #     ],
    # )
    sweeps = [N, DEL] #, SNAIL_AMPX

    ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass
    # MAG.fitfn = "exp_decay_sine"
    # PHASE.fitfn = "exp_decay_sine"
    # I.fitfn = "exp_decay_sine"
    # Q.fitfn = "exp_decay_sine"
    PHASE.plot = False
    MAG.plot = False
    Q.plot = False
    I.plot = False

    # MAG.axes = sweeps[1:]
    # PHASE.axes = sweeps[1:]
    PHASE.datafn_args = {"delay": 2.792e-7, "freq": RR.int_freq}
    # PHASE.plot = False
    datasets = [I, Q, MAG, PHASE]

    ######################## INITIALIZE AND RUN EXPERIMENT #############################

    # expt.run()
    IF_values =np.linspace(start=124.15e6-10e6, stop=124.2e6+12e6, num=441)

    for index_f in range(len(IF_values)): 
        with Stage(configpath=MODES_CONFIG, remote=True) as stage:
            (snail_drive,) = stage.get("snail_drive")
            snail_drive.configure(
                name="snail_drive",
                lo_name="opx1000",
                ports={"I": [1,5]},
                upconverter = 1,
                int_freq=IF_values[index_f],
                rf_switch=None,
                rf_switch_on=False,
            )
            expt = cav_swap_1d_len_fock1_sweep_freq_new(FOLDER, modes, pulses, sweeps, datasets, **parameters)
            expt.run()
            print(IF_values[index_f])
            # expt.run(simulate=True)
            time.sleep(1)  # Sleeps for 1 second; adjust as needed