import sys
# The directory containing the 'config' folder
FOLDER = "C:/Users/qcrew/Documents/eunice/"

# Add the FOLDER itself to sys.path, not the file path
if FOLDER not in sys.path:
    sys.path.insert(0, FOLDER)

from config.experiment_config import FOLDER, N, FREQ, I, Q, MAG, PHASE

from qcore import Experiment, qua, Sweep

class RRSpec_crosskerr(Experiment):
    """Readout resonator spectroscopy"""

    ############################# DEFINE PRIMARY DATASETS ##############################
    # these Datasets form the "raw" experimental data and will be streamed by the OPX
    # they must be specified at experiment runtime

    primary_datasets = ["I", "Q"]

    ############################## DEFINE PRIMARY SWEEPS ###############################
    # these Sweeps are uniquely associated with the Experiment subclass
    # these Sweeps must be specified at experiment runtime

    primary_sweeps = ["resonator_frequency"]

    ############################ DEFINE THE PULSE SEQUENCE #############################
    # ensure that you import 'qua' from 'qcore' and not from 'qm' library
    # attributes accessed via 'self' must be defined in 'if __name__ == "__main__"' code

    def sequence(self):
        """QUA sequence that defines this Experiment subclass"""
        #qua.reset_phase(self.resonator)
        qua.update_frequency(self.resonator, self.resonator_frequency)
        self.cavity.play(self.cav_displacement, ampx=self.cav_ampx)  # create a coherent state
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

    modes = {"resonator": "rr", "cavity": "cavity"}

    ################################### PULSE MAP ######################################
    # key: name of the Pulse as defined by the Experiment subclass
    # value: name of the Pulse as defined by the user in modes.yml

    pulses = {"readout_pulse": "rr_readout_pulse", "cav_displacement": "cav_constant_64",}

    ############################## CONTROL PARAMETERS ##################################

    parameters = {
        "wait_time": 800_000,
        "ro_ampx": 1,
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    ################################### 1D SWEEP #######################################

    # set number of repetitions for this Experiment run
    N.num = 100_000
 
    # set the qubit frequency sweep for this Experiment run
    FREQ.name = "resonator_frequency"
    FREQ.start = -55e6
    FREQ.stop = -45e6
    FREQ.num = 101

    ################################### 2D SWEEP #######################################
    # set the delay sweep
    CAV_AMP = Sweep(name="cav_ampx", start=0, stop=0.2, step=0.2)
    sweeps = [N, CAV_AMP, FREQ]
    # sweeps = [N, FREQ]

    ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass

    PHASE.inputs = ("I", "Q", "resonator_frequency")
    PHASE.datafn_args = {"delay": -3.298e-7}

    MAG.fitfn = "lorentzian"
    # MAG.axes = sweeps

    I.plot = True
    Q.plot = True
    PHASE.plot = True

    datasets = [I, Q, MAG, PHASE]

    ######################## INITIALIZE AND RUN EXPERIMENT #############################

    # expt = RRSpec(FOLDER, modes, pulses, sweeps, datasets, current_value=1.23e-3, **parameters)
    expt = RRSpec_crosskerr(FOLDER, modes, pulses, sweeps, datasets, **parameters)
    expt.run()
