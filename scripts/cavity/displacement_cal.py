""" """
""" """
""" """
import sys
# The directory containing the 'config' folder
FOLDER = "C:/Users/qcrew/Documents/eunice/"

# Add the FOLDER itself to sys.path, not the file path
if FOLDER not in sys.path:
    sys.path.insert(0, FOLDER)
    
from config.experiment_config import FOLDER, N, FREQ, I, Q, MAG, PHASE, RR, SINGLE_SHOT
from qm import qua as qm_qua
from qcore import Experiment, qua, Sweep
import numpy as np


class CavDisplacementCalSelective(Experiment):
    """Dispersive shift between cavity and qubit"""

    ############################# DEFINE PRIMARY DATASETS ##############################
    # these Datasets form the "raw" experimental data and will be streamed by the OPX
    # they must be specified at experiment runtime

    primary_datasets = ["I", "Q"]

    ############################## DEFINE PRIMARY SWEEPS ###############################
    # these Sweeps are uniquely associated with the Experiment subclass
    # these Sweeps must be specified at experiment runtime

    primary_sweeps = ["cav_ampx"]

    ############################ DEFINE THE PULSE SEQUENCE #############################
    # ensure that you import 'qua' from 'qcore' and not from 'qm' library
    # attributes accessed via 'self' must be defined in 'if __name__ == "__main__"' code

    def sequence(self):
        """QUA sequence that defines this Experiment subclass"""
        qua.reset_phase(self.cavity)
        qua.reset_frame(self.cavity)
        # qua.reset_phase(self.qubit)
        # qua.reset_frame(self.qubit)
            
        qua.align()
        self.cavity.play(self.cav_displacement, ampx=self.cav_ampx)  # create a coherent state
        qua.align() 
        self.qubit.play(self.qubit_selective_pi)
        qua.align()
        self.resonator.measure(self.readout_pulse, (self.I, self.Q), demod_type="dual")

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
        "cavity": "cavity",
        # "cavity_e": "alice_e",
        "resonator": "rr",
    }

    ################################### PULSE MAP ######################################
    # key: name of the Pulse as defined by the Experiment subclass
    # value: name of the Pulse as defined by the user in modes.yml

    pulses = {
        "cav_displacement": "cav_constant_100",
        # "qubit_pi_pulse": "qubit_pi_9",
        "qubit_selective_pi": "qubit_constant_pi_400",
        "readout_pulse": "rr_readout_pulse",
    }

    ############################## CONTROL PARAMETERS ##################################

    parameters = {
        "wait_time": 800_000,
        "plot_single_shot": False,
     

    }

    ######################## SWEEP (INDEPENDENT) VARIABLES ############ #################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this Experiment run
    N.num = 50000

    # set the delay sweep
    CAV_AMP = Sweep(name="cav_ampx", start=0, stop=1.8, step=0.015)

 
    
    sweeps = [N, CAV_AMP]

    ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass
    
    from qcore import Dataset
    # PRESELECT = Dataset(
    #     name="preselect",
    #     save=True,
    #     plot=False,
    # )

    # MAG.axes = sweeps[1:]
    # PHASE.axes = sweeps[1:]
    PHASE.datafn_args = {"delay": 2.792e-7, "freq": RR.int_freq}  # 2.792e-7
    PHASE.plot = True
    MAG.plot = True
    Q.plot = True
    I.plot = True
    I.fitfn = "displacement_cal"
    Q.fitfn = "displacement_cal"
    MAG.fitfn = "displacement_cal"
    PHASE.fitfn = "displacement_cal"
    datasets = [I, Q, MAG, PHASE]

    ######################## INITIALIZE AND RUN EXPERIMENT #############################
    # cavities = ["Alice", "Bob", "Charlie"]
    # ampx_list = [1.0]
    # for cavity in cavities:
    #     if cavity == "Alice":
    #         modes["cavity"] = "alice"
    #         pulses["cav_displacement"] = "a_d_large"
    #     elif cavity == "Bob":
    #         modes["cavity"] = "bob"
    #         pulses["cav_displacement"] = "b_d_large"
    #     elif cavity == "Charlie":
    #         modes["cavity"] = "charlie"
    #         pulses["cav_displacement"] = "c_s100"
    # for ampx_item in ampx_list:
    #     parameters["cav_ampx"] = ampx_item
    expt = CavDisplacementCalSelective(FOLDER, modes, pulses, sweeps, datasets, **parameters)
    expt.run()
