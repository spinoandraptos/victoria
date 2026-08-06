""" """
import sys
from config.experiment_config import FOLDER, N, FREQ, I, Q, MAG, PHASE, RR, SINGLE_SHOT
from qm import qua as qm_qua
from qcore import Experiment, qua, Sweep


class RabiGF2(Experiment):
    """Power Rabi"""

    ############################# DEFINE PRIMARY DATASETS ##############################
    # these Datasets form the "raw" experimental data and will be streamed by the OPX
    # they must be specified at experiment runtime

    primary_datasets = ["I", "Q"]

    ############################## DEFINE PRIMARY SWEEPS ###############################
    # these Sweeps are uniquely associated with the Experiment subclass
    # these Sweeps must be specified at experiment runtime

    primary_sweeps = ["drive_frequency"]

    ############################ DEFINE THE PULSE SEQUENCE #############################
    # ensure that you import 'qua' from 'qcore' and not from 'qm' library
    # attributes accessed via 'self' must be defined in 'if __name__ == "__main__"' code


    def sequence(self):
        """QUA sequence that defines this Experiment subclass"""
        # qua.reset_phase(self.qubit_gf2)
        # qua.reset_frame(self.qubit_gf2)
        # qua.update_frequency(self.qubit, self.qubit_frequency)
        qua.align()
        
        self.qubit_gf2.play(self.qubit_gf2_drive, ampx=1.0)
        # qua.wait(46,self.drive)
        qua.update_frequency(self.drive, self.drive_frequency)
        # self.qubit_ef.play(self.qubit_ef_drive) 
        qua.align(self.qubit_gf2, self.drive)
        
        # self.drive.play(self.stark_drive, ampx=self.d_ampx) # fixed freq #, ampx=2.0 max , duration=self.length_drive
        self.drive.play(self.fock_drive)
        # self.snail.play(self.snail_pulse, duration=self.length_snail, ampx= self.snail_ampx)
        # qua.align(self.qubit_gf2, self.drive)
        # qua.wait(56,self.qubit_gf2)
        # self.qubit_gf2.play(self.qubit_gf2_drive)
        
        qua.align(self.drive, self.resonator)
        # qua.wait(124,self.resonator)

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
        "drive": "fock_drive",
        "qubit_gf2": "qubit_GF2",
        "resonator": "rr",
    }

    ################################### PULSE MAP ######################################
    # key: name of the Pulse as defined by the Experiment subclass
    # value: name of the Pulse as defined by the user in modes.yml

    pulses = {
           "fock_drive": "drive_constant_56",
           "qubit_gf2_drive": "qubitGF2_constant_pi_200",
           "readout_pulse": "rr_readout_pulse",
    }

    ############################## CONTROL PARAMETERS ##################################

    parameters = {
        "wait_time":20_000,
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
    FREQ.name = "drive_frequency"
    FREQ.start = -200e6  # 40e6
    FREQ.stop = 200e6  # 60e6 #the 60e6 is from the lo used to generate ef pulse
    FREQ.num = 201
    sweeps = [N, FREQ]

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

    expt = RabiGF2(FOLDER, modes, pulses, sweeps, datasets, **parameters)
    # expt.run(simulate=True)
    expt.run()
