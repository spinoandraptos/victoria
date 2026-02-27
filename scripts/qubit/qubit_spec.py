import sys
# The directory containing the 'config' folder
FOLDER = "C:/Users/qcrew/Documents/eunice/"

# Add the FOLDER itself to sys.path, not the file path
if FOLDER not in sys.path:
    sys.path.insert(0, FOLDER)

from config.experiment_config import FOLDER, N, FREQ, I, Q, MAG, PHASE, RR

from qcore import Experiment, qua, Sweep
import numpy as np

class QubitSpec(Experiment):
    """Qubit spectroscopy"""

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
        qua.reset_phase(self.resonator)
        qua.update_frequency(self.qubit, self.qubit_frequency)
        #qua.update_frequency(self.resonator, self.resonator_frequency)
        self.qubit.play(self.qubit_drive)#, ampx=self.qubit_drive_ampx)
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
        "qubit": "qubit",
        "resonator": "rr",
    }

    ################################### PULSE MAP ######################################
    # key: name of the Pulse as defined by the Experiment subclass
    # value: name of the Pulse as defined by the user in modes.yml

    pulses = {
        "qubit_drive": "qubit_constant_pi_1500",#"qubit_constant_pulse",#"qubit_constant_pi_1500",
        "readout_pulse": "rr_readout_pulse",
    }

    ############################## CONTROL PARAMETERS ##################################

    parameters = {
        "wait_time": 10000,
        "ro_ampx": 1.0,
        "qubit_drive_ampx": 1,
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this E xperiment run
    N.num = 50000

    # set the qubit frequency sweep for this Experiment run
    FREQ.name = "qubit_frequency"
    FREQ.start = -200e6  # 40e6
    FREQ.stop = 200e6  # 60e6 #the 60e6 is from the lo used to generate ef pulse
    FREQ.num = 201
    

    sweeps = [N, FREQ]

    ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass

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
    expt = QubitSpec(FOLDER, modes, pulses, sweeps, datasets, **parameters)
    expt.run(simulate=False)
