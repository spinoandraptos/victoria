""" """
import sys
from config.experiment_config import FOLDER, N, FREQ, I, Q, MAG, PHASE, RR, SINGLE_SHOT
from qm import qua as qm_qua
from qcore import Experiment, qua, Sweep


class Rabi(Experiment):
    """Power Rabi"""

    ############################# DEFINE PRIMARY DATASETS ##############################
    # these Datasets form the "raw" experimental data and will be streamed by the OPX
    # they must be specified at experiment runtime

    primary_datasets = ["I", "Q"]

    ############################## DEFINE PRIMARY SWEEPS ###############################
    # these Sweeps are uniquely associated with the Experiment subclass
    # these Sweeps must be specified at experiment runtime

    primary_sweeps = ["qubit_pulse_amplitude"]

    ############################ DEFINE THE PULSE SEQUENCE #############################
    # ensure that you import 'qua' from 'qcore' and not from 'qm' library
    # attributes accessed via 'self' must be defined in 'if __name__ == "__main__"' code

    def sequence(self):
        qua.reset_phase(self.qubit)
        qua.reset_frame(self.qubit)
        # qua.initialize_qubit(self.resonator,
        #                     self.readout_pulse,
        #                     demod_type="dual",
        #                     threshold_g=self.readout_pulse.threshold,
        #                     wait_time=self.initialize_wait_time,
        #                     n_consecutive=15)
        # qua.align()
        # qua.reset_phase(self.qubit)
        # qua.reset_frame(self.qubit)
        # qua.align()
        """QUA sequence that defines this Experiment subclass"""
        self.qubit.play(self.qubit_drive, ampx=self.qubit_pulse_amplitude)
        # self.qubit.play(self.qubit_drive, ampx=self.qubit_pulse_amplitude)
        qua.align(self.qubit, self.qubit_ef)
        
        self.qubit_ef.play(self.qubit_ef_drive, ampx=self.qubit_pulse_amplitude)
        # self.qubit.play(self.qubit_drive, ampx=self.qubit_pulse_amplitude)
     
        qua.align(self.qubit_ef, self.resonator)

        # qua.align(self.qubit, self.resonator)
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
        "qubit_ef": "qubit_EF",
        "qubit": "qubit",
        "resonator": "rr",
    }

    ################################### PULSE MAP ######################################
    # key: name of the Pulse as defined by the Experiment subclass
    # value: name of the Pulse as defined by the user in modes.yml

    pulses = {
        "qubit_drive": "qubit_constant_pi_300",
        "qubit_ef_drive": "qubitEF_constant_pi_16",
        "readout_pulse": "rr_readout_pulse",
    }

    ############################## CONTROL PARAMETERS ##################################

    parameters = {
        "wait_time":8000,
        # "initialize_wait_time": 5000,
        "ro_ampx": 1,
        "plot_single_shot": False,
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this Experiment run
    N.num = 100_000

    # set the qubit amplitude sweep for this Experiment run
    QD_AMPX = Sweep(name="qubit_pulse_amplitude", start=-1.5, stop=1.5, num=31)
    sweeps = [N, QD_AMPX]

    ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass
    I.fitfn, Q.fitfn, MAG.fitfn, SINGLE_SHOT.fitfn = (
        "sine",
        "sine",
        "sine",
        "sine",
        # "sine_gf",
        # "sine_gf",
        # "sine_gf",
    )

    PHASE.datafn_args = {"delay": -3.298e-7, "freq": RR.int_freq}
    MAG.plot = True
    PHASE.plot = True
    I.plot = True
    Q.plot = True
    SINGLE_SHOT.plot = False
    datasets = [I, Q, MAG, PHASE]

    ######################## INITIALIZE AND RUN EXPERIMENT #############################

    expt = Rabi(FOLDER, modes, pulses, sweeps, datasets, **parameters)
    # expt.run(simulate=True)
    expt.run()
