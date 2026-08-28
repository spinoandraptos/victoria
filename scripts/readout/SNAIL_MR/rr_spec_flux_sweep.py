""" """
import sys
from datetime import datetime
from config.experiment_config import FOLDER, N, FREQ, I, Q, MAG, PHASE, SINGLE_SHOT, RR

from qcore import Experiment, qua, Sweep
from qm import qua as qm_qua
from qcore.helpers import Stage
from config.experiment_config import MODES_CONFIG
import numpy as np
import time


class RRSpec(Experiment):
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
        "wait_time": 10_000,
        "ro_ampx": 1,
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this Experiment run
    N.num = 5000

    
    # set the qubit frequency sweep for this Experiment run
    FREQ.name = "resonator_frequency"
    FREQ.start = -51e6
    FREQ.stop = -49e6
    FREQ.num = 101

    PHASE.plot = False
    MAG.plot = False
    Q.plot = False
    I.plot = False
    SINGLE_SHOT.plot = False
    
    sweeps = [N, FREQ]    #SINGLE_SHOT.plot_args["plot_type"] = "image"

    ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass


    PHASE.datafn_args = {"delay": 2.792e-7, "freq": RR.int_freq}
    
   
    datasets = [I, Q, MAG, PHASE]
    ######################## INITIALIZE AND RUN EXPERIMENT #############################
    flux_start = -100e-3
    flux_end = -190e-3
    flux_step = -10e-3
    flux_points = np.arange(flux_start, flux_end+flux_step, flux_step)

    with Stage(configpath=MODES_CONFIG, remote=True) as stage:
    
      print("START: "+ str(datetime.now()))

      for flux_point in flux_points:
        
        (yoko, opx1000) = stage.get("yoko1", "opx1000")
        yoko.output=True
        yoko.ramp(flux_point, step=1e-4)
        
        expt = RRSpec(FOLDER, modes, pulses, sweeps, datasets, **parameters)
        expt.run()
        
    print("END: "+ str(datetime.now()))
    yoko.output=True
    yoko.ramp(0e-3, step=1e-4)
      
