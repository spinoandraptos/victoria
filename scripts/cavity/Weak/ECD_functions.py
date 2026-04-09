from cmath import cos
from qcore import qua
import numpy as np
from qm import qua as qm_qua
from qm.qua import *


def Char_1D_singledisplacement(
    cav,
    qubit,
    displacement_pulse,
    qubit_pi_pulse,
    qubit_pi2_pulse,
    ampx,
    delay,
    measure_real,
    tomo_phase,
):

    # bring qubit into superposition
    qua.align(qubit, cav)
    qubit.play(qubit_pi2_pulse)

    # start ECD gate
    qua.align(qubit, cav)  # wait for qubit pulse to end
    # First positive displacement
    cav.play(displacement_pulse, ampx, phase=tomo_phase)

    qua.wait(int(delay), cav)
    # First negative displacement
    cav.play(displacement_pulse, -ampx, phase=tomo_phase)

    qua.align(qubit, cav)
    qubit.play(qubit_pi_pulse, phase=0.25)  # play pi to flip qubit around X
    qua.align(qubit, cav)  # wait for qubit pulse to end

    # Second negative displacement
    cav.play(displacement_pulse, -ampx, phase=tomo_phase)

    qua.wait(int(delay), cav)
    # Second positive displacement
    cav.play(displacement_pulse, ampx, phase=tomo_phase)

    qua.align(qubit, cav)

    qubit.play(
        qubit_pi2_pulse, phase=0 if measure_real else 0.25
    )  # play pi/2 pulse around X or SY, to measure either the real or imaginary part of the characteristic function


def Char_2D_singledisplacement(
    cav,
    qubit,
    displacement_pulse,
    qubit_pi_pulse,
    qubit_pi2_pulse,
    ampx_x,
    ampx_y,
    delay,
    measure_real,
    tomo_phase,
):

    # bring qubit into superposition
    qua.align(qubit, cav)
    qubit.play(qubit_pi2_pulse)

    # start ECD gate
    qua.align(cav, qubit)  # wait for qubit pulse to end
    # First positive displacement
    cav.play(
        displacement_pulse, ampx=(ampx_x, -ampx_y, ampx_y, ampx_x), phase=tomo_phase
    )

    qua.wait(int(delay), cav)
    # First negative displacement
    cav.play(
        displacement_pulse, ampx=(-ampx_x, ampx_y, -ampx_y, -ampx_x), phase=tomo_phase
    )

    qua.align(qubit, cav)
    qubit.play(qubit_pi_pulse, phase=0.25)  # play pi to flip qubit around X
    qua.align(cav, qubit)  # wait for qubit pulse to end

    # Second negative displacement
    cav.play(
        displacement_pulse, ampx=(-ampx_x, ampx_y, -ampx_y, -ampx_x), phase=tomo_phase
    )

    qua.wait(int(delay), cav)
    # Second positive displacement
    cav.play(
        displacement_pulse, ampx=(ampx_x, -ampx_y, ampx_y, ampx_x), phase=tomo_phase
    )

    qua.align(qubit, cav)

    qubit.play(
        qubit_pi2_pulse, phase=0 if measure_real else 0.25
    )  # play pi/2 pulse around X or SY, to measure either the real or imaginary part of the characteristic function


def ECD(cav, qubit, displacement_pulse, qubit_pi_pulse, ampx, delay, tomo_phase):
    qua.align()  # wait for qubit pulse to end
    cav.play(
        displacement_pulse, ampx=ampx, phase=tomo_phase
    )  # First positive displacement
    qua.wait(int(delay), cav)
    cav.play(
        displacement_pulse, ampx=-ampx, phase=tomo_phase
    )  # First negative displacement
    qua.align()
    qubit.play(qubit_pi_pulse, phase=0.25)  # play pi to flip qubit around X
    qua.align()  # wait for qubit pulse to end
    cav.play(
        displacement_pulse, ampx=-ampx, phase=tomo_phase
    )  # Second negative displacement
    qua.wait(int(delay), cav)
    cav.play(
        displacement_pulse, ampx=ampx, phase=tomo_phase
    )  # Second positive displacement
    qua.align()


def U(cav, qubit, displacement_pulse, qubit_pi_pulse, qubit_pi2_pulse, ampx, delay):
    qua.align()
    qubit.play(qubit_pi2_pulse, phase=0.5)

    ECD(
        cav,
        qubit,
        displacement_pulse,
        qubit_pi_pulse,
        ampx,
        delay,
        phase=0,
        qubit_phase=0,
    )

    # qubit.play(qubit_pi_pulse, phase=0.75)  #0.25 in ECD and 0.75 to flip back
    # qubit.play(qubit_pi2_pulse, phase=0)

    qubit.play(qubit_pi2_pulse, phase=0.5)
    qua.align()


def V(cav, qubit, displacement_pulse, qubit_pi_pulse, qubit_pi2_pulse, ampx, delay):
    qua.align()
    qubit.play(qubit_pi2_pulse, phase=0.25)

    ECD(
        cav,
        qubit,
        displacement_pulse,
        qubit_pi_pulse,
        ampx,
        delay,
        phase=0.25,
        qubit_phase=0.25,
    )

    # qubit.play(qubit_pi_pulse, phase=0.75)  # reverse pi flip in ECD
    # qubit.play(qubit_pi2_pulse, phase=0.75)
    qubit.play(qubit_pi2_pulse, phase=0.25)  # reverse pi flip in ECD
    qua.align()


def V_cat(
    cav,
    qubit,
    displacement_pulse,
    qubit_pi_pulse,
    qubit_pi2_pulse,
    ampx,
    delay,
    # qubit_phase,
):
    qua.align()
    qubit.play(qubit_pi2_pulse, phase=0.25)
    
    ECD(
        cav,
        qubit,
        displacement_pulse,
        qubit_pi_pulse,
        ampx,
        delay,
        tomo_phase=0,
        # qubit_phase=0.25,
    )
    ###
    # qubit.play(qubit_pi_pulse, phase=0.75)  # reverse pi flip in ECD
    # qubit.play(qubit_pi2_pulse, phase=0.75)
    ###
    qubit.play(qubit_pi2_pulse, phase=0.25)
    qua.align()


def U_cat(
    cav,
    qubit,
    displacement_pulse,
    qubit_pi_pulse,
    qubit_pi2_pulse,
    ampx,
    delay,
    qubit_phase,
):
    qua.align()
    qubit.play(qubit_pi2_pulse, phase=0.5)

    ECD(
        cav,
        qubit,
        displacement_pulse,
        qubit_pi_pulse,
        ampx,
        delay,
        phase=0.25,
        qubit_phase=0,
    )

    # qubit.play(qubit_pi_pulse, phase=0.75)  # reverse pi flip in ECD
    # qubit.play(qubit_pi2_pulse, phase=0)
    qubit.play(qubit_pi2_pulse, phase=0.5)
    qua.align()
