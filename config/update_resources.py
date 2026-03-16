""" """

from qcore.helpers import Stage
from qcore.modes import *
from qcore.pulses import *
# from qcore.pulses.clear_readout_pulse import ClearReadoutPulse

FOLDER = "C:\\Users\\qcrew2\\Documents\\Candace\\eunice\\"
MODES_CONFIG = FOLDER + "config/modes.yml"



# from config.experiment_config import MODES_CONFIG

if __name__ == "__main__":
    """ """

    # configpath must be the path to the modes config file
    # remote = True means the Stage will connect with the Server and stage instruments
    # for remote = True to work, please run setup_server.bat first
    
    # NOTE adding digital markers to test RF switch to RR
    with Stage(configpath=MODES_CONFIG, remote=True) as stage:
        
        (opx1000, qubit, rr, cavity, yoko1) = stage.get("opx1000", "qubit", "rr", "cavity", "yoko1")
        
        yoko1.output = True
        yoko1.ramp(stop=0e-3, start=None, step=0.1e-3)
    
        # rr_LO = 7.88e9+32e6+21e6-0.3e6-2e6-0.6e6-0.15e6
        # rr_IF = -53e6
        
        # qubit_LO = 6e9+96.7e6+250e6-11e6+0.1e6-200e6+50e6-4.6e6-150e6
        # qubit_IF = 113.8e6
        
        # cav_LO = 6.7e9 + 53.4e6+19e6-1E6#-20e6#6.6e9+50e6
        # cav_IF = -53.5e6
    
        rr_LO =7.78163552e9+50e6#7.787955E9+50E6+0.2e6-6E6#7.88e9+32e6+21e6-0.3e6
        rr_IF = -50e6
        
        qubit_LO = 6e9+96.7e6+250e6-11e6+0.1e6+400e6-200e6-200e6-400e6#+70e6-1.7e6
        qubit_IF = -160e6

        
        cav_LO = 7.4e9+50e6+13.3e6#6.7e9 + 53.4e6+19e6-1E6#6.6e9+50e6
        cav_IF = -50e6
        
        settings = {
                "controllers": {
                    "con1": {
                        "fems": {
                            8: {
                                "analog_outputs": {
                                    1: {
                                        "full_scale_power_dbm": 16, #only in increments of 3s -11 1
                                        "upconverters": {1: {"frequency":  rr_LO}},
                                        "band":3,
                                    },
                                    3: {
                                        "full_scale_power_dbm": 16, #-11 to 16
                                        "upconverters": {1: {"frequency": cav_LO}},
                                        "band":3,
                                    },
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
                                    5: {
                                        "full_scale_power_dbm": 16, 
                                        "upconverters": {1: {"frequency": qubit_LO}},
                                        "band":2,
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
                "I": [8,1], "out1": [8,1] # [2, 1],[2,1]
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
                length=5000,#600,  # 2000,
                I_ampx=1.95, #1,
                pad=600, #1200, #
                digital_marker=DigitalWaveform("ADC_ON"),
                # weights=r"C:\Users\qcrew\Documents\eunice\config\weights\20260219_174734_weights.npz"
            ),
        ]

        cavity.configure(
            name="cavity",
            lo_name="opx1000",
            ports={"I": [8,3]},
            int_freq=cav_IF,
            rf_switch=None, #alice_rf,
            rf_switch_on=False,
        )
        
        cavity.operations = [
                ConstantPulse(
                name="cav_constant_10000",
                length=10000,
                I_ampx=2.0,
            ),
                ConstantPulse(
                name="cav_constant_400",
                length=400,
                I_ampx=2/2,
            ),
        ]
        

        qubit.configure(
            name="qubit",
            lo_name="opx1000",
            ports={"I": [8,5]},
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
                name="qubit_constant_pi_160",
                length=160,
                I_ampx=1.3*0.5/0.467,
            ),
            ConstantPulse(
                name="qubit_constant_pi2_52",
                length=52,
                I_ampx=1.36612 / 2,
            ),
            ConstantPulse(
                name="qubit_constant_pi_320",
                length=320,
                I_ampx=1.3*0.5/0.467/2*0.5/0.446,
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