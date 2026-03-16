""" """

import matplotlib.pyplot as plt
from qm import qua

from qcore.instruments import QM
from qcore.pulses import ConstantPulse
from qcore import Stage

from config.experiment_config import (
    QUBIT,
   
    RR,
    CAV,
    LO_RR,
    LO_QUBIT,
    LO_CAV,
    SA,
)


def get_sweep(mode, lo, sa, qm, sa_pulse, **kwargs):
    # pulse = ConstantPulse("spectrum_analysis_constant_pulse")
    # mode.add_operations(pulse)
    sa.configure(**kwargs)

    def get_qua_program(mode):
        with qua.program() as play_constant_pulse:
            with qua.infinite_loop_():
                mode.play(sa_pulse, ampx=1.0)
        return play_constant_pulse

    job = qm.execute(get_qua_program(mode))  # play IF to mode
    freqs, amps = sa.sweep()  # get, plot, show sweep
    plt.plot(freqs, amps)
    job.halt()
    plt.show()


if __name__ == "__main__":
    mode = CAV
    mode_lo = LO_CAV

    sweep_parameters = {  # set sweep parameters
        "center": mode_lo.frequency,  # 1e9,
        "span": 400e6,
        "rbw": 250e3,
        "ref_power": 0,
    }
    
    with Stage(remote=True) as stage:
            instruments = {rsc.name: rsc for rsc in stage.get(*stage.resources)}
            opx=instruments.get("opx_plus",instruments.get("opx1000"))
            qm = QM(modes=(mode,), oscillators=(mode_lo,), opx=opx)
            pulses = {p.name: p for p in mode.operations.values()}
            sa_pulse = pulses["spectrum_analysis_constant_pulse"]
            get_sweep(mode, mode_lo, SA, qm, sa_pulse, **sweep_parameters)