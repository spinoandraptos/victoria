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
        lo_qubit, lo_rr, lo_cav = stage.get(
            "lo_qubit", "lo_rr", "lo_cav"
        )
        qubit, rr, sa, cav = stage.get("qubit", "rr", "sa", "cav")

        # CONFIGURE THE RR PROPERTIES AND OPERATIONS
        lo_rr.frequency = 7.6149e9 +0.15e6 + 50e6
        lo_rr.power = 15.0
        lo_rr.output = True

        rr.configure(
            name="rr",
            lo_name="lo_rr",
            ports={"I": 5, "Q": 6, "out": 1},
            int_freq=-49.4e6,
            tof=272,
        )

        rr.operations = [
            # ConstantReadoutPulse(
            #     name="rr_readout_pulse",
            #     length=400,  # 400, #400, #400,  # 10000,
            #     I_ampx=0.25,  # 1,
            #     pad=400,
            #     digital_marker=DigitalWaveform("ADC_ON"),
            #     # threshold= 0.0004282540982746491,
            #     # weights="C:/Users/qcrew/Desktop/qcrew/qcrew/config/weights/20230720_142024_opt_weights.npz",
            # ),
            ConstantReadoutPulse(
                name="rr_readout_pulse",
                length=600,  # 400,  # 400, #400,  # 10000,
                I_ampx=1.95,#1.95*0.1,  # 0.014,  # 0.02,  # 0.25,
                pad=300,
                digital_marker=DigitalWaveform("ADC_ON"),
                # threshold= 0.0004282540982746491,
                # weights=r"C:\Users\qcrew\Documents\eunice\config\weights\20260212_133929_weights.npz",
            ),
            ConstantPulse(
                name="spectrum_analysis_constant_pulse",
                length=5000,  # 2000,
                I_ampx=1.0,
                pad=0
            ),
        ]

        # CONFIGURE THE QUBIT PROPERTIES AND OPERATIONS
        lo_qubit.frequency = 5.7e9-200E6
        lo_qubit.power = 15.0
        lo_qubit.output = True


        qubit.configure(
            name="qubit",
            lo_name="lo_qubit",
            ports={"I": 1, "Q": 2},
            int_freq=113e6,
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

        # CONFIGURE THE CAVITY PROPERTIES AND OPERATIONS

        lo_cav.frequency = 7.14e9+50e6#+400e6  # +50e3 # -50e3 # 3e9 in anapico channel 3
        lo_cav.power = 15.0  # 15.0
        lo_cav.output = True

        cav.configure(
            name="cav",
            lo_name="lo_cav",
            ports={
                "I": 7,
                "Q": 8,
            },
            int_freq=-110e6,  # +5e6,  # -31.545e6,
        )

        cav.operations = [
            ConstantPulse(
                name="cav_constant_pulse_100000",
                length=100000,
                I_ampx=1.95,
            ),
            ConstantPulse(
                name="cav_const_1",
                length=160,
                I_ampx=1.95,
            ),
            ConstantPulse(
                name="cav_cohstate_long",
                length=160,
                I_ampx=1.9,
            ),
            ConstantPulse(
                name="cav_cohstate_superlong",
                length=10000,
                I_ampx=1.9,
            ),
            GaussianPulse(
                name="cav_gaussian_shortest",
                sigma=8,
                chop=4,
                I_ampx=1.9,
                Q_ampx=0.0,
            ),
            GaussianPulse(
                name="cav_gaussian_long",
                sigma=40,
                chop=4,
                I_ampx=0.5,
                Q_ampx=0.0,
            ),
            GaussianPulse(
                name="ECD_gaussian_1",
                sigma=40,
                chop=4,
                I_ampx=0.2,
                Q_ampx=0.0,
            ),
            GaussianPulse(
                name="cav_gaussian_short",
                sigma=40,
                chop=4,
                I_ampx=0.3,
                Q_ampx=0.0,
            ),
            ConstantPulse(
                name="spectrum_analysis_constant_pulse",
                length=1000,  # 2000,
                I_ampx=1.0,
                pad=0
            ),
        ]
