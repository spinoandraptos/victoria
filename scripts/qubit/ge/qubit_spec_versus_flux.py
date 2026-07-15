import sys


from qm import qua as qm_qua
import numpy as np
from config.experiment_config import FOLDER, N, FREQ, I, Q, MAG, PHASE, MODES_CONFIG, RR
from qcore import Experiment, qua, Sweep
from qcore.helpers import Stage

import time

class qubit_spec_versus_flux(Experiment):
    """Cavity spectroscopy"""

    ############################# DEFINE PRIMARY DATASETS ##############################
    # these Datasets form the "raw" experimental data and will be streamed by the OPX
    # they must be specified at experiment runtime

    primary_datasets = ["I", "Q"]

    ############################## DEFINE PRIMARY SWEEPS ###############################
    # these Sweeps are uniquely associated with the Experiment subclass
    # these Sweeps must be specified at experiment runtime

    primary_sweeps = ["qubit_frequency"]

    ############################ DEFINE THE PULSE SEQUENCE #############################
    # ensure that you import 'qua' from 'qcore' and not from 'qm' library
    # attributes accessed via 'self' must be defined in 'if __name__ == "__main__"' code

    def sequence(self):
        """QUA sequence that defines this Experiment subclass"""
        #qua.reset_phase(self.cavity)
        #qua.reset_frame(self.cavity)
    
        
        # There are two cavity modes here, please check which mode is used.
        # qua.update_frequency(self.cavity, self.cavity_frequency)
        qua.update_frequency(self.qubit, self.qubit_frequency)
        self.qubit.play(self.qubit_pulse)
        
        qua.align(self.qubit, self.resonator)
        # qua.update_frequency(self.resonator, self.resonator_frequency)
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
        
        "qubit": "qubit",
        "resonator": "rr",
        
    }

    ################################### PULSE MAP ######################################
    # key: name of the Pulse as defined by the Experiment subclass
    # value: name of the Pulse as defined by the user in modes.yml

    pulses = {
        
        "qubit_pulse": "qubit_constant_10000",
        
        "readout_pulse": "rr_readout_pulse",
    }

    ############################## CONTROL PARAMETERS ############# #####################

    parameters = {
        "wait_time": 10_000,
        "ro_ampx": 1,
        "cav_ampx": 1,
        "fetch_interval": 1,
        "plot_single_shot": False,
        # "resonator_frequency": -50e6
        
        
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this Experiment run
    N.num = 20000

    # set the qubit frequency sweep for this Experiment run
    
    FREQ.name = "qubit_frequency"
    FREQ.start =-400e6
    FREQ.stop =0e6 
    FREQ.num = 201
    #PULSE_LENGTH = Sweep(name="cav_pulse_length", start=16, stop=400, step=16, dtype=int)
    # QB_AMPX = Sweep(
    #     name="qb_ampx",
    #     points=[0.0, 1.0],
    # )
    PHASE.plot = False
    MAG.plot = False
    Q.plot = False
    I.plot = False
    # SINGLE_SHOT.plot = False
    
    sweeps = [N, FREQ]
    #SINGLE_SHOT.plot_args["plot_type"] = "image"

    ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass


    PHASE.datafn_args = {"delay": 2.792e-7, "freq": RR.int_freq}
    
   
    datasets = [I, Q, MAG, PHASE]
    ######################## INITIALIZE AND RUN EXPERIMENT #############################
    

    # flux_values = np.linspace(start=-20e-3, stop=-10e-3, num=11)



    current_A_print = np.linspace(start=-15e-3, stop=5e-3, num=21)
    # current_A_print =[-0.015, -0.01495, -0.0149, -0.01485, -0.0148, -0.01475, -0.0147, -0.01465, -0.0145, -0.01445, -0.0144, -0.0143, -0.01425, -0.01415, -0.0141, -0.01405, -0.014, -0.01395, -0.0139, -0.01385, -0.0138, -0.01375, -0.01365, -0.0136, -0.01355, -0.0134, -0.01335, -0.0133, -0.01325, -0.0132, -0.01315, -0.0129, -0.01285, -0.0128, -0.01275, -0.0127, -0.01265, -0.0126, -0.01255, -0.0125, -0.01245, -0.0124, -0.01235, -0.0123, -0.01225, -0.0122, -0.01215, -0.0121, -0.01205, -0.012, -0.01195, -0.0119, -0.01185, -0.0118, -0.01175, -0.0117, -0.01165, -0.0116, -0.01155, -0.0115, -0.01145, -0.0114, -0.01135, -0.0113, -0.01125, -0.0112, -0.01115, -0.0111, -0.01105, -0.011, -0.01095, -0.0109, -0.01085, -0.0108, -0.01075, -0.0107, -0.01065, -0.0106, -0.01055, -0.0105, -0.01045, -0.0104, -0.01035, -0.0103, -0.01025, -0.0102, -0.0101, -0.01005, -0.01, -0.00995, -0.00985, -0.0098, -0.00975, -0.0097, -0.00965, -0.0095, -0.00945, -0.0094, -0.00935, -0.0092, -0.00915, -0.0091, -0.00905, -0.009, -0.00895, -0.0089, -0.00885, -0.0086, -0.00855, -0.0085, -0.00845, -0.0084, -0.00835, -0.0083, -0.00825, -0.0082, -0.00815, -0.0081, -0.00805, -0.008]
    # if_freq=[-104000074, -104000074, -104000074, -104000074, -106666740, -106666740, -106666740, -106666740, -114666738, -114666738, -114666738, -120000070, -120000070, -128000068, -128000068, -128000068, -133333400, -133333400, -138666732, -138666732, -24000094, -24000094, -34666758, -34666758, -34666758, -42666756, -42666756, -48000088, -48000088, -50666754, -50666754, -58666752, -58666752, -61333418, -61333418, -64000084, -64000084, -64000084, -64000084, -64000084, -66666750, -66666750, -66666750, -66666750, -66666750, -66666750, -69333416, -69333416, -69333416, -69333416, -69333416, -69333416, -69333416, -69333416, -69333416, -69333416, -69333416, -69333416, -69333416, -69333416, -69333416, -69333416, -69333416, -69333416, -69333416, -69333416, -69333416, -66666750, -66666750, -66666750, -66666750, -66666750, -66666750, -66666750, -64000084, -64000084, -64000084, -64000084, -64000084, -64000084, -61333418, -61333418, -61333418, -58666752, -58666752, -58666752, -56000086, -56000086, -53333420, -53333420, -42666756, -42666756, -42666756, -40000090, -40000090, -29333426, -29333426, -24000094, -24000094, -8000098, -8000098, -128000068, -128000068, -125333402, -125333402, -120000070, -120000070, -109333406, -109333406, -109333406, -106666740, -106666740, -106666740, -104000074, -104000074, -104000074, -104000074, -104000074, -104000074, -104000074]
    # if_freq = [-50180000, -50180000, -50180000, -50160000, -50160000, -50120000,
    #     -50100000, -50060000, -50020000, -49960000, -49940000, -49960000]

    
    for index_f in range(len(current_A_print)): 
        with Stage(configpath=MODES_CONFIG, remote=True) as stage:
            (yoko1,cavity,opx1000) = stage.get("yoko1", "cavity","opx1000")
            
            yoko_target = current_A_print[index_f]
            yoko1.ramp(yoko_target, step=0.1e-3)
            # parameters["resonator_frequency"] = if_freq[index_f]
            expt = qubit_spec_versus_flux(FOLDER, modes, pulses, sweeps, datasets, **parameters)
            expt.run()
            # expt.run(simulate=True)
            time.sleep(1)  # Sleeps for 1 second; adjust as needed
    # yoko1.ramp(0e-3, step=1e-4)

