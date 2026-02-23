""" """
import sys
# The directory containing the 'config' folder
FOLDER = "C:/Users/qcrew/Documents/eunice/"

# Add the FOLDER itself to sys.path, not the file path
if FOLDER not in sys.path:
    sys.path.insert(0, FOLDER)


from config.experiment_config import FOLDER, N, FREQ, I, Q, MAG, PHASE, RR

from qcore import Experiment, qua, Sweep


class RabiEF(Experiment):
    """Power Rabi EF"""

    ############################# DEFINE PRIMARY DATASETS ##############################
    # these Datasets form the "raw" experimental data and will be streamed by the OPX
    # they must be specified at experiment runtime

    primary_datasets = ["I", "Q"]

    ############################## DEFINE PRIMARY SWEEPS ###############################
    # these Sweeps are uniquely associated with the Experiment subclass
    # these Sweeps must be specified at experiment runtime

    primary_sweeps = ["qubit_ef_pulse_amplitude"]

    ############################ DEFINE THE PULSE SEQUENCE #############################
    # ensure that you import 'qua' from 'qcore' and not from 'qm' library
    # attributes accessed via 'self' must be defined in 'if __name__ == "__main__"' code

    def sequence(self):
        """QUA sequence that defines this Experiment subclass"""

        self.qubit.play(self.qubit_pi_pulse)
        qua.align(self.qubit, self.qubit_ef)
        self.qubit_ef.play(self.qubit_ef_drive, ampx=self.qubit_ef_pulse_amplitude)
        qua.align(self.qubit_ef, self.qubit)
        self.qubit.play(self.qubit_pi_pulse)
        qua.align(self.qubit, self.resonator)
        self.resonator.measure(self.readout_pulse, (self.I, self.Q), ampx=self.ro_ampx, demod_type="dual")
        qua.wait(self.wait_time, self.resonator)


if __name__ == "__main__":
    """ """

    #################################### MODE MAP ######################################
    # key: name of the Mode as defined by the Experiment subclass
    # value: name of the Mode as defined by the user in modes.yml

    modes = {
        "qubit": "qubit",
        "qubit_ef": "qubit_ef",
        "resonator": "rr",
    }

    ################################### PULSE MAP ######################################
    # key: name of the Pulse as defined by the Experiment subclass
    # value: name of the Pulse as defined by the user in modes.yml

    pulses = {
        "qubit_pi_pulse": "qubit_constant_pi_52",
        "qubit_ef_drive": "qubit_ef_constant_pulse",
        "readout_pulse": "rr_readout_pulse",
    }
    
    
        ############################## CONTROL PARAMETERS ##################################

    parameters = {
        "wait_time":10000,
        "ro_ampx": 1,
        "plot_single_shot": False,
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this Experiment run
    N.num = 100_000

    # set the qubit amplitude sweep for this Experiment run
    QD_AMPX = Sweep(name="qubit_ef_pulse_amplitude", start=-1.8, stop=1.8, num=51)
    sweeps = [N, QD_AMPX]

    ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass
    I.fitfn, Q.fitfn, MAG.fitfn = (
        "sine",
        "sine",
        "sine",
        # "sine",
        # "sine_gf",
        # "sine_gf",
        # "sine_gf",
    )

    PHASE.datafn_args = {"delay": -3.298e-7, "freq": RR.int_freq}
    MAG.plot = True
    PHASE.plot = True
    I.plot = True
    Q.plot = True
    datasets = [I, Q, MAG, PHASE]

    ######################## INITIALIZE AND RUN EXPERIMENT #############################

    expt = RabiEF(FOLDER, modes, pulses, sweeps, datasets, **parameters)
    expt.run(simulate=True)
