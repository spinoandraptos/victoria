from config.experiment_config import FOLDER, N, FREQ, I, Q, MAG, PHASE, MODES_CONFIG, RR
from qcore import Experiment, qua, Sweep


from qcore.helpers import Stage
from qcore import Experiment, qua, Sweep
import time

class QubitSpec_snaildrive(Experiment):
    """Qubit spectroscopy"""

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
        qua.reset_phase(self.resonator)
        
        qua.update_frequency(self.drive, self.drive_frequency)
        
        self.drive.play(self.drive_pulse)
        qua.align(self.qubit, self.drive)
        #qua.update_frequency(self.resonator, self.resonator_frequency)
        self.qubit.play(self.qubit_drive, ampx=self.qubit_drive_ampx)
        qua.align()
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
        "drive": "drive",
    }

    ################################### PULSE MAP ######################################
    # key: name of the Pulse as defined by the Experiment subclass
    # value: name of the Pulse as defined by the user in modes.yml

    pulses = {
        "drive_pulse": "drive_constant_5000",
        "qubit_drive": 'qubit_gaussian_pi_1200',#"qubit_constant_pi_400",#"qubit_constant_pulse",#"qubit_constant_pi_1500",
        "readout_pulse": "rr_readout_pulse",
    }

    ############################## CONTROL PARAMETERS ##################################

    parameters = {
        "wait_time": 50000,
        "ro_ampx": 1.0,
        "qubit_drive_ampx": 1,
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this E xperiment run
    N.num = 20000

    # set the qubit frequency sweep for this Experiment run
    FREQ.name = "drive_frequency"
    FREQ.start =-200e6  # 40e6
    FREQ.stop = 0e6  # 60e6 #the 60e6 is from the lo used to generate ef pulse
    FREQ.num = 101
    

    sweeps = [N, FREQ]

    ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass

    PHASE.datafn_args = {"delay": 2.792e-7, "freq": RR.int_freq}
    PHASE.plot = False
    I.plot = False
    Q.plot = False
    MAG.plot = False


    datasets = [I, Q, MAG, PHASE]

    ######################## INITIALIZE AND RUN EXPERIMENT #############################
    import datetime
    
    # flux_start = 0e-3
    # flux_end = 50e-3
    # flux_step = 10e-3
    # flux_points = np.arange(flux_start, flux_end+flux_step, flux_step)

    import numpy as np

    # start_flux = -7e-3
    # stop_flux = -2e-3
    # step = 0.1e-3
    flux_values = np.linspace(start=10e-3, stop=-20e-3, num=5)  # 121)  # np.linsp

    # = np.arange(start_flux, stop_flux + step, step)  # Include stop value+
    # lo_rr_values = [7825033798.617158+5E6+1.8E6,  7825033798.617158+5E6+1.8E6+1.5E6 , 7825033798.617158+5E6+1.8E6+1.5E6 +1.5E6-1.1E6, 7825033798.617158+5E6+1.8E6+1.5E6 +1.5E6-1.1E6,7825033798.617158+5E6+1.8E6+1.5E6 +1.5E6-1.1E6 ]
    
    # lo_qubit_values = np.arange(4e9, 7.6e9 + 400e6, 400e6)

    # Generate the linearly spaced values
    # LO_list = flux_values
     

    for index_f in range(len(flux_values)): 
        with Stage(configpath=MODES_CONFIG, remote=True) as stage:
            (yoko1,) = stage.get("yoko1")
            yoko_target = flux_values[index_f]
            yoko1.ramp(yoko_target, step=0.1e-3)
            expt = QubitSpec_snaildrive(FOLDER, modes, pulses, sweeps, datasets, **parameters)
            expt.run()
            # expt.run(simulate=True)
            time.sleep(1)  # Sleeps for 1 second; adjust as needed
        yoko1.ramp(0e-3, step=1e-4)
