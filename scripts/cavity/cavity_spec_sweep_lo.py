""" """
""" """
import sys

from config.experiment_config import FOLDER, N, FREQ, I, Q, MAG, PHASE, SINGLE_SHOT, RR

from qcore import Experiment, qua, Sweep
from qm import qua as qm_qua
from qcore.helpers import Stage
from config.experiment_config import MODES_CONFIG
import numpy as np
import time


class CavitySpec(Experiment):
    """Cavity spectroscopy"""

    ############################# DEFINE PRIMARY DATASETS ##############################
    # these Datasets form the "raw" experimental data and will be streamed by the OPX
    # they must be specified at experiment runtime

    primary_datasets = ["I", "Q"]

    ############################## DEFINE PRIMARY SWEEPS ###############################
    # these Sweeps are uniquely associated with the Experiment subclass
    # these Sweeps must be specified at experiment runtime

    primary_sweeps = ["cavity_frequency"]

    ############################ DEFINE THE PULSE SEQUENCE #############################
    # ensure that you import 'qua' from 'qcore' and not from 'qm' library
    # attributes accessed via 'self' must be defined in 'if __name__ == "__main__"' code

    def sequence(self):
        """QUA sequence that defines this Experiment subclass"""
        #qua.reset_phase(self.cavity)
        #qua.reset_frame(self.cavity)
       
        
        # There are two cavity modes here, please check which mode is used.
        qua.update_frequency(self.cavity, self.cavity_frequency)
        self.cavity.play(self.cavity_pulse, ampx = self.cav_ampx)
        qua.align(self.cavity, self.qubit)
        # qua.wait(32, self.qubit)
        self.qubit.play(self.qubit_pulse)
        qua.align(self.qubit, self.resonator)
        qua.align()
        self.resonator.measure(self.readout_pulse, (self.I, self.Q), ampx=self.ro_ampx)
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
        "cavity": "cav",
        "qubit": "qubit",
        "resonator": "rr",
    }

    ################################### PULSE MAP ######################################
    # key: name of the Pulse as defined by the Experiment subclass
    # value: name of the Pulse as defined by the user in modes.yml

    pulses = {
        "cavity_pulse": "cavity_constant_pulse_10000",
        "qubit_pulse": "qubit_constant_pi_pulse_300",
        "readout_pulse": "rr_readout_pulse",
    }

    ############################## CONTROL PARAMETERS ############# #####################

    parameters = {
        "wait_time": 600_000,
        "ro_ampx": 1,
        "cav_ampx": 1,
        "fetch_interval": 1,
        "plot_single_shot": False,
        
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this Experiment run
    N.num = 100000

    # set the qubit frequency sweep for this Experiment run
    
    FREQ.name = "cavity_frequency"
    FREQ.start =-200e6
    FREQ.stop =200e6 
    FREQ.num = 2001
    #PULSE_LENGTH = Sweep(name="cav_pulse_length", start=16, stop=400, step=16, dtype=int)
    # QB_AMPX = Sweep(
    #     name="qb_ampx",
    #     points=[0.0, 1.0],
    # )
    PHASE.plot = False
    MAG.plot = False
    Q.plot = False
    I.plot = False
    SINGLE_SHOT.plot = False
    
    sweeps = [N, FREQ]
    #SINGLE_SHOT.plot_args["plot_type"] = "image"

    ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass
    # I.fitfn = "gaussian"
    # Q.fitfn = "gaussian"
    # MAG.fitfn = "gaussian"
    # PHASE.fitfn = "gaussian"

    PHASE.datafn_args = {"delay": 2.792e-7, "freq": RR.int_freq}
    
   
    datasets = [I, Q, MAG, PHASE]
    lo_cav_values = np.arange(6.7e9, 7.9e9 + 400e6, 400e6)

    # Generate the linearly spaced values
    # LO_list = flux_values
    with Stage(configpath=MODES_CONFIG, remote=True) as stage:
        lo_qubit, lo_rr, lo_cav = stage.get("lo_qubit", "lo_rr", "lo_cav")
        
        for index_q in range(len(lo_cav_values)):
            lo_cav.frequency = lo_cav_values[index_q]
            lo_cav.power = 15.0
            lo_cav.output = True
            expt = CavitySpec(FOLDER, modes, pulses, sweeps, datasets, **parameters)
            expt.run()
            # expt.run(simulate=True)
            time.sleep(1)  # Sleeps for 1 second; adjust as needed
        
