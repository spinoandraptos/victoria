""" """

from config.experiment_config import (
    FOLDER,
    N,
    FREQ,
    I,
    Q,
    MAG,
    PHASE,
    RR,
    SINGLE_SHOT_PRE,
    SINGLE_SHOT_POST,
)

from qcore import Experiment, qua, Sweep
from qm import qua as qm_qua


class ECD_CAL_1D(Experiment):
    """Char_1D_singledisplacement"""

    ############################# DEFINE PRIMARY DATASETS ##############################
    # these Datasets form the "raw" experimental data and will be streamed by the OPX
    # they must be specified at experiment runtime

    primary_datasets = ["I", "Q", "single_shot_post"]

    ############################## DEFINE PRIMARY SWEEPS ###############################
    # these Sweeps are uniquely associated with the Experiment subclass
    # these Sweeps must be specified at experiment runtime

    primary_sweeps = ["cavity_amp"]

    ############################ DEFINE THE PULSE SEQUENCE #############################
    # ensure that you import 'qua' from 'qcore' and not from 'qm' library
    # attributes accessed via 'self' must be defined in 'if __name__ == "__main__"' code

    def sequence(self):
        """QUA sequence that defines this Experiment subclass"""

        # bring qubit into superposition
        qua.reset_phase(self.cavity)
        qua.reset_frame(self.cavity)
        qua.align()
        ###################### do a first measurement  #####################
        # self.resonator.measure(self.readout_pulse, (self.I, self.Q), ampx=self.ro_ampx)
        # if self.plot_single_shot:  # assign state to G or E
        #     qm_qua.assign(
        #         self.single_shot_pre,
        #         qm_qua.Cast.to_fixed(self.I > self.readout_pulse.threshold),
        #     )
        # qua.align()
        # qua.wait(int(10000), self.cavity, self.qubit)
        ######################  charactristic function  1D measurement #####################

        self.qubit.play(self.qubit_pi2)

        # start ECD gate
        qua.align()  # wait for qubit pulse to end
        # First positive displacement
        self.cavity.play(self.cav_disp, ampx=self.cavity_amp, phase=self.tomo_phase)

        qua.wait(int(self.delay), self.cavity)
        # First negative displacement
        self.cavity.play(self.cav_disp, ampx=-self.cavity_amp, phase=self.tomo_phase)

        qua.align()
        self.qubit.play(self.qubit_pi, phase=0.0)  # play pi to flip qubit around X
        qua.align()  # wait for qubit pulse to end

        # Second negative displacement
        self.cavity.play(self.cav_disp, ampx=-self.cavity_amp, phase=self.tomo_phase)

        qua.wait(int(self.delay), self.cavity)
        # Second positive displacement
        self.cavity.play(self.cav_disp, ampx=self.cavity_amp, phase=self.tomo_phase)
        qua.align()

        self.qubit.play(
            self.qubit_pi2,
            phase=self.correction_phase + (0 if self.measure_real else 0.25),
        )  # play pi/2 pulse around X or SY, to measure either the real or imaginary part of the characteristic function
        # qubit.play(qubit_pi2_pulse, phase=measure_real)  # 0 else 0.25  # play

        qua.align()
        self.resonator.measure(self.readout_pulse, (self.I, self.Q), ampx=self.ro_ampx)
        if self.plot_single_shot:  # assign state to G or E
            qm_qua.assign(
                self.single_shot_post,
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
        "cav_disp": "cav_const_112",  # "cav_gaussian_40",
        "qubit_pi2": "qubit_gaussian_pi2_4",
        "qubit_pi": "qubit_gaussian_pi_4",
        "readout_pulse": "rr_readout_pulse",
    }

    ############################## CONTROL PARAMETERS ##################################

    parameters = {
        "wait_time": 1500000,
        "ro_ampx": 1,
        "fetch_interval": 5,
        "tomo_phase": 0,
        "delay": 45,
        "correction_phase": 0,
        "measure_real": True,
        "plot_single_shot": True,
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this Experiment run
    N.num = 50000

    # set the qubit frequency sweep for this Experiment run
    CAV_AMPX = Sweep(name="cavity_amp", start=-1, stop=1, step=0.1)

    sweeps = [N, CAV_AMPX]

    ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass
    I.fitfn = "gaussian"
    Q.fitfn = "gaussian"
    SINGLE_SHOT_PRE.fitfn = "gaussian"
    SINGLE_SHOT_POST.fitfn = "gaussian"
    datasets = [I, Q, SINGLE_SHOT_POST]

    ######################## INITIALIZE AND RUN EXPERIMENT #############################

    expt = ECD_CAL_1D(FOLDER, modes, pulses, sweeps, datasets, **parameters)
    expt.run()
    # expt.run(simulate=True)
