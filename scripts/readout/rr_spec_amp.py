""" """
import sys

from config.experiment_config import FOLDER, N, FREQ, I, Q, MAG, PHASE

from qcore import Experiment, qua, Sweep


class RRSpecAmp(Experiment):
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
        self.resonator.measure(
            self.readout_pulse, (self.I, self.Q), ampx=self.ro_ampx, demod_type="dual"
        )
        qua.wait(self.wait_time, self.resonator)


if __name__ == "__main__":
    """ """

    #################################### MODE MAP ######################################
    # key: name of the Mode as defined by the Experiment subclass
    # value: name of the Mode as defined by the user in modes.yml

    modes = {"resonator": "rr"}

    ################################### PULSE MAP ######################################
    # key: name of the Pulse as defined by the Experiment subclass
    # value: name of the Pulse as defined by the user in modes.yml

    pulses = {"readout_pulse": "rr_longer_readout_pulse"}

    ############################## CONTROL PARAMETERS ##################################

    parameters = {
        "wait_time": 20_000,
        # "ro_ampx": 1,
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    ################################### 1D SWEEP #######################################

    # set number of repetitions for this Experiment run
    N.num = 100_000
 
    # set the qubit frequency sweep for this Experiment run
    FREQ.name = "resonator_frequency"
    FREQ.start = -51e6
    FREQ.stop = -45e6
    FREQ.num = 201#101

    ################################### 2D SWEEP #######################################

    RO_AMPX = Sweep(
        name="ro_ampx",
        # points=[0.05,0.1,0.5, 0.6, 0.7, 0.8, 0.9, 1]
        # points=[0.1, 0.2, 0.3, 0.5, 1, 1.5]#0.25,0.5,0.75] #[0.01,0.05, 0.08,0.1, 0.2, 0.3, 0.4]
        # points=[0.01, 0.2, 0.5, 0.8, 1.0, 1.2]
        points=[0.005, 0.01, 0.02, 0.05, 0.08, 0.1, 0.2, .3, 0.4,0.5]#0.25,0.5,0.75]
    ) 
    sweeps = [N, RO_AMPX, FREQ]
    # sweeps = [N, FREQ]

    ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass

    PHASE.inputs = ("I", "Q", "resonator_frequency")
    PHASE.datafn_args = {"delay": -3.72e-7}#-3.298e-7

    # MAG.fitfn = "lorentzian"
    # MAG.axes = sweeps

    I.plot = True
    Q.plot = True
    PHASE.plot = True

    datasets = [I, Q, MAG, PHASE]

    ######################## INITIALIZE AND RUN EXPERIMENT #############################

    # expt = RRSpec(FOLDER, modes, pulses, sweeps, datasets, current_value=1.23e-3, **parameters)
    expt = RRSpecAmp(FOLDER, modes, pulses, sweeps, datasets, **parameters)
    expt.run()
