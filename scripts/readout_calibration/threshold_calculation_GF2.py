""" Readout integration weights training for single-shot readout """

import datetime
from pathlib import Path

from qcore import Stage
from qcore.instruments import QM
from qcore.scripts.readout_training_octave import ReadoutTrainerOctave

from config.experiment_config import MODES_CONFIG
from config.experiment_config import (
    RR,
    qubit_GF2,
)

if __name__ == "__main__":
    """ """

    with Stage(configpath=MODES_CONFIG, remote=True) as stage:

        (opx1000,) = stage.get("opx1000")
        # qm = QM(modes=(RRC, QUBITC), oscillators=(octave,), opx_plus=opx_plus,config_path=f"{FOLDER}/config/")
        qm = QM(modes=(RR, qubit_GF2), oscillators=(opx1000,), opx=opx1000)
        
        params = {
            "reps": 10_000,
            "wait_time": 100_000,  # ns
            "readout_pulse": "rr_readout_pulse",  # pulse name used to readout
            "qubit_pi_pulse": "qubitGF2_gaussian_pi_24",  # pulse name used to excite qubit
        }
 
        ro_trainer = ReadoutTrainerOctave(RR, qubit_GF2, qm, **params)
        threshold, data = ro_trainer.calculate_threshold()