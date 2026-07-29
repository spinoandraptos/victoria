""" """
""" """
import sys

from config.experiment_config import FOLDER, N, FREQ, I, Q, MAG, PHASE, SINGLE_SHOT, RR

from qcore import Experiment, qua, Sweep
from qm import qua as qm_qua
from qcore.helpers import Stage
from config.experiment_config import MODES_CONFIG
import numpy as np
import time


class snail_stark_shift_sweep(Experiment):

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
       
        # There are two cavity modes here, please check which mode is used.
        qua.update_frequency(self.drive, self.drive_frequency)        
        qua.update_frequency(self.snail, self.snail_frequency)        
        self.drive.play(self.stark_drive, ampx=self.drive_ampx) # fixed freq
        self.snail.play(self.snail_pulse, ampx = self.snail_ampx)
        qua.align(self.snail, self.qubit)
        self.qubit.play(self.qubit_pulse)
        qua.align(self.qubit, self.resonator)
        qua.align()
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
        "drive": "drive",
        "snail": "snail_drive",
        "qubit": "qubit",
        "resonator": "rr",
    }

    ################################### PULSE MAP ######################################
    # key: name of the Pulse as defined by the Experiment subclass
    # value: name of the Pulse as defined by the user in modes.yml

    pulses = {
        "snail_pulse": "snail_drive_constant_10000",
        "qubit_pulse": "qubit_gaussian_pi_2000",
        "stark_drive": "drive_constant_10000",
        "readout_pulse": "rr_readout_pulse",
    }

    ############################## CONTROL PARAMETERS ############# #####################

    parameters = {
        "wait_time": 100_000,
        "ro_ampx": 1,
        "snail_ampx": 1,
        "fetch_interval": 1,
        "plot_single_shot": False,
        "drive_frequency": 120e6
        
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this Experiment run
    N.num = 300

    # set the qubit frequency sweep for this Experiment run
    Q_AMPX = Sweep(
        name="drive_ampx",
        # points=[0.01, 0.05, 0.08, 0.1, 0.2, 0.3, 0.4, 0.5]#0.25,0.5,0.75]
        #points=[0.1, 0.2, 0.3, 0.4, 0.5]
        points=[0.0, 0.1, 0.2, 0.4, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.75, 2.0]#0.25,0.5,0.75]
    ) 
    
    FREQ.name = "snail_frequency"
    FREQ.start =-40e7
    FREQ.stop =20e7
    FREQ.num = 501
    
    sweeps = [N, FREQ, Q_AMPX]
    
    PHASE.plot = False
    MAG.plot = False
    Q.plot = False
    I.plot = False
    SINGLE_SHOT.plot = False
    I.plot_args["plot_type"] = "image"

    PHASE.datafn_args = {"delay": 2.792e-7, "freq": RR.int_freq}
    
   
    datasets = [I, Q, MAG, PHASE]
    ######################## INITIALIZE AND RUN EXPERIMENT #############################
    
    flux_values = np.linspace(start=-8e-3, stop=-12e-3, num=5)
    drive_IF = [120e6, 124e6, 180e6]

    for index_f in range(len(flux_values)): 
        for index_d in range(len(drive_IF)):
            with Stage(configpath=MODES_CONFIG, remote=True) as stage:
                (yoko1,opx1000) = stage.get("yoko1","opx1000")
                yoko_target = flux_values[index_f]
                yoko1.ramp(yoko_target, step=0.1e-3)
                parameters["drive_frequency"] = drive_IF[index_d]
                expt = snail_stark_shift_sweep(FOLDER, modes, pulses, sweeps, datasets, **parameters)
                expt.run()
                time.sleep(1) 

