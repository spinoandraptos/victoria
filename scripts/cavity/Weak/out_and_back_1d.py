""" """

from config.experiment_config import FOLDER, N, FREQ, I, Q, MAG, PHASE, RR

from qcore import Experiment, qua, Sweep
from qcore.libs.qua_macros import QuaVariable
from qm import qua as qm_qua


class OUTANDBACK_1d(Experiment):
    """Cavity spectroscopy"""

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
        qua.reset_phase(self.cavity)
        qua.reset_frame(self.cavity)

        if self.qubit_in_e:
            self.qubit.play(self.qubit_pi)

        qua.wait(int(130), self.cavity)
        self.cavity.play(
            self.cavity_pulse, ampx=self.cav_ampx, phase=0.0
        )  # create a coherent state
        # qua.wait(int(130), self.cavity)
        qua.align()
        # # qua.update_frequency(self.cavity, -50e6 -15.29e3,keep_phase=True)
        qua.wait(self.time_delay, self.cavity)  # wait for state to rotate
        # qua.wait(int(16), self.cavity)  # wait for state to rotate
        # # qua.update_frequency(self.cavity, -50e6 - 9.362e3, keep_phase=True)
        
        self.cavity.play(self.cavity_pulse, ampx=self.cav_ampx, phase=self.disp_phase)
        # )  # displace cavity back

        qua.align()
        self.qubit.play(self.qubit_pi_selective)  # flip qubit if cav is in vac.

        qua.align()

        self.resonator.measure(self.readout_pulse, (self.I, self.Q), ampx=self.ro_ampx)
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
        "cavity_pulse": "cav_gaussian_long",
        "qubit_pi_selective": "qubit_gaussian_pi_pulse_200",
        "qubit_pi": "qubit_gaussian_pi_pulse",
        "readout_pulse": "rr_readout_pulse",
    }

    ############################## CONTROL PARAMETERS ##################################

    parameters = {
        "wait_time": 500000,
        "ro_ampx": 1,
        "fetch_interval": 5,
        "qubit_in_e": True,
        "cav_ampx": 1,
        "phase": QuaVariable(
            value=0.0,
            dtype=qm_qua.fixed,
            tag="phase",
            buffer=True,
            stream=True,
        ),
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this Experiment run
    N.num = 200000

    # set the delay sweep
    DEL = Sweep(name="time_delay", points=[16, 216], dtype=int)

    DISPL_PHASE = Sweep(name="disp_phase", start=0.1, stop=0.7, step=0.01, dtype=float)

    sweeps = [N,DEL, DISPL_PHASE]

    # sweeps = [N, FREQ]

    ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass
    # MAG.fitfn = "gaussian"

    PHASE.datafn_args = {"delay": 2.792e-7, "freq": RR.int_freq}

    Q.plot = False
    PHASE.plot = False
    MAG.plot = False

    I.fitfn = "gaussian"
    Q.fitfn = "gaussian"
    MAG.fitfn = "gaussian"
    PHASE.fitfn = "gaussian"
    datasets = [I, Q, MAG, PHASE]
    I.plot = True
    Q.plot = True
    MAG.plot = True
    PHASE.plot = True
    # SINGLE_SHOT.plot = False
    # MAG.plot_args["plot_type"] = "image"
    # I.plot_args["plot_type"] = "image"
    # SINGLE_SHOT.plot_args["plot_type"] = "image"

    ######################## INITIALIZE AND RUN EXPERIMENT #############################

    expt = OUTANDBACK_1d(FOLDER, modes, pulses, sweeps, datasets, **parameters)
    expt.run()
