from qm import qua as qm_qua
import numpy as np
from config.experiment_config import FOLDER, N, FREQ, I, Q, MAG, PHASE, MODES_CONFIG, RR
from qcore import Experiment, qua, Sweep
from qcore.helpers import Stage
from qcore.libs.qua_macros import QuaVariable
from cavity_self_kerr import CavitySelfKerr
import time

if __name__ == "__main__":
    """ """

    #################################### MODE MAP ######################################
    # key: name of the Mode as defined by the Experiment subclass
    # value: name of the Mode as defined by the user in modes.yml

    modes = {
        "cavity": "cavity",
        "qubit": "qubit",
        "resonator": "rr",
    }

    ################################### PULSE MAP ######################################
    # key: name of the Pulse as defined by the Experiment subclass
    # value: name of the Pulse as defined by the user in modes.yml

    pulses = {
        "cavity_drive": "cav_constant_48_ecd",
        "sel_qubit_pulse": "qubit_gaussian_pi_2000",
        "readout_pulse": "rr_readout_pulse",
    }

    ############################## CONTROL PARAMETERS ############# #####################

    parameters = {
        "wait_time": 800_000,
        "ro_ampx": 1,
        "detuning":10e6,
        "phase": QuaVariable(
            value=0.0,
            dtype=qm_qua.fixed,
            tag="phase",
            buffer=True,
            stream=True,
        ),
        "fetch_interval": 1,
        "plot_single_shot": False,
        
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this Experiment run
    N.num = 250

    # set the qubit frequency sweep for this Experiment run

    DEL = Sweep(name="time_delay", start=4, stop=2_000, step=8, dtype=int)
    DIS_AMPX = Sweep(
        name="disp_ampx",
        points=[0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
    ) 
    sweeps = [N, DIS_AMPX, DEL]

    PHASE.plot = False
    MAG.plot = False
    Q.plot = False
    I.plot = False
    
    # PHASE.plot = True
    # MAG.plot = True
    # Q.plot = True
    # I.plot = True
    
    ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass
    # I.fitfn = "gaussian"
    # Q.fitfn = "gaussian"
    # MAG.fitfn = "gaussian"
    # PHASE.fitfn = "gaussian"

    PHASE.datafn_args = {"delay": 2.792e-7, "freq": RR.int_freq}
    
   
    datasets = [I, Q, MAG, PHASE]
    flux_values = [-16.5e-3, -15e-3, -14e-3, -13e-3, -10.5e-3, 0e-3]
    cav_IF_values = [-9.7255e7, -1.0608e8, -1.365e8, -6.1813e7, -6.3762e7, -9.3195e7]
    # flux_values = [-16.5e-3]
    # cav_IF_values = [-9.7255e7]
   
    for index_f in range(len(flux_values)): 
        with Stage(configpath=MODES_CONFIG, remote=True) as stage:
            (yoko1,cavity) = stage.get("yoko1", "cavity")
            yoko_target = flux_values[index_f]
            yoko1.ramp(yoko_target, step=0.1e-3)
            
            cav_IF = cav_IF_values[index_f]
            cavity.configure(
                name="cavity",
                lo_name="opx1000",
                ports={"I": [1,2]},
                upconverter = 1,
                int_freq=cav_IF,
                rf_switch=None,
                rf_switch_on=False,
            )
                        
            expt = CavitySelfKerr(FOLDER, modes, pulses, sweeps, datasets, **parameters)
            expt.run()
            time.sleep(1)  # Sleeps for 1 second