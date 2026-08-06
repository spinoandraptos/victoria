""" Readout integration weights training for single-shot readout """

import sys

import datetime
from pathlib import Path

from qcore import Stage
from qcore.instruments import QM
from qcore.scripts.readout_training_octave import ReadoutTrainerOctave

from config.experiment_config import MODES_CONFIG, FOLDER
from config.experiment_config import RR, QUBIT, qubit_EF

if __name__ == "__main__":
    """ """

    with Stage(configpath=MODES_CONFIG, remote=True) as stage:

        (opx1000,) = stage.get("opx1000")
        qm = QM(modes=(RR, QUBIT,qubit_EF), oscillators=(opx1000,), opx=opx1000) 
        # Save file with today's date
        date_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_weights.npz")
        file_path = Path(FOLDER) / "config/weights" / date_str

        params = {
            "reps": 20_000,
            "wait_time": 110_000,  # ns
            "readout_pulse": "rr_readout_pulse",  # pulse name used to readout
            "qubit_pi_pulse": "qubit_constant_pi_36",  # pulse name used to excite qubit
            # "qubitEF_pi_pulse": "qAEF_short_gaussian_pi_pulse",  # pulse name used to excite qubit
            "weights_file_path": file_path,
        }

        ro_trainer = ReadoutTrainerOctave(RR, QUBIT,qubit_EF, qm, **params)
        ro_trainer.train_weights(use_GF=False)

        ## Make sure to run this script every time the readout pulse is changed!!
