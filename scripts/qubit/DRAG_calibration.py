""" """

from config.experiment_config import FOLDER, N, FREQ, I, Q, MAG, PHASE, RR

from qcore import Experiment, qua, Sweep
from qcore.helpers import Stage
from qm import qua as qm_qua

from config.experiment_config import MODES_CONFIG

class drag(Experiment):
    """Qubit spectroscopy"""

    ############################# DEFINE PRIMARY DATASETS ##############################
    # these Datasets form the "raw" experimental data and will be streamed by the OPX
    # they must be specified at experiment runtime

    primary_datasets = ["I", "Q"]

    ############################## DEFINE PRIMARY SWEEPS ###############################
    # these Sweeps are uniquely associated with the Experiment subclass
    # these Sweeps must be specified at experiment runtime

    primary_sweeps = ["drag"]

    ############################ DEFINE THE PULSE SEQUENCE #############################
    # ensure that you import 'qua' from 'qcore' and not from 'qm' library
    # attributes accessed via 'self' must be defined in 'if __name__ == "__main__"' code

    def __init__(self, folder, modes, pulses, sweeps, datasets, **parameters):

        super().__init__(
            folder, modes, pulses, sweeps, datasets, **parameters
        )  # Passes other parameters to parent

        self._gate_list = [
            (self.qubit_pi_op, 0.00, self.qubit_pi2_op, 0.25, "XpY9"),
            (self.qubit_pi_op, 0.25, self.qubit_pi2_op, 0.00, "YpX9"),
        ]
        

    def sequence(self):
        """QUA sequence that defines this Experiment subclass"""

        with qm_qua.switch_(self.gate):
            for i in range(len(self._gate_list)):
                with qm_qua.case_(i):
                    # qua.update_frequency(self.qubit, self.qubit.int_freq)
                    qua.align()
                    gate1_rot, gate1_axis, gate2_rot, gate2_axis, _ = self._gate_list[i]
                    qua.reset_frame(self.qubit)

                    # self.flux.play(self.flux_drive, ampx=self.flux_ampx)
                    # qua.wait(self.flux_delay, self.qubit)

                    # Play the first gate
                    if gate1_rot != "idle":
                        self.qubit.play(
                            gate1_rot, phase=gate1_axis, ampx=(1.0, 0.0, 0.0, self.drag)
                        )
                    # Play the second gate
                    if gate2_rot != "idle":
                        self.qubit.play(
                            gate2_rot, phase=gate2_axis, ampx=(1.0, 0.0, 0.0, self.drag)
                        )

                    # qua.update_frequency(self.qubit, self.qubit_ef_freq)
                    # self.qubit.play(self.qubit_ef_drive)

                    qua.align(self.qubit, self.resonator)
                    self.resonator.measure(
                    self.readout_pulse, (self.I, self.Q), ampx=self.ro_ampx, demod_type="dual"
        )   

                    qua.align()
                    qua.wait(self.wait_time)
                    qua.align()


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
        "qubit_pi_op": "qubit_gaussian_pi_24",
        "qubit_pi2_op": "qubit_gaussian_pi2_24",
        "readout_pulse": "rr_readout_pulse",
    }

    ############################## CONTROL PARAMETERS ##################################

    parameters = {
        "wait_time": 100_000,
        "ro_ampx": 1,
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this Experiment run
    N.num = 100_000

    # set the qubit amplitude sweep for this Experiment run
    GATES = Sweep(name="gate", start=0, stop=1, step=1, dtype=int)
    # PHA2 = Sweep(name="phase2", start=-0.0, stop=0.25, step=0.25)
    # DRAG = Sweep(name="drag", start=-0.5, stop=0, num=50)
    DRAG = Sweep(name="drag", start=-1, stop=1, num=50)

    sweeps = [N, GATES, DRAG]

    ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass

    PHASE.datafn_args = {"delay": 2.792e-7, "freq": RR.int_freq}
    PHASE.plot = True

    # I.fitfn = "linear"
    # Q.fitfn = "linear"

    datasets = [I, Q, MAG, PHASE]

    ######################## INITIALIZE AND RUN EXPERIMENT #############################

    expt = drag(FOLDER, modes, pulses, sweeps, datasets, **parameters)
    expt.run(simulate=False)
