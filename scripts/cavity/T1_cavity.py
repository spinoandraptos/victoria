""" """
import sys
# The directory containing the 'config' folder
FOLDER = "C:/Users/qcrew/Documents/eunice/"

# Add the FOLDER itself to sys.path, not the file path
if FOLDER not in sys.path:
    sys.path.insert(0, FOLDER)

from config.experiment_config import FOLDER, N, I, Q, MAG, PHASE, RR, SINGLE_SHOT
from qcore import Experiment, qua, Sweep
from qm import qua as qm_qua


class CavityT1(Experiment):
    """Cavity T1"""

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
    
        self.cavity.play(self.cavity_drive, ampx=1.0)
        # self.cavity.play(self.cavity_drive)
        #self.cavity.play(self.cavity_drive)
        qua.wait(self.time_delay, self.cavity)
        qua.align()
        # qua.align(self.cavity, self.qubit)
        self.qubit.play(self.qubit_pulse)
        qua.align(self.qubit, self.resonator)
        self.resonator.measure(self.readout_pulse, (self.I, self.Q), ampx=self.ro_ampx, demod_type='dual')
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
        "cavity": "cavity",#"cav",
        "qubit": "qubit",
        "resonator": "rr",
        
    }

    ################################### PULSE MAP ######################################
    # key: name of the Pulse as defined by the Experiment subclass
    # value: name of the Pulse as defined by the user in modes.yml

    pulses = {
        "cavity_drive": "cav_constant_400",
        "qubit_pulse": "qubit_constant_pi_400",
        "readout_pulse": "rr_readout_pulse",
    }

    ############################## CONTROL PARAMETERS ##################################

    parameters = {
        "wait_time": 1000000,
        "ro_ampx": 1,
        "plot_single_shot": False,
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this Experiment run
    N.num = 100000

    # set the qubit frequency sweep for this Experiment run

    DEL = Sweep(name="time_delay", start=10, stop=6_000, step=50, dtype=int)
    sweeps = [N, DEL]

    ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass
    MAG.fitfn = 'cohstate_decay' #'exp_decay' cohstate_decay'
    I.fitfn = 'cohstate_decay' #'exp_decay' cohstate_decay'
    Q.fitfn = 'cohstate_decay' #'exp_decay' cohstate_decay'
    SINGLE_SHOT.fitfn = 'cohstate_decay' #'exp_decay' cohstate_decay'
    

    datasets = [I, Q, MAG, PHASE]

    ######################## INITIALIZE AND RUN EXPERIMENT #############################

    expt = CavityT1(FOLDER, modes, pulses, sweeps, datasets, **parameters)
    expt.run()
