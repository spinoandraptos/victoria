""" """

from tkinter import SINGLE
from config.experiment_config import FOLDER, N, I, Q, MAG, PHASE

from qcore import Experiment, qua, Sweep

from qm.qua import *

from qm import qua as qm_qua

class ALLXY(Experiment):
    """ALLXY"""

    ############################# DEFINE PRIMARY DATASETS ##############################
    # these Datasets form the "raw" experimental data and will be streamed by the OPX
    # they must be specified at experiment runtime

    primary_datasets = ["I", "Q"]

    ############################## DEFINE PRIMARY SWEEPS ###############################
    # these Sweeps are uniquely associated with the Experiment subclass
    # these Sweeps must be specified at experiment runtime

    primary_sweeps = ["gate_id"]

    ############################ DEFINE THE PULSE SEQUENCE #############################
    # ensure that you import 'qua' from 'qcore' and not from 'qm' library
    # attributes accessed via 'self' must be defined in 'if __name__ == "__main__"' code

    def __init__(self, folder, modes, pulses, sweeps, datasets, **parameters):
       
        super().__init__(
            folder,
            modes,
            pulses,
            sweeps,
            datasets,
            **parameters,
        )  # Passes other parameters to parent
    
        
        self._gate_list = [
            ("idle", 0.00, "idle", 0.00, "IdId"),
            (self.qubit_pi_op, 0.00, self.qubit_pi_op, 0.00, "XpXp"),
            (self.qubit_pi_op, 0.25, self.qubit_pi_op, 0.25, "YpYp"),
            (self.qubit_pi_op, 0.00, self.qubit_pi_op, 0.25, "XpYp"),
            (self.qubit_pi_op, 0.25, self.qubit_pi_op, 0.00, "YpXp"),
            (self.qubit_pi2_op, 0.00, "idle", 0.00, "X9Id"),
            (self.qubit_pi2_op, 0.25, "idle", 0.00, "Y9Id"),
            (self.qubit_pi2_op, 0.00, self.qubit_pi2_op, 0.25, "X9Y9"),
            (self.qubit_pi2_op, 0.25, self.qubit_pi2_op, 0.00, "Y9X9"),
            (self.qubit_pi2_op, 0.00, self.qubit_pi_op, 0.25, "X9Yp"),
            (self.qubit_pi2_op, 0.25, self.qubit_pi_op, 0.00, "Y9Xp"),
            (self.qubit_pi_op, 0.00, self.qubit_pi2_op, 0.25, "XpY9"),
            (self.qubit_pi_op, 0.25, self.qubit_pi2_op, 0.00, "YpX9"),
            (self.qubit_pi2_op, 0.00, self.qubit_pi_op, 0.00, "X9Xp"),
            (self.qubit_pi_op, 0.00, self.qubit_pi2_op, 0.00, "XpX9"),
            (self.qubit_pi2_op, 0.25, self.qubit_pi_op, 0.25, "Y9Yp"),
            (self.qubit_pi_op, 0.25, self.qubit_pi2_op, 0.25, "YpY9"),
            (self.qubit_pi_op, 0.00, "idle", 0.00, "XpId"),
            (self.qubit_pi_op, 0.25, "idle", 0.00, "YpId"),
            (self.qubit_pi2_op, 0.00, self.qubit_pi2_op, 0.00, "X9X9"),
            (self.qubit_pi2_op, 0.25, self.qubit_pi2_op, 0.25, "Y9Y9"),
        ]

    def sequence(self):
        """QUA sequence that defines this Experiment subclass"""
        # qua.initialize_qubit(self.resonator,
        #                     self.readout_pulse,
        #                     demod_type="dual",
        #                     threshold_g=self.readout_pulse.threshold,
        #                     wait_time=self.initialize_wait_time,
        #                     n_consecutive=5)
        with switch_(self.gate_id):
            for i in range(len(self._gate_list)):
                with case_(i):
                    
                    gate1_rot, gate1_axis, gate2_rot, gate2_axis, _ = self._gate_list[i]

                    # qua.reset_frame(self.qubit.name)
                    # Play the first gate
                    if gate1_rot != "idle":
                        self.qubit.play(gate1_rot, phase=gate1_axis)
                    # Play the second gate
                    if gate2_rot != "idle":
                        self.qubit.play(gate2_rot, phase=gate2_axis)
                    
                    qua.align()
                    # self.qubit_ef.play(self.qubit_ef_pi_pulse)
                    # qua.align()
                    # qua.align(self.qubit_ef, self.resonator)
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
        "qubit_pi_op": "qubit_gaussian_pi_24",
        "qubit_pi2_op": "qubit_gaussian_pi2_24",
       
        "readout_pulse": "rr_readout_pulse",
    }

    ############################## CONTROL PARAMETERS ##################################

    parameters = {
        "wait_time": 400_000,
        "initialize_wait_time": 5000,
        "ro_ampx": 1,
        "plot_single_shot":False
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this Experiment run
    N.num = 100000

    GATES = Sweep(name="gate_id", start=0, stop=20, num=21, dtype=int, save=True)

    # set the qubit amplitude sweep for this Experiment run
    # QD_AMPX = Sweep(name="qubit_pulse_amplitude", start=-1.2, stop=1.2, num=401)
    sweeps = [N, GATES]

    ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass
    Q.plot = True
    MAG.plot = True
    PHASE.plot = True
    I.plot = True
    
    

    # PHASE.datafn_args = {"delay": 2.792e-7, "freq": RR.int_freq}
    # PHASE.plot = False
    datasets = [I, Q, MAG, PHASE]

    ######################## INITIALIZE AND RUN EXPERIMENT #############################

    expt = ALLXY(FOLDER, modes, pulses, sweeps, datasets, **parameters)
    expt.run()