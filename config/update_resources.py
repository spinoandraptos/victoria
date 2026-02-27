""" """

from qcore.helpers import Stage
from qcore.modes import *
from qcore.pulses import *
from qcore.pulses.clear_readout_pulse import ClearReadoutPulse

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
        
        # (opx1000, qubit, rr, cavity, yoko, snail,cavity_m, rr_MR) = stage.get("opx1000", "qubit", "rr", "cavity", "yoko2", "snail", "cavity_m", "rr_MR")
        (opx1000, qubit, rr, cavity, yoko, snail,cavity_m) = stage.get("opx1000", "qubit", "rr", "cavity", "yoko2", "snail", "cavity_m")
        
        yoko.output=True
        yoko.ramp(0e-3, step=1e-4)
    
        rr_LO =  3.916631000E9-0.4E6#3.868364e9+50e6-1.443e6+1.5e6-0.17e6-0.24e6-0.42e6-0.32e6-0.24e6-0.4E6
        
        # The ones below are for IF at -50e6
        #0mA 3.918421000e9
        #20mA 3.918421000e9
        #40mA 3.918251000e9
        #60mA 3.918011000e9
        #80mA 3.917591000e9
        #90mA 3.917271000e9
        #100mA 3.917031000e9
        #110mA 3.916631000E9
        #120mA 3.916231000

        rr_IF = -50e6

        cav_LO = 3e9 #6.7e9 + 53.4e6+19e6-2E6-2E6-4.9e6-0.3e6 #6.6e9+50e6                                                                                                                                           
        cav_IF = -50e6
        
        
        # rr_MR_LO = 3.868364e9+50e6-1.443e6#3.86842E9+50E6+13.2e6 #7.736728e9+50e6+50e6#
        # rr_MR_IF = -50e6
        
        
        qubit_LO = 5.862E9-400E6#6.5e9-250e6+70e6+45e6+2e6+110e6-10e6-130e6-190e6-80e6-130e6-30e6-15e6-30e6#+72e6+58e6
        # qubit_LO = 4.53e9+50e6#6e9+96.7e6+250e6-11e6+0.1e6
        qubit_IF = -20e6
        
        # qubit_LO = 5.8e9
        # # qubit_LO = 5e9
        # qubit_IF = 57.608e6 +0.005e6
        
      
        
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
                                        "band":1
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
                                        "full_scale_power_dbm": 16, #7
                                        "upconverters": {1: {"frequency": qubit_LO}},
                                        "band":1
                                    },
                                    # 8: {
                                    #     "full_scale_power_dbm": -11, #-5, 16, #
                                    #     "upconverters": {1: {"frequency": rr_MR_LO}},
                                    # },
                                },
                                "analog_inputs": {
                                    1: {
                                        "downconverter_frequency": rr_LO,
                                        "band":1 #3
                                        },  # for down-conversion
                                    # 2: {
                                    #     "downconverter_frequency": rr_MR_LO,
                                    #     "band":1
                                    #     },  # for down-conversion
                
                                },
                            },
                            
                        } 
                    }
                }
            }      
        opx1000.settings = settings
        # rr_MR.configure(
        #     name="rr_MR",
        #     lo_name="opx1000",  # either octave or labbrick
        #     ports={
        #         "I": [2,8], "out1": [2,2] # [2, 1],[2,1]
        #     },  # OPX has two separate inputs (I, Q), from the Octave
        #     # ports={"I": 1, "Q": 2, "out": 1}, # OPX has I,Q combined in 1 input, from Labbrick downconversion
        #     int_freq=rr_MR_IF,
        #     tof=300,#264+36,
        #     rf_switch=None,
        #     rf_switch_on=False,
        # )
        


        # rr_MR.operations = [
        #     ConstantPulse(
        #         name="rr_MR_constant_pulse",
        #         length=1000,
        #         I_ampx=0.4,
        #     ),
        #     GaussianPulse(
        #         name="rr_MR_gaussian_pulse",
        #         sigma=100,
        #         chop=6,
        #         I_ampx=1.0,
        #         Q_ampx=0.0,
        #     ),
        #     ConstantReadoutPulse(
        #         name="rr_MR_readout_pulse",
        #         length=1000,  # 2000,
        #         I_ampx=0.2,
        #         pad=600, #1200, #
        #         digital_marker=DigitalWaveform("ADC_ON"),
        #         # weights=r"C:\Users\qcrew\Documents\eunice\config\weights\20260223_105919_weights.npz"
        #     ),
        #     # ConstantReadoutPulse(
        #     #     name="rr_MR_readout_pulse",
        #     #     length=1000,  # 2000,
        #     #     I_ampx=1.7,
        #     #     pad=600, #1200, #
        #     #     digital_marker=DigitalWaveform("ADC_ON"),
        #     #     # weights=r"C:\Users\qcrew\Documents\eunice\config\weights\20260223_105919_weights.npz"
        #     # ),
        # ]
        
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
                length=600,  # 2000,
                I_ampx=0.2,
                pad=600, #1200, #
                digital_marker=DigitalWaveform("ADC_ON"),
                # weights=r"C:\Users\qcrew\Documents\eunice\config\weights\20260223_105919_weights.npz"
            ),
            # ClearReadoutPulse(
            #     name="rr_CLEAR_readout_pulse",
            #     I_ampx = 0.8,
            #     Q_ampx = 0.0,
            #     length = 1106,
            #     pad = 46,
            #     ringdown1_amp = 0.4317212045970007,
            #     ringup1_amp = 2.1935413793958536,
            #     ringdown1_time = 278,
            #     ringup1_time = 194,
            #     ringdown2_amp = -0.4679171693995341,
            #     ringdown2_time = 303,
            #     ringup2_amp = 0.030386693416017317,
            #     ringup2_time = 327,
            #     drive_amp = 1.7,
            #     drive_time = 4,
            #     digital_marker=DigitalWaveform("ADC_ON"),
            # )
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
                I_ampx=1.95,
            ),
            ConstantPulse(
                name="qubit_constant_pi_52",
                length=52,
                I_ampx=1.1#1.1,
            ),
            ConstantPulse(
                name="qubit_constant_pi_104",
                length=104,
                I_ampx=1.95,
            ),
            ConstantPulse(
                name="qubit_constant_pi2_52",
                length=52,
                I_ampx=1.36612 / 2,
            ),
            ConstantPulse(
                name="qubit_constant_pi_520",
                length=520,
                I_ampx=1.95,
            ),
            ConstantPulse(
                name="qubit_constant_pi_1500",
                length=1500,
                I_ampx=0.3,
            ),
            ConstantPulse(
                name="qubit_constant_pi_260",
                length=260,
                I_ampx=1.36612/10*0.5/0.468*0.5/0.47/2*0.5/0.457*2,
            ),
            ConstantPulse(
                name="qubit_constant_pi_200",
                length=200,
                I_ampx=0.14748208571*0.5/0.35*0.5/0.37*0.5/0.6*0.5/0.663*0.5/0.477,
            ),
            GaussianPulse(
                name="qubit_gaussian_pi_200",
                chop=5,
                sigma=40,
                I_ampx=0.37601911372,
            ),
            GaussianPulse(
                name="qubit_gaussian_pi_300",
                chop=5,
                sigma=60,
                I_ampx=0.25642329086,
            ),
            GaussianPulse(
                name="qubit_gaussian_pi_400",
                chop=5,
                sigma=80,
                I_ampx=0.1940190149,
            ),
            GaussianPulse(
                name="qubit_gaussian_pi_520",
                chop=5,
                sigma=80,
                I_ampx=0.1940190149,
            ),
            GaussianPulse(
                name="qubit_gaussian_pi_clara",
                chop=4,
                sigma=8,
                I_ampx=1.634,
            ),
            GaussianPulse(
                name="qubit_gaussian_pi_clara_long",
                chop=4,
                sigma=400,
                I_ampx=0.05,
            ),
            GaussianPulse(
                name="qubit_gaussian_pi2_clara",
                chop=4,
                sigma=8,
                I_ampx=1.634/2,
            )
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
                I_ampx=1.5*0.7,#1.5*0.15,
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
        