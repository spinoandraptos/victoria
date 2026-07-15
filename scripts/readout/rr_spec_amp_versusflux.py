""" """
from config.experiment_config import FOLDER, N, FREQ, I, Q, MAG, PHASE, MODES_CONFIG, RR
from qcore import Experiment, qua, Sweep


from qcore.helpers import Stage
from qcore import Experiment, qua, Sweep
import time


class RRSpecAmp_flux(Experiment):
    """Readout resonator spectroscopy"""

    ############################# DEFINE PRIMARY DATASETS ##############################
    # these Datasets form the "raw" experimental data and will be streamed by the OPX
    # they must be specified at experiment runtime

    primary_datasets = ["I", "Q"]

    ############################## DEFINE PRIMARY SWEEPS ###############################
    # these Sweeps are uniquely associated with the Experiment subclass
    # these Sweeps must be specified at experiment runtime

    primary_sweeps = ["resonator_frequency"]

    ############################ DEFINE THE PULSE SEQUENCE #############################
    # ensure that you import 'qua' from 'qcore' and not from 'qm' library
    # attributes accessed via 'self' must be defined in 'if __name__ == "__main__"' code

    def sequence(self):
        """QUA sequence that defines this Experiment subclass"""
        #qua.reset_phase(self.resonator)
        qua.update_frequency(self.resonator, self.resonator_frequency)
        self.resonator.measure(
            self.readout_pulse, (self.I, self.Q), ampx=self.ro_ampx, demod_type="dual"
        )
        qua.wait(self.wait_time, self.resonator)


if __name__ == "__main__":
    """ """

    #################################### MODE MAP ######################################
    # key: name of the Mode as defined by the Experiment subclass
    # value: name of the Mode as defined by the user in modes.yml

    modes = {"resonator": "rr"}

    ################################### PULSE MAP ######################################
    # key: name of the Pulse as defined by the Experiment subclass
    # value: name of the Pulse as defined by the user in modes.yml

    pulses = {"readout_pulse": "rr_readout_pulse"}

    ############################## CONTROL PARAMETERS ##################################

    parameters = {
        "wait_time": 20_000,
        # "ro_ampx": 1,
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    ################################### 1D SWEEP #######################################

    # set number of repetitions for this Experiment run
    N.num = 1_000
 
    # set the qubit frequency sweep for this Experiment run
    FREQ.name = "resonator_frequency"
    FREQ.start = -50.5e6
    FREQ.stop = -49e6
    FREQ.num = 201#101

    ################################### 2D SWEEP #######################################

    RO_AMPX = Sweep(
        name="ro_ampx",
        # points=[0.05,0.1,0.5, 0.6, 0.7, 0.8, 0.9, 1]
        # points=[0.1, 0.2, 0.3, 0.5, 1, 1.5]#0.25,0.5,0.75] #[0.01,0.05, 0.08,0.1, 0.2, 0.3, 0.4]
        # points=[0.01, 0.2, 0.5, 0.8, 1.0, 1.2]
        points=[0.01, 0.05, 0.1, 0.5 ,1]#0.25,0.5,0.75]
    ) 
    sweeps = [N, RO_AMPX, FREQ]
    
    # sweeps = [N, FREQ]

        ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass
    PHASE.inputs = ("I", "Q", "resonator_frequency")
    PHASE.datafn_args = {"delay": 2.792e-7}
    PHASE.plot = False
    MAG.plot = False
    I.plot = False
    Q.plot = False

    # MAG.fitfn = "gaussian"

    datasets = [I, Q, MAG, PHASE]

    ######################## INITIALIZE AND RUN EXPERIMENT #############################
    import numpy as np

    ######################## INITIALIZE AND RUN EXPERIMENT #############################

    # expt = RRSpec(FOLDER, modes, pulses, sweeps, datasets, current_value=1.23e-3, **parameters)
    flux_values = np.linspace(start=0e-3, stop=10e-3, num=81)

    # = np.arange(start_flux, stop_flux + step, step)  # Include stop value+
    # lo_rr_values = [7825033798.617158+5E6+1.8E6,  7825033798.617158+5E6+1.8E6+1.5E6 , 7825033798.617158+5E6+1.8E6+1.5E6 +1.5E6-1.1E6, 7825033798.617158+5E6+1.8E6+1.5E6 +1.5E6-1.1E6,7825033798.617158+5E6+1.8E6+1.5E6 +1.5E6-1.1E6 ]
    
    # lo_qubit_values = np.arange(4e9, 7.6e9 + 400e6, 400e6)

    # Generate the linearly spaced values
    # LO_list = flux_values
     
    # power_sweep = np.linspace(start=0, stop=1.5, num=16)#[0.005, 0.01, 0.05, 0.1, 0.2, 0.5, 1]
    # for power_rr in power_sweep:
    for index_f in range(len(flux_values)): 
        with Stage(configpath=MODES_CONFIG, remote=True) as stage:
            (yoko1, rr) = stage.get("yoko1", "rr")
            yoko_target = flux_values[index_f]
            yoko1.ramp(yoko_target, step=0.1e-3)
            # parameters["ro_ampx"] = power_rr
            
            expt = RRSpecAmp_flux(FOLDER, modes, pulses, sweeps, datasets, **parameters)
            expt.run()
            # expt.run(simulate=True)
            time.sleep(1)  # Sleeps for 1 second; adjust as needed
    # yoko1.ramp(0e-3, step=1e-4)
