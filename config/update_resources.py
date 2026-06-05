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
        
        rr_LO = 7.668e9+50e6#+0.5e6 
        rr_IF = -50.8e6#-50e6 
        
        qubit_LO = 5e9+200e6+50e6-400e6-200e6#5.7e9+50e6-150E6
        qubit_IF = 121.62e6+120e3#-80e6+1.62e6+200e6
        
        cav_LO = 6.659e9+50e6+118e3
        cav_IF = -68.2e6
        
        qubitEF_IF = -80e6#-23.8e6 #-118e6# -76e6
        qubitGF2_IF = 25e6#59.5e6 #3.2e6 no stark shift #stark shift 59.5e6
        drive_LO = 2.4e9 #2.7092
        drive_IF = -113e6#-244e6#-40e6 #-55.95e6 #-43.8e6# -76e6  -92e6#

        
        settings = {
                "controllers": {
                    "con1": {
                        "fems": {
                            1: {
                                "analog_outputs": {
                                    1: {
                                        "full_scale_power_dbm": 16, #only in increments of 3s -11
                                        "upconverters": {1: {"frequency":  rr_LO}},
                                        "band":3,
                                    },
   
                                    3: {
                                        "full_scale_power_dbm": 4, 
                                        "upconverters": {1: {"frequency": qubit_LO}},
                                        "band":2,
                                    },
                                    6: {
                                        "full_scale_power_dbm": 16, #-11 to 16
                                        "upconverters": {1: {"frequency": drive_LO}},
                                        "band":1,
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
                                    4: {
                                        "full_scale_power_dbm": 4, #if rt amp, max 4
                                        "upconverters": {1: {"frequency": cav_LO}},
                                        "band":2,
                                    },
                                    # 1: {
                                    #     "full_scale_power_dbm": -1, #-5,
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
                "I": [1,1], "out1": [1,1] 
            },  # OPX has two separate inputs (I, Q), from the Octave
            # ports={"I": 1, "Q": 2, "out": 1}, # OPX has I,Q combined in 1 input, from Labbrick downconversion
            upconverter = 1,
            int_freq=rr_IF,
            tof= 200+107, 
            rf_switch=None,
            rf_switch_on=False,
        )

        rr.operations = [
            ConstantPulse(
                name="rr_constant_pulse",
                length=1000,
                I_ampx=0.1*0.3,
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
                length=64*15,#3,#400,#
                I_ampx=0.015,#.02, #0.03
                pad=64*1,#*8,#300,#64*12, #1200, #
                digital_marker=DigitalWaveform("ADC_ON"),
                weights="C:\\Users\\qcrew\Desktop\\Juncheng\\victoria\\config\\weights\\20260604_150624_weights.npz",
            ),
        ]
        
        drive.configure(
            name="drive",
            lo_name="opx1000",
            ports={"I": [1,6]},
            upconverter = 1,
            int_freq=drive_IF,
            rf_switch=None,
            rf_switch_on=False,
        )
        
        drive.operations = [
            
        GaussianPulse(
                name="drive_gaussian_pi_24",
                sigma=6,
                chop=4,
                I_ampx=1.95,#*0.5/0.426,
                Q_ampx=0.0,
            ),
        ConstantPulse(
                name="drive_constant_400",
                length=160,
                I_ampx=.9,#0.247/10000*52,
            ),
        ConstantPulse(
                name="drive_constant_fock1",
                length=60,
                I_ampx=.9,#0.247/10000*52,
            ),
        ConstantPulse(
                name="drive_constant_fock1_16",
                length=16,
                I_ampx=1,#0.247/10000*52,
            ),
        ConstantPulse(
                name="drive_constant_SS",
                length=6*4,
                I_ampx=1,#0.247/10000*52,
            ),
        ]

        qubit.configure(
            name="qubit",
            lo_name="opx1000",
            ports={"I": [1,3]},
            upconverter = 1,
            int_freq=qubit_IF,
            rf_switch=None,
            rf_switch_on=False,
        )

        qubit.operations = [
            ConstantPulse(
                name="qubit_constant_pulse",
                length=240,
                I_ampx=1*0.5/0.58/4,#0.247/10000*52,
            ),
           
            
            GaussianPulse(
                name="qubit_gaussian_pi_24",
                sigma=6,
                chop=4,
                I_ampx=0.16*.5/.24*.5/.477*.5/.284*.5/.51,
                Q_ampx = -0.165,
            ),
            GaussianPulse(
                name="qubit_gaussian_pi2_24",
                sigma=6,
                chop=4,
                I_ampx=0.16*.5/.24*.5/.477*.5/.284*.5/.51/2,
                Q_ampx = -0.165,
            ),
            GaussianPulse(
                name="qubit_gaussian_pi_48",
                sigma=12,
                chop=4,
                I_ampx=0.16*.5/.24*.5/.477*.5/.284*.5/.51/2*0.5/0.54/1.04
                # Q_ampx = 1*-0.159,
            ),
            GaussianPulse(
                name="qubit_gaussian_pi_160",
                sigma=48,
                chop=4,
                I_ampx=0.16*.5/.24*.5/.477*.5/.284*.5/.51/2*0.5/0.54/1.04/2/2
                # Q_ampx = 1*-0.159,
            ),
            GaussianPulse(
                name="qubit_gaussian_pi_240",
                sigma=60*15,
                chop=4,
                I_ampx=0.06712*48/60/15
                # Q_ampx = 1*-0.159,
            ),
            GaussianPulse(
                name="qubit_gaussian_pi_360",
                sigma=90,
                chop=4,
                I_ampx=0.349/20*.5/.35*90/120
                # Q_ampx = 1*-0.159,
            ),
            GaussianPulse(
                name="qubit_gaussian_pi_1200",
                sigma=320,
                chop=4,
                I_ampx=1.8*0.5/1.47*0.5/2/6*0.5/0.47*0.5/0.4*0.5/0.59
                # Q_ampx = 1*-0.159,
            ),
            GaussianPulse(
                name="qubit_gaussian_pi_2000",
                sigma=520,
                chop=4,
                I_ampx=0.019*0.5/0.471
                # Q_ampx = 1*-0.159,
            ),
            GaussianPulse(
                name="qubit_spec_1600",
                sigma=400,
                chop=4,
                I_ampx=1
                # Q_ampx = 1*-0.159,
            ),
            GaussianPulse(
                name="qubit_spec_40",
                sigma=40,
                chop=4,
                I_ampx=0.5
                # Q_ampx = 1*-0.159,
            ),
            ConstantPulse(
                name="qubit_constant_1200",
                length=1200,
                I_ampx=1*0.5/0.58*0.5/2.63/2,#0.247/10000*52,
            ),
        
            RampedConstantPulse(
                name="qubit_cos_ramp_pulse",
                ramp=10,
                rampfn="cos",
                length=20,
                I_ampx=1.4,
            ),

        ]
        
        
        cav.configure(
            name="cavity",
            lo_name="opx1000",
            ports={"I": [1,4]},
            upconverter = 1,
            int_freq=cav_IF,
            rf_switch=None, #alice_rf,
            rf_switch_on=False,
        )
        
        cav.operations = [
            GaussianPulse(
                name="cav_gaussian_pulse_60",
                sigma=60,
                chop=4,
                I_ampx=1.95,
                Q_ampx=0.0,
            ),
            GaussianPulse(
                name="cav_gaussian_pulse_100",
                sigma=100,
                chop=4,
                I_ampx=1.1,
                Q_ampx=0.0,
            ),
            ConstantPulse(
                name="cav_constant_pulse",
                length=100000,
                I_ampx=1.95,
            ),
          
            ConstantPulse(
                name="cav_constant_200",
                length=200,
                I_ampx=1.3,
            ),
            ConstantPulse(
                name="cav_constant_1000",
                length=1000,
                I_ampx=1/5,
            ),
             ConstantPulse(
                name="cav_spec_2000",
                length=2000,
                I_ampx=1/10,
            ),
            # ConstantPulse(
            #     name="cav_constant_200",
            #     length=200,
            #     I_ampx=1,
            # ),    
            # ConstantPulse(
            #     name="cav_constant_60",
            #     length=80,
            #     I_ampx=1,
            # ),    
            ConstantPulse(
                name="cav_constant_40",
                length=40,
                I_ampx=1.95,
            ),
            ConstantPulse(
                name="cav_constant_180",
                length=180,
                I_ampx=1.3*0.52/0.5,
            ),
            ConstantPulse(
                name="cav_constant_40_amp1",
                length=40,
                I_ampx=1,
            ),
            ConstantPulse(
                name="cav_constant_64",
                length=64,
                I_ampx=1,
            ),
            ConstantPulse(
                name="cav_constant_240",
                length=240,
                I_ampx=1.95,
            ),
        ]
        
        qubit_EF.configure(
            name="qubit_EF",
            lo_name="opx1000",
            ports={"I": [1,3]},
            upconveter = 1,
            int_freq=qubitEF_IF,
            rf_switch=None,
            rf_switch_on=False,
        )

        qubit_EF.operations = [

            GaussianPulse(
                name="qubitEF_gaussian_pi_16",
                sigma=4,
                chop=4,
                I_ampx=0.3082,
                Q_ampx=0.0,
            ),
            GaussianPulse(
                name="qubitEF_gaussian_pi_24",
                sigma=6,
                chop=4,
                I_ampx=1.5*0.5/1.43*0.5/0.515*0.5/2.2*.5/.57*.5/.245*.5/.47*0.5/0.296,#*0.5/0.426,
                Q_ampx=0.0,
            ),
            
            
            GaussianPulse(
                name="qubitEF_gaussian_pulse_300",
                sigma=300,
                chop=4,
                I_ampx=1.38*0.5/0.32,
                Q_ampx=0.0,
            ),
        ]
        
        qubit_GF2.configure(
            name="qubit_GF2",
            lo_name="opx1000",
            ports={"I": [1,3]},
            upconveter = 1,
            int_freq=qubitGF2_IF,
            rf_switch=None,
            rf_switch_on=False,
        )

        qubit_GF2.operations = [
            GaussianPulse(
                name="qubitGF2_gaussian_pi_16",
                sigma=4,
                chop=4,
                I_ampx=0.2*0.5/0.167*0.6*0.5/0.555*0.5/0.492,
                Q_ampx=0.0,
            ),
            GaussianPulse(
                name="qubitGF2_gaussian_pi_24",
                sigma=6,
                chop=4,
                I_ampx=0.371*.5/.2*.87*.5/.2*.5/.72*.5/.512,#*0.5/0.426,
                Q_ampx=0.0,
            ),
            GaussianPulse(
                name="qubitGF2_gaussian_pulse_300",
                sigma=300,
                chop=4,
                I_ampx=1.38*0.5/0.32,
                Q_ampx=0.0,
            ),
        ]