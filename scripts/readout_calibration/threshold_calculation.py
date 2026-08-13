""" Readout integration weights training for single-shot readout """

import datetime
from pathlib import Path

from qcore import Stage
from qcore.instruments import QM
from qcore.scripts.readout_training_octave_old import ReadoutTrainerOctave

from config.experiment_config import MODES_CONFIG
from config.experiment_config import (
    RR,
    QUBIT,
)

if __name__ == "__main__":
    """ """

    with Stage(configpath=MODES_CONFIG, remote=True) as stage:

        (opx1000,) = stage.get("opx1000")
        qm = QM(modes=(RR, QUBIT), oscillators=(opx1000,), opx=opx1000)
        
        params = {
            "reps": 20_000,
            "wait_time": 150_000,  # ns
            "readout_pulse": "rr_readout_pulse",  # pulse name used to readout
            "qubit_pi_pulse": "qubit_gaussian_pulse_60",  # pulse name used to excite qubit
        }
 
        ro_trainer = ReadoutTrainerOctave(RR, QUBIT, qm, **params)
        threshold, data = ro_trainer.calculate_threshold()