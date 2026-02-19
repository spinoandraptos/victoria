""" """

from qcore.helpers import Stage
from qcore.modes import *
from qcore.pulses import *

FOLDER = "C:/Users/qcrew/Documents/eunice/"
MODES_CONFIG = FOLDER + "config/modes.yml"

# from config.experiment_config import MODES_CONFIG

if __name__ == "__main__":
    """ """

    # configpath must be the path to the modes config file
    # remote = True means the Stage will connect with the Server and stage instruments
    # for remote = True to work, please run setup_server.bat first
    
    # NOTE adding digital markers to test RF switch to RR
    with Stage(configpath=MODES_CONFIG, remote=True) as stage:
        
        (opx1000, cav, qubit, rr) = stage.get("opx1000", "cav", "qubit", "rr")
    
        rr_LO = 7.8e9
        rr_IF = -50e6
        
        qubit_LO = 5e9
        qubit_IF = -50e6
        
        cav_LO = 7e9
        cav_IF = -50e6
        
        settings = {
                "controllers": {
                    "con1": {
                        "fems": {
                            2: {
                                "analog_outputs": {
                                    1: {
                                        "full_scale_power_dbm": -11, #only in increments of 3s
                                        "upconverters": {1: {"frequency":  rr_LO}},
                                        "band":3
                                    },
                                    # 2: {
                                    #     "full_scale_power_dbm": 16,
                                    #     "upconverters": {1: {"frequency": alice_LO}},
                                    # },
                                    # 3: {
                                    #     "full_scale_power_dbm": 4,
                                    #     "upconverters": {1: {"frequency": bob_LO}}, #bob
                                    # },
                                    # 4: {
                                    #     "full_scale_power_dbm": -11, #16
                                    #     "upconverters": {1: {"frequency": alice_LO}},
                                    # },
                                    # 5: {
                                    #     "full_scale_power_dbm": 4, #10
                                    #     "upconverters": {1: {"frequency": charlie_LO}},
                                    # },
                                    # 6: {
                                    #     "full_scale_power_dbm": 16, 
                                    #     "upconverters": {1: {"frequency": qubit_LO}},
                                    # },
                                    7: {
                                        "full_scale_power_dbm": -8, 
                                        "upconverters": {1: {"frequency": qubit_LO}},
                                        "band":2
                                    },
                                    # 8: {
                                    #     "full_scale_power_dbm": -8, #-5,
                                    #     "upconverters": {1: {"frequency": rr_LO}},
                                    # },
                                },
                                "analog_inputs": {
                                    1: {
                                        "downconverter_frequency": rr_LO,
                                        "band":3
                                        },  # for down-conversion
                
                                },
                            },
                            
                        } 
                    }
                }
            }      
        opx1000.settings = settings
        
        rr.configure(
            name="rr",
            lo_name="opx1000",  # either octave or labbrick
            ports={
                "I": [2,1], "out1": [2,1] # [2, 1],[2,1]
            },  # OPX has two separate inputs (I, Q), from the Octave
            # ports={"I": 1, "Q": 2, "out": 1}, # OPX has I,Q combined in 1 input, from Labbrick downconversion
            int_freq=rr_IF,
            tof=264+36,
            rf_switch=None,
            rf_switch_on=False,
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
                length=2000,  # 2000,
                I_ampx=0.25,
                pad=600,
                digital_marker=DigitalWaveform("ADC_ON"),
                # threshold= 0.0004282540982746491,
                # weights="C:/Users/qcrew/Desktop/qcrew/qcrew/config/weights/20230720_142024_opt_weights.npz",
            ),
        ]

        qubit.configure(
            name="qubit",
            lo_name="opx1000",
            ports={"I": [2,7]},
            # int_freq=177.3065e6,
            int_freq=qubit_IF,
            rf_switch=None,
            rf_switch_on=False,
        )

        qubit.operations = [
            ConstantPulse(
                name="qubit_constant_pulse",
                length=10000,
                I_ampx=1.5,
            ),
            ConstantPulse(
                name="qubit_constant_pi_pulse",
                length=52,
                I_ampx=0.595,
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
                I_ampx=0.008,
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
        ]