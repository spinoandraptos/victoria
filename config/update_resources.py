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
        
        (opx1000, qubit, rr, cavity, yoko, snail,cavity_m) = stage.get("opx1000", "qubit", "rr", "cavity", "yoko2", "snail", "cavity_m")
        
        yoko.output=True
        yoko.ramp(50e-3, step=1e-4)
    
        rr_LO = 7.88e9+32e6+21e6-0.3e6+0.1e6-0.3e6+0.1e6
        rr_IF = -50e6
        
        qubit_LO = 6e9+96.7e6+250e6-11e6+0.1e6
        qubit_IF = -50e6
        
        cav_LO = 6.7e9 + 53.4e6+19e6-2E6-2E6-4.9e6-0.3e6 #6.6e9+50e6
        cav_IF = -50e6
        
        snail_LO = 3.8e9+50e6#6.33e9#6.6e9+50e6
        snail_IF = -68e6# -68e6 #
        
        cavity_m_LO = 2.9312e9+50e6#6.33e9#6.6e9+50e6
        cavity_m_IF = -50e6#-68e6
        
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
                                    2: {
                                        "full_scale_power_dbm": 16, #-11 to 16
                                        "upconverters": {1: {"frequency": cav_LO}},
                                    },
                                    # 3: {
                                    #     "full_scale_power_dbm": 4,
                                    #     "upconverters": {1: {"frequency": bob_LO}}, #bob
                                    # },
                                    4: {
                                        "full_scale_power_dbm": 16, #16
                                        "upconverters": {1: {"frequency": snail_LO}},
                                    },
                                    5: {
                                        "full_scale_power_dbm": 16, #10
                                        "upconverters": {1: {"frequency": cavity_m_LO}},
                                    },
                                    # 6: {
                                    #     "full_scale_power_dbm": 16, 
                                    #     "upconverters": {1: {"frequency": qubit_LO}},
                                    # },
                                    7: {
                                        "full_scale_power_dbm": 7, 
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
            tof=300,#264+36,
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
                length=1000,  # 2000,
                I_ampx=0.08,
                pad=600, #1200, #
                digital_marker=DigitalWaveform("ADC_ON"),
                # weights=r"C:\Users\qcrew\Documents\eunice\config\weights\20260223_105919_weights.npz"
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
                I_ampx=0.6,
            ),
            ConstantPulse(
                name="qubit_constant_pi_52",
                length=52,
                I_ampx=1.36612,
            ),
            ConstantPulse(
                name="qubit_constant_pi2_52",
                length=52,
                I_ampx=1.36612 / 2,
            ),
            ConstantPulse(
                name="qubit_constant_pi_520",
                length=520,
                I_ampx=1.36612/10*0.5/0.468*0.5/0.47/2*0.5/0.457,
            ),
            ConstantPulse(
                name="qubit_constant_pi_260",
                length=260,
                I_ampx=0.14748208571*0.5/0.35*0.5/0.37,
            ),
            ConstantPulse(
                name="qubit_constant_pi_200",
                length=200,
                I_ampx=0.14748208571*0.5/0.35*0.5/0.37*0.5/0.6*0.5/0.663*0.5/0.477,
            ),
        ]
        
        snail.configure(
            name="snail",
            lo_name="opx1000",
            ports={"I": [2,4]},
            int_freq=snail_IF,
            rf_switch=None,
            rf_switch_on=False,
        )
        
        snail.operations = [
            ConstantPulse(
                name="snail_constant_pulse",
                length=10000,
                I_ampx=1.5,
            ),
            ConstantPulse(
                name="snail_constant_pulse_20",
                length=20,
                I_ampx=2,
            ),
            ConstantPulse(
                name="snail_constant_pulse_400",
                length=400,
                I_ampx=1/4,
            ),
            ConstantPulse(
                name="snail_constant_pi_52",
                length=52,
                I_ampx=2,
            ),
            ConstantPulse(
                name="snail_constant_pi2_52",
                length=52,
                I_ampx=1.36612 / 2,
            ),
            ConstantPulse(
                name="snail_constant_pi_520",
                length=520,
                I_ampx=1.36612/10*0.5/0.468,
            ),
        ]
        
        cavity.configure(
                name="cavity",
                lo_name="opx1000",
                ports={"I": [2,2]},
                int_freq=cav_IF,
                rf_switch=None, #alice_rf,
                rf_switch_on=False,
            )
        cavity.operations = [
                ConstantPulse(
                name="cav_constant_1000",
                length=1000,
                I_ampx=2.0,
            ),
                ConstantPulse(
                name="cav_constant_400",
                length=400,
                I_ampx=2/2*1.5,
            ),
            ConstantPulse(
                name="cav_constant_200",
                length=200,
                I_ampx=2*0.5,
            ),
            ConstantPulse(
                name="cav_constant_100",
                length=100,
                I_ampx=1.5,
            ),
            ConstantPulse(
                name="cav_constant_40",
                length=40,
                I_ampx=1.5,#1.5*0.15,
            ),

            

        ]
        
        cavity_m.configure(
                name="cavity_m",
                lo_name="opx1000",
                ports={"I": [2,5]},
                int_freq=cavity_m_IF,
                rf_switch=None, #alice_rf,
                rf_switch_on=False,
            )
        cavity_m.operations = [
                ConstantPulse(
                name="cav_m_constant_10000",
                length=10000,
                I_ampx=2.0,
            ),
                ConstantPulse(
                name="cav_m_constant_400",
                length=400,
                I_ampx=2,
            ),
            ConstantPulse(
                name="cav_m_constant_200",
                length=200,
                I_ampx=2,
            ),
            ConstantPulse(
                name="cav_m_constant_100",
                length=100,
                I_ampx=1.5*0.15,
            ),
            # ConstantPulse(
            #     name="cav_constant_100",
            #     length=100,
            #     I_ampx=1.5,
            # ),

            

        ]
        