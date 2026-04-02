""" """

from qcore.helpers import Stage
from qcore.modes import *
from qcore.pulses import *
from qualang_tools.units import unit
from experiment_config import MODES_CONFIG

if __name__ == "__main__":
    """ """
    with Stage(configpath=MODES_CONFIG, remote=True) as stage:
        
        (opx1000, qubit, rr, cav, qubit_EF, qubit_GF2, drive) = stage.get("opx1000", "qubit", "rr", "cavity", "qubit_EF", "qubit_GF2", "drive")
        u = unit(coerce_to_integer=True)
        
        rr_LO = 7.88067e9+50e6 
        rr_IF = -50e6
        
        qubit_LO = 6.135e9 #6.285e9+50e6-200e6
        qubit_IF = 122e6# 123.2e6# -76e6
        
        qubitEF_IF = -118e6# -76e6
        qubitGF2_IF = 2.28e6#59.5e6 #3.2e6 no stark shift #stark shift 59.5e6
        drive_LO =5.6118e9+50e6
        drive_IF =-44e6#-40e6 #-55.95e6 #-43.8e6# -76e6  -92e6#
        
        cav_LO = 6.7684e9 # 6.7184e9+50e6
        cav_IF = -108e6
        
        settings = {
                "controllers": {
                    "con1": {
                        "fems": {
                            8: {
                                "analog_outputs": {
                                    1: {
                                        "full_scale_power_dbm": 16, #only in increments of 3s -11
                                        "upconverters": {1: {"frequency":  rr_LO}},
                                        "band":3,
                                    },
   
                                    4: {
                                        "full_scale_power_dbm": 16, 
                                        "upconverters": {1: {"frequency": qubit_LO}},
                                        "band":2,
                                    },
                                    5: {
                                        "full_scale_power_dbm": 16, #-11 to 16
                                        "upconverters": {1: {"frequency": drive_LO}},
                                        "band":2,
                                    },
                                    # 4: {
                                    #     "full_scale_power_dbm": -11, #16
                                    #     "upconverters": {1: {"frequency": alice_LO}},
                                    # },
                                    # 5: {
                                    #     "full_scale_power_dbm": 16, 
                                    #     "upconverters": {1: {"frequency": qubit_LO}},
                                    #     "band":2,
                                    # },
                                    # 6: {
                                    #     "full_scale_power_dbm": 16, 
                                    #     "upconverters": {1: {"frequency": qubit_LO}},
                                    # },
                                    2: {
                                        "full_scale_power_dbm": 16, 
                                        "upconverters": {1: {"frequency": cav_LO}},
                                        "band":3,
                                    },
                                    # 8: {
                                    #     "full_scale_power_dbm": -8, #-5,
                                    #     "upconverters": {1: {"frequency": rr_LO}},
                                    # },
                                },
                                "analog_inputs": {
                                    2: {
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
                "I": [8,1], "out1": [8,2] 
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
                I_ampx=0.1*0.25,
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
                length=64*9,#400,#
                I_ampx=0.03, #0.03
                pad=64*1,#300,#64*12, #1200, #
                digital_marker=DigitalWaveform("ADC_ON"),
                weights = r"C:\Users\qcrew2\Documents\Candace\eunice\config\weights\20260401_135509_weights.npz",
            ),
        ]
        

        qubit.configure(
            name="qubit",
            lo_name="opx1000",
            ports={"I": [8,4]},
            int_freq=qubit_IF,
            rf_switch=None,
            rf_switch_on=False,
        )

        qubit.operations = [
            ConstantPulse(
                name="qubit_constant_pulse",
                length=10000,
                I_ampx=1.95*0.001,#0.247/10000*52,
            ),
            ConstantPulse(
                name="qubit_constant_pi_160",
                length=160,
                I_ampx=0.1,
            ),
            ConstantPulse(
                name="qubit_constant_pi_52",
                length=52,
                I_ampx=0.27*0.5/0.66*0.5/0.6*0.5/0.36*0.5/0.478*0.5/0.59*0.5,#1*0.5/0.338*0.2,
            ),
            ConstantPulse(
                name="qubit_constant_pi_16",
                length=16,
                I_ampx=0.08*0.5/0.56,
            ),
            GaussianPulse(
                name="qubit_gaussian_pi_16",
                sigma=4,
                chop=4,
                I_ampx=0.12*0.5/0.513*15*0.5/0.4*0.5/0.512,#*0.5/0.426,
            ),
            GaussianPulse(
                name="qubit_gaussian_pi2_16",
                sigma=4,
                chop=4,
                I_ampx=0.12/2,#*0.5/0.426,
            ),
            ConstantPulse(
                name="qubit_constant_pi2_16",
                length=16,
                I_ampx=0.08*0.5/0.56/2,
            ),
            ConstantPulse(
                name="qubit_constant_pi2_52",
                length=52,
                I_ampx=0.27*0.5/0.66*0.5/0.6*0.5/0.36*0.5/0.478*0.5/0.59/2*0.5/0.51,
            ),
            ConstantPulse(
                name="qubit_constant_pi_300",
                length=300,
                I_ampx=0.08*0.5/0.56/300*16,#1*0.5/0.338*0.2,
            ),
            
            ConstantPulse(
                name="qubit_constant_pi_200",
                length=200,
                I_ampx=0.08*0.5/0.56/300*16/300*200,#1*0.5/0.338*0.2,
            ),
            ConstantPulse(
                name="qubit_constant_pi_300_strong",
                length=300,
                I_ampx=2.3,#1*0.5/0.338*0.2,
            ),
            ConstantPulse(
                name="qubit_constant_pi_400",
                length=400,
                I_ampx=0.04245827766,#1*0.5/0.338*0.2,
            ),
            ConstantPulse(
                name="qubit_constant_pi_600",
                length=600,
                I_ampx=0.04245827766*400/600*0.5/0.441,#1*0.5/0.338*0.2,
            ),
            ConstantPulse(
                name="qubit_constant_pi_700",
                length=700,
                I_ampx=0.04245827766*400/600*0.5/0.441*600/700,#1*0.5/0.338*0.2,
            ),
            ConstantPulse(
                name="qubit_constant_pi_1000",
                length=1000,
                I_ampx=0.04245827766*400/600*0.5/0.441*600/1000,#1*0.5/0.338*0.2,
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
                name="qubit_gaussian_pi_300",
                sigma=300,
                chop=4,
                I_ampx=0.032*10,
                Q_ampx=0.0,
            ),
            RampedConstantPulse(
                name="qubit_cos_ramp_pulse",
                ramp=10,
                rampfn="cos",
                length=20,
                I_ampx=1.4,
            ),
             GaussianPulse(
                name="qubit_gaussian_pi_64",
                sigma=16,
                chop=4,
                I_ampx=0.05*0.5/1.03,#*0.5/0.426,
                Q_ampx=0.0,
            ),
        ]
        
        qubit_EF.configure(
            name="qubit_EF",
            lo_name="opx1000",
            ports={"I": [8,4]},
            int_freq=qubitEF_IF,
            rf_switch=None,
            rf_switch_on=False,
        )

        qubit_EF.operations = [
            ConstantPulse(
                name="qubit_constant_pulse",
                length=10000,
                I_ampx=1.95*0.25,#0.247/10000*52,
            ),
            ConstantPulse(
                name="qubit_constant_pi_160",
                length=160,
                I_ampx=0.1,
            ),
            ConstantPulse(
                name="qubitEF_constant_pi_52",
                length=52,
                I_ampx=0.21*1.5*0.5/0.961*0.5/0.516,#1*0.5/0.338*0.2,
            ),
            ConstantPulse(
                name="qubitEF_constant_pi_16",
                length=16,
                I_ampx=0.06*0.5/0.68,#1*0.5/0.338*0.2,
            ),
            GaussianPulse(
                name="qubitEF_gaussian_pi_16",
                sigma=4,
                chop=4,
                I_ampx=2.0*0.5/0.736,#*0.5/0.426,
            ),
 
        ]
        drive.configure(
            name="drive",
            lo_name="opx1000",
            ports={"I": [8,5]},
            int_freq=drive_IF,
            rf_switch=None,
            rf_switch_on=False,
        )

        drive.operations = [

            ConstantPulse(
                name="drive_constant_pi_72",
                length=72,
                I_ampx=1.95,#1*0.5/0.338*0.2,
            ),
            ConstantPulse(
                name="drive_constant_pi_300",
                length=300,
                I_ampx=1.95,#1*0.5/0.338*0.2,
            ),
            ConstantPulse(
                name="drive_constant_pi_200",
                length=200,
                I_ampx=1.95*0.1,#1*0.5/0.338*0.2,
            ),
            ConstantPulse(
                name="drive_constant_pi_16",
                length=16,
                I_ampx=1.95#0.052,
            ),
            GaussianPulse(
                name="drive_gaussian_pi_64",
                sigma=16,
                chop=4,
                I_ampx=0.05*0.5/1.03*6,
                Q_ampx=0.0,
            ),
            RampedConstantPulse(
                name="drive_ramp_pi_96",
                ramp = 8,
                length = 80,
                I_ampx = 1.95,         
            ),
            RampedConstantPulse(
                name="drive_ramp_pi_300",
                ramp = 8,
                length = 284,
                I_ampx = 1.95,         
            ),
            RampedConstantPulse(
                name="drive_ramp_pi_400",
                ramp = 8,
                length = 384,
                I_ampx = 1.95,         
            ),
            GaussianPulse(
                name="drive_gaussian_pulse_300",
                sigma=300,
                chop=4,
                I_ampx=1.95,
                Q_ampx=0.0,
            ),
           
        ]
        
        cav.configure(
            name="cavity",
            lo_name="opx1000",
            ports={"I": [8,2]},
            int_freq=cav_IF,
            rf_switch=None, #alice_rf,
            rf_switch_on=False,
        )
        
        cav.operations = [
                ConstantPulse(
                name="cav_constant_10000",
                length=10000,
                I_ampx=1.95,
            ),
                ConstantPulse(
                name="cav_constant_100",
                length=100,
                I_ampx=1,
            ),
            ConstantPulse(
                name="cav_constant_40",
                length=40,
                I_ampx=1.5*0.2/3*1.5,
            ),
        ]
        
        qubit_GF2.configure(
            name="qubit_GF2",
            lo_name="opx1000",
            ports={"I": [8,4]},
            int_freq=qubitGF2_IF,
            rf_switch=None,
            rf_switch_on=False,
        )

        qubit_GF2.operations = [
            ConstantPulse(
                name="qubitGF_constant_pi_16",
                length=16,
                I_ampx=1.95#0.052,
            ),
            ConstantPulse(
                name="qubitGF_constant_pi_20",
                length=20,
                I_ampx=0.06,#1*0.5/0.338*0.2,
            ),

            ConstantPulse(
                name="qubitGF_constant_pi_300",
                length=300,
                I_ampx=0.04*0.5/0.45*10,#1*0.5/0.338*0.2,
            ),
            GaussianPulse(
                name="qubitGF_gaussian_pi_16",
                sigma=4,
                chop=4,
                I_ampx=0.2*0.5/0.167*0.6*0.5/0.555*0.5/0.492,
                Q_ampx=0.0,
            ),
            GaussianPulse(
                name="qubitGF_gaussian_pi_24",
                sigma=24,
                chop=4,
                I_ampx=2.0,#*0.5/0.426,
                Q_ampx=0.0,
            ),
            GaussianPulse(
                name="qubitGF_gaussian_pulse_300",
                sigma=300,
                chop=4,
                I_ampx=1.38*0.5/0.32,
                Q_ampx=0.0,
            ),
        ]