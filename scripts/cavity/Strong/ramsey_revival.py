""" """

import sys

# sys.path.append("C:/Users/admin/Desktop/qcore-yabba/yabba-main/")
from config.experiment_config import FOLDER, N, FREQ, I, Q, MAG, PHASE, RR, SINGLE_SHOT
from qcore import Experiment, qua, Sweep
from qcore import Dataset
from qm import qua as qm_qua

class RamseyRevival(Experiment):
    """Ramsey revival"""

    ############################# DEFINE PRIMARY DATASETS ##############################
    # these Datasets form the "raw" experimental data and will be streamed by the OPX
    # they must be specified at experiment runtime
    primary_datasets = ["I", "Q"]

    ############################## DEFINE PRIMARY SWEEPS ###############################
    # these Sweeps are uniquely associated with the Experiment subclass
    # these Sweeps must be specified at experiment runtime
    primary_sweeps = ["delay"]

    ############################ DEFINE THE PULSE SEQUENCE #############################
    # ensure that you import 'qua' from 'qcore' and not from 'qm' library
    # attributes accessed via 'self' must be defined in 'if __name__ == "__main__"' code

    def sequence(self):
        """QUA sequence that defines this Experiment subclass"""
        qua.reset_phase()

        self.cavity.play(self.cavity_pulse, ampx = self.cavity_ampx)
        # self.cavity.play(self.cavity_pulse, ampx = self.cavity_ampx)
        # self.cavity.play(self.cavity_pulse, ampx = self.cavity_ampx)
        qua.align(self.cavity,self.qubit)


        self.qubit.play(self.qubit_pulse) # pi/2
        qua.wait(self.delay, self.qubit)  # wait
        self.qubit.play(self.qubit_pulse) # pi/2
        qua.align()

        # self.qubitEF.play(self.qubitEF_drive)
        # qua.align(self.qubitEF, self.resonator)

        self.resonator.measure(self.readout_pulse, (self.I, self.Q), ampx=self.ro_ampx,  demod_type="dual")

        qua.wait(self.wait_time, self.resonator)

        if self.plot_single_shot:  # assign state to G or E
            qm_qua.assign(self.single_shot,qm_qua.Cast.to_fixed(self.I > self.readout_pulse.threshold),)
        

if __name__ == "__main__":
    """ """

    #################################### MODE MAP ######################################
    # key: name of the Mode as defined by the Experiment subclass
    # value: name of the Mode as defined by the user in modes.yml

    modes = {
        # "qubitAGF": "qA",
        # "driveA": "driveA",
        "cavity": "cavity",
        "qubit": "qubit",
        # "qubitEF":'qubit_EF',
        "resonator": "rr",
    }

    ################################### PULSE MAP ######################################
    # key: name of the Pulse as defined by the Experiment subclass
    # value: name of the Pulse as defined by the user in modes.yml

    pulses = {
        # "qubitA_drive": "qubitAGF_gaussian_pi_pulse",
        # "driveA_pulse": "driveA_constant_ramp_pulse_short",
        "cavity_pulse": "cav_constant_200",
        "qubit_pulse": "qubit_gaussian_pi2_pulse_24",
        # "qubitEF_drive": "qubitEF_constant_pi_16",
        "readout_pulse": "rr_readout_pulse",
    }

    ############################## CONTROL PARAMETERS ##################################

    parameters = {
        "wait_time": 600_000,
        "ro_ampx": 1,
        # "cavity_ampx": 1,
        "fetch_interval": 1,
        "plot_single_shot": False,
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this Experiment run
    N.num = 10000

    # set the qubit frequency sweep for this Experiment run
    DELAY = Sweep(
        name="delay",
        dtype=int,
        start=4,
        stop=6000,
        step=60,
    )
    
    CAVITY_AMPX = Sweep(name="cavity_ampx", points=[0.5, 0.7])


    sweeps = [N, CAVITY_AMPX ,DELAY]

    ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass
    # MAG.fitfn = "gaussian"

    PHASE.datafn_args = {"delay": 2.792e-7, "freq": RR.int_freq}
    MAG.plot = True
    I.plot = True
    Q.plot = True
    PHASE.plot = True,
    I.fitfn = "gaussian"
    Q.fitfn = "gaussian"
    PHASE.fitfn = "gaussian"
    MAG.fitfn = "gaussian"
    datasets = [I, Q, MAG, PHASE]

    ######################## INITIALIZE AND RUN EXPERIMENT #############################

    expt = RamseyRevival(FOLDER, modes, pulses, sweeps, datasets, **parameters)
    expt.run(simulate = False)
