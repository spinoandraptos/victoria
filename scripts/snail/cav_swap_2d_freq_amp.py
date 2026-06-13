""" """
import sys
from datetime import datetime


    
from config.experiment_config import FOLDER, N, I, Q, MAG, PHASE, RR, FREQ
from qcore import Experiment, qua, Sweep


class CavitySWAP2D_freq_amp(Experiment):
    """Cavity T1"""

    ############################# DEFINE PRIMARY DATASETS ##############################
    # these Datasets form the "raw" experimental data and will be streamed by the OPX
    # they must be specified at experiment runtime

    primary_datasets = ["I", "Q"]

    ############################## DEFINE PRIMARY SWEEPS ###############################
    # these Sweeps are uniquely associated with the Experiment subclass
    # these Sweeps must be specified at experiment runtime

    primary_sweeps = ["snail_frequency"]

    ############################ DEFINE THE PULSE SEQUENCE #############################
    # ensure that you import 'qua' from 'qcore' and not from 'qm' library
    # attributes accessed via 'self' must be defined in 'if __name__ == "__main__"' code

    def sequence(self):
        """QUA sequence that defines this Experiment subclass"""
        qua.reset_phase(self.cavity)
        qua.reset_frame(self.cavity)
        qua.reset_phase(self.snail)
        qua.reset_frame(self.snail)
        qua.align()
        self.cavity.play(self.cavity_drive)
        qua.align(self.cavity, self.snail)
        qua.update_frequency(self.snail, self.snail_frequency)
        self.snail.play(self.snail_pulse, ampx= self.snail_ampx) #
        # qua.wait(self.time_delay, self.cavity)
        qua.align(self.snail, self.qubit)
        self.qubit.play(self.qubit_pulse)
        qua.align(self.qubit, self.resonator)
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
        "cavity": "cavity",
        "qubit": "qubit",
        "resonator": "rr",
        "snail": "drive",
    }

    ################################### PULSE MAP ######################################
    # key: name of the Pulse as defined by the Experiment subclass
    # value: name of the Pulse as defined by the user in modes.yml

    pulses = {
        "cavity_drive": "cav_constant_64",
        "qubit_pulse": "qubit_gaussian_pi_1200",
        "readout_pulse": "rr_readout_pulse",
        "snail_pulse": "drive_constant_2000",
    }

    ############################## CONTROL PARAMETERS ##################################

    parameters = {
        "wait_time": 1_000_000,
        "ro_ampx": 1,
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this Experiment run
    N.num = 50000

    # set the qubit frequency sweep for this Experiment run

    # DEL = Sweep(name="time_delay", start=16, stop=1200000, step=8000, dtype=int)
        # set the qubit frequency sweep for this Experiment run
    FREQ.name = "snail_frequency"
    FREQ.start =0e6
    FREQ.stop = 15e6
    FREQ.num = 51
    # DEL = Sweep(name="length_snail", start=4, stop=120, step=4, dtype=int)
    SNAIL_AMPX = Sweep(name="snail_ampx", start=-1.3, stop=1.3, num=31)
    sweeps = [N, FREQ, SNAIL_AMPX]
    # QD_AMPX = Sweep(name="snail_frequency", points=[0.0, 1.0])

    PHASE.plot = False
    # MAG.plot = False
    # Q.plot = False
    I.plot = False
  
    # SINGLE_SHOT.plot_args["plot_type"] = "image"

    # MAG.axes = sweeps[1:]
    # PHASE.axes = sweeps[1:]
    PHASE.datafn_args = {"delay": 2.792e-7, "freq": RR.int_freq}
    # PHASE.plot = False
    datasets = [I, Q, MAG, PHASE]
    Q.plot_args["plot_type"] = "image"
    MAG.plot_args["plot_type"] = "image"

    ######################## INITIALIZE AND RUN EXPERIMENT #############################

    expt = CavitySWAP2D_freq_amp(FOLDER, modes, pulses, sweeps, datasets, **parameters)
    expt.run()