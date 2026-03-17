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
        lo_cav, lo_qubit, lo_rr = stage.get("lo_cav", "lo_qubit", "lo_rr")
        qubit, qubitEF, rr, sa, cav, yoko= stage.get("qubit", "qubitEF", "rr", "sa", "cav", "yoko1")
        
        yoko.output=True
        yoko.ramp(0e-3, step=0.1e-3)

        # CONFIGURE THE RR PROPERTIES AND OPERATIONS
        lo_rr.frequency = 7.876950000e9+50e6-4.5e6+5.4e6 #7.78163552e9+50e6+50e6-150e6
        lo_rr.power = 15.0
        lo_rr.output = True

        rr.configure(
            name="rr",
            lo_name="lo_rr",
            ports={"I": 5, "Q": 6, "out": 1},
            int_freq=50e6,
            tof=272,
        )

        rr.operations = [
            ConstantPulse(
                name="rr_constant_pulse",
                length=1000,
                I_ampx=0.4,
            ),
            GaussianPulse(
                name="rr_gaussian_pulse",
                sigma=100,
                chop=6,
                I_ampx=1.0,
                Q_ampx=0.0,
            ),
            ConstantReadoutPulse(
                name="rr_readout_pulse",
                length=600,  # 2000,
                I_ampx=0.2,
                pad=600,
                digital_marker=DigitalWaveform("ADC_ON"),
                # threshold= 0.0004282540982746491,
                # weights="C:/Users/qcrew/Desktop/qcrew/qcrew/config/weights/20230720_142024_opt_weights.npz",
            ),
            ConstantPulse(
                name="spectrum_analysis_constant_pulse",
                length=1000,  # 2000,
                I_ampx=1.0,
                pad=0
            ),
        ]

        # CONFIGURE THE QUBIT PROPERTIES AND OPERATIONS
        lo_qubit.frequency =  6.145000000e9 +50e6#6.575800000e9-15e6-2e6+2.3e6-0.9E6-150e6#-200e6
        lo_qubit.power = 15.0
        lo_qubit.output = True

        qubit.configure(
            name="qubit",
            lo_name="lo_qubit",
            ports={"I": 1, "Q": 2},
            int_freq=68e6,
        )

        qubit.operations = [
            ConstantPulse(
                name="qubit_constant_pulse_10000",
                length=1000,
                I_ampx=0.05,
            ),
            ConstantPulse(
                name="qubit_constant_pi_pulse",
                length=52,
                I_ampx=1,
            ),
            ConstantPulse(
                name="qubit_constant_pi_pulse_400",
                length=400,
                I_ampx=0.01*0.5/0.34,
            ),
            ConstantPulse(
                name="qubit_constant_pi_pulse_16",
                length=16,
                I_ampx=0.25*0.5/0.41
            ),
            ConstantPulse(
                name="qubit_constant_pi_pulse_28",
                length=28,
                I_ampx=0.3,
            ),
            ConstantPulse(
                name="qubit_constant_pi_pulse_52",
                length=52,
                I_ampx=0.2,
            ),
            ConstantPulse(
                name="qubit_constant_pi_pulse_100",
                length=100,
                I_ampx=1.33,
            ),
            ConstantPulse(
                name="qubit_constant_pi_pulse_300",
                length=300,
                I_ampx=1.33,
            ),
            ConstantPulse(
                name="qubit_constant_pi2_pulse",
                length=52,
                I_ampx=0.595 / 2,
            ),
            ConstantPulse(
                name="qubit_constant_selective_pi_pulse",
                length=1000,
                I_ampx=0.032,
            ),
            ConstantPulse(
                name="qubit_constant_very_selective_pi_pulse",
                length=4000,
                I_ampx=0.01,
            ),
            GaussianPulse(
                name="qubit_gaussian_pulse",
                sigma=200,
                chop=4,
                I_ampx=0.032,
                Q_ampx=0.0,
            ),
            RampedConstantPulse(
                name="qubit_cos_ramp_pulse",
                ramp=10,
                rampfn="cos",
                length=20,
                I_ampx=1.4,
            ),
            ConstantPulse(
                name="spectrum_analysis_constant_pulse",
                length=1000,  # 2000,
                I_ampx=1.0,
                pad=0
            ),
        ]
        
        # lo_qubitEF = 6.288800000e9
        qubitEF.configure(
            name="qubitEF",
            lo_name="lo_qubit",
            ports={"I": 1, "Q": 2},
            int_freq=-124.6e6,
        )

        qubitEF.operations = [
            ConstantPulse(
                name="qubitEF_constant_pulse_10000",
                length=10000,
                I_ampx=0.5,
            ),
            ConstantPulse(
                name="qubitEF_constant_pi_pulse",
                length=52,
                I_ampx=1,
            ),
            ConstantPulse(
                name="qubitEF_constant_pi_pulse_400",
                length=400,
                I_ampx=1.33,
            ),
            ConstantPulse(
                name="qubitEF_constant_pi_pulse_96",
                length=96,
                I_ampx=1#0.5*0.5/0.318,
            ),
            ConstantPulse(
                name="qubitEF_constant_pi_pulse_28",
                length=28,
                I_ampx=0.3,
            ),
            ConstantPulse(
                name="qubitEF_constant_pi_pulse_300",
                length=300,
                I_ampx=1.33,
            ),
            ConstantPulse(
                name="qubitEF_constant_pi2_pulse",
                length=52,
                I_ampx=0.595 / 2,
            ),
            ConstantPulse(
                name="qubitEF_constant_selective_pi_pulse",
                length=1000,
                I_ampx=0.032,
            ),
            ConstantPulse(
                name="qubitEF_constant_very_selective_pi_pulse",
                length=4000,
                I_ampx=0.008,
            ),
            GaussianPulse(
                name="qubitEF_gaussian_pulse",
                sigma=200,
                chop=4,
                I_ampx=0.032,
                Q_ampx=0.0,
            ),
            RampedConstantPulse(
                name="qubitEF_cos_ramp_pulse",
                ramp=10,
                rampfn="cos",
                length=20,
                I_ampx=1.4,
            ),
        ]

        # CONFIGURE THE CAVITY PROPERTIES AND OPERATIONS
        lo_cav.frequency =  6.715900000e9-50e6#7.4133e9+50e6#-400e6
        lo_cav.power = 15.0
        lo_cav.output = True

        cav.configure(
            name="cav",
            lo_name="lo_cav",
            ports={"I": 7, "Q": 8},
            int_freq=53.4e6,
        )

        cav.operations = [
            ConstantPulse(
                name="cavity_constant_pulse_10000",
                length=10000,
                I_ampx=1.95,#0.2,
            ),
             ConstantPulse(
                name="cavity_constant_pulse_10000_weaker",
                length=10000,
                I_ampx=0.4,#0.2,
            ),
             ConstantPulse(
                name="cavity_constant_pulse_5000_weaker",
                length=5000,
                I_ampx=1.2,
            ),
            ConstantPulse(
                name="cavity_constant_pi_400",
                length=400,
                I_ampx=1,#0.2,
            ),
            ConstantPulse(
                name="cavity_constant_pi_100",
                length=100,
                I_ampx=1,#0.2,
            ),
            ConstantPulse(
                name="cavity_constant_pi_52",
                length=52,
                I_ampx=1,#0.2,
            ),
            ConstantPulse(
                name="cavity_constant_pi_800",
                length=800,
                I_ampx=1,#0.2,
            ),
            ConstantPulse(
                name="cavity_constant_pi_400",
                length=400,
                I_ampx=1.95,#0.2,
            ),
            GaussianPulse(
                name="cavity_gaussian_pulse",
                sigma=200,
                chop=4,
                I_ampx=0.032,
                Q_ampx=0.0,
            ),
            ConstantPulse(
                name="spectrum_analysis_constant_pulse",
                length=1000,  # 2000,
                I_ampx=1.0,
                pad=0
            ),
        ]