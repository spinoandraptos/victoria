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

from config.experiment_config import MODES_CONFIG, FOLDER
from config.experiment_config import (
    RR,
    QUBIT,
)

if __name__ == "__main__":
    """ """

    with Stage(configpath=MODES_CONFIG, remote=True) as stage:

        #(octave, opx_one) = stage.get("octave1", "opx_one")
        (opx1000,) = stage.get("opx1000")
        # qm = QM(modes=(RRC, QUBITC), oscillators=(octave,), opx_plus=opx_plus,config_path=f"{FOLDER}/config/")
        qm = QM(modes=(RR, QUBIT), oscillators=(opx1000,), opx=opx1000)
        # Save file with today's date
        date_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_weights.npz")
        file_path = Path(FOLDER) / "config/weights" / date_str

        params = {
            "reps": 20_000,
            "wait_time": 4e5,  # ns
            "readout_pulse": "rr_readout_pulse",  # pulse name used to readout
            "qubit_pi_pulse": "qubit_constant_pi_20",  # pulse name used to excite qubit
            "weights_file_path": file_path,
        }

        ro_trainer = ReadoutTrainerOctave(RR, QUBIT, qm, **params)
        ro_trainer.train_weights()

        ## Make sure to run this script every time the readout pulse is changed!!
