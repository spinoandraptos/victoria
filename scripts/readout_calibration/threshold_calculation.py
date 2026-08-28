""" Readout integration weights training for single-shot readout """

""" Readout integration weights training for single-shot readout """
import sys
# The directory containing the 'config' folder
FOLDER = "C:/Users/qcrew/Documents/eunice/"

# Add the FOLDER itself to sys.path, not the file path
if FOLDER not in sys.path:
    sys.path.insert(0, FOLDER)
""" Readout integration weights training for single-shot readout """

import sys

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
        # qm = QM(modes=(RRC, QUBITC), oscillators=(octave,), opx_plus=opx_plus,config_path=f"{FOLDER}/config/")
        qm = QM(modes=(RR, QUBIT), oscillators=(opx1000,), opx=opx1000)
        
        params = {
            "reps": 10_000,
            "wait_time": 4e5,  # ns
            "readout_pulse": "rr_readout_pulse",  # pulse name used to readout
            "qubit_pi_pulse": "qubit_constant_pi_20",  # pulse name used to excite qubit
        }
 
        ro_trainer = ReadoutTrainerOctave(RR, QUBIT, qm, **params)
        threshold, data = ro_trainer.calculate_threshold()