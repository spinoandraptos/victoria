""" """

from qcore.helpers import Stage
from qcore.modes import *
from qcore.pulses import *

from config.experiment_config import MODES_CONFIG

if __name__ == "__main__":
    """ """

    # configpath must be the path to the modes config file
    # remote = True means the Stage will connect with the Server and stage instruments
    # for remote = True to work, please run setup_server.bat first

    # NOTE adding digital markers to test RF switch to RR

    with Stage(configpath=MODES_CONFIG, remote=True) as stage:
        # RETRIEVE INSTRUMENTS AND MODES
        lo_qubit, lo_rr = stage.get(
            "lo_qubit", "lo_rr"
        )
        qubit, rr, sa = stage.get("qubit", "rr", "sa")

        # CONFIGURE THE RR PROPERTIES AND OPERATIONS
        lo_rr.frequency = 7.34351e9
        lo_rr.power = 15.0
        lo_rr.output = True

        rr.configure(
            name="rr",
            lo_name="lo_rr",
            ports={"I": 5, "Q": 6, "out": 1},
            int_freq=-50e6,
            tof=272,
        )

        rr.operations = [
            ConstantReadoutPulse(
                name="rr_readout_pulse",
                length=400,#600,  # 2000,
                I_ampx=1,
                pad=300, #1200, #
                digital_marker=DigitalWaveform("ADC_ON"),
            ),
            ConstantPulse(
                name="spectrum_analysis_constant_pulse",
                length=5000,  # 2000,
                I_ampx=1.0,
                pad=0
            ),
        ]

        # CONFIGURE THE QUBIT PROPERTIES AND OPERATIONS
        lo_qubit.frequency = 6e9
        lo_qubit.power = 15.0
        lo_qubit.output = True


        qubit.configure(
            name="qubit",
            lo_name="lo_qubit",
            ports={"I": 1, "Q": 2},
            int_freq=53e6-580e3,
        )

        qubit.operations = [
            ConstantPulse(
                name="qubit_constant_pulse_10000",
                length=10000,
                I_ampx=1.95,
            ),
            ConstantPulse(
                name="qubit_constant_pulse_100",
                length=100,
                I_ampx=1.95,
            ),
            ConstantPulse(
                name="qubit_constant_pi_pulse_32",
                length=32,
                I_ampx=1.95,
            ),
            ConstantPulse(
                name="qubit_constant_pi2_pulse_32",
                length=32,
                I_ampx=1.1/2,
            ),
            ConstantPulse(
                name="spectrum_analysis_constant_pulse",
                length=1000,  # 2000,
                I_ampx=1.0,
                pad=0
            ),
            # ConstantPulse(
            #     name="qubit_constant_pi2_pulse",
            #     length=64,
            #     I_ampx=1 * 0.5 / 0.7 / 4,
            # ),
            ConstantPulse(
                name="qubit_constant_pi_pulse_320",
                length=320,
                I_ampx=0.27,
            ),
            ConstantPulse(
                name="qubit_constant_pi_pulse_640",
                length=640,
                I_ampx=0.5,
            ),
            ConstantPulse(
                name="qubit_constant_pi_pulse_800",
                length=800,
                I_ampx=1.1/800*3*1.1*0.5/0.31,
            ),
            # ConstantPulse(
            #     name="qubit_constant_lessselective_pi_pulse",
            #     length=200,
            #     I_ampx=1,
            # ),
            # GaussianPulse(
            #     name="qubit_gaussian_pi2_pulse_short",
            #     sigma=16,
            #     chop=4,
            #     I_ampx=0.8750,
            #     Q_ampx=0.0,
            # ),
            GaussianPulse(
                name="qubit_gaussian_pi_4",
                sigma=4,
                chop=4,
                I_ampx=0.05 * 0.5 / 0.282 * 2 * 0.5 / 0.385 * 0.5 / 0.448,
                Q_ampx=0.0,
                drag=0.0,
            ),
            GaussianPulse(
                name="qubit_gaussian_pi2_4",
                sigma=4,
                chop=4,
                I_ampx=0.05 * 0.5 / 0.282 * 2 * 0.5 / 0.385 * 0.5 / 0.448 / 2,
                Q_ampx=0.0,
                drag=0.0,
            ),
            # GaussianPulse(
            #     name="qubit_gaussian_pi_pulse_short_4",
            #     sigma=12,
            #     chop=4,
            #     I_ampx=1.99,
            #     Q_ampx=0.0,
            # ),
            GaussianPulse(
                name="qubit_gaussian_pi_pulse",
                sigma=40,
                chop=4,
                I_ampx=0.7014,
                Q_ampx=0.0,
            ),
            GaussianPulse(
                name="qubit_gaussian_pi_pulse_200",
                sigma=200,
                chop=4,
                I_ampx=0.28056 / 2 * 0.5 / 0.3 * 0.5 / 0.58 * 0.5 / 1.03,
                Q_ampx=0.0,
            ),
            RampedConstantPulse(
                name="qubit_cos_ramp_pulse",
                ramp=10,
                rampfn="cos",
                length=20,
                I_ampx=1.4,
            ),
        ]