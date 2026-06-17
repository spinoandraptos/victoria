""" """

from qcore.helpers import Stage
from qcore.modes import *
from qcore.pulses import *
from qualang_tools.units import unit
from experiment_config import MODES_CONFIG

if __name__ == "__main__":
    """ """
    with Stage(configpath=MODES_CONFIG, remote=True) as stage:
        
        # (opx1000, qubit, rr, cav, qubit_EF, qubit_GF2, drive, drive_fock, yoko1) = stage.get("opx1000", "qubit", "rr", "cavity", "qubit_EF", "qubit_GF2", "drive","drive_fock", "yoko1")
        (opx1000, qubit, rr, cav, qubit_EF, qubit_GF2, drive, drive_fock) = stage.get("opx1000", "qubit", "rr", "cavity", "qubit_EF", "qubit_GF2", "drive","drive_fock")
        u = unit(coerce_to_integer=True)
        
        rr_LO = 7.8471e9+50e6#7.726e9+50e6+0.9e6#7.415e9+50e6+0.5e6 
        rr_IF = -41.6e6 
        
        qubit_LO = 5e9+100e6#5.7e9+50e6-150E6
        qubit_IF = 133e6+1e6
                
        cav_LO = 6.71841e9+50e6#6.659e9+50e6
        cav_IF = -67.7e6
        
        qubitEF_IF = -68.8e6 #-118e6# -76e6
        qubitGF2_IF = 32.7e6#59.5e6 #3.2e6 no stark shift #stark shift 59.5e6
        drive_fock_LO = 3.56729e9+50E6
        drive_fock_IF = 71.7E6
        drive_LO = 6.71841e9+50e6-2.9e9+50e6#5.6118e9+50e6
        drive_IF =  7.92e6-5E6#

        # yoko1.output = True
        # yoko1.ramp(0e-3, step=1e-4)
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
                                    # 5: {
                                    #     "full_scale_power_dbm": 16, #-11 to 16
                                    #     "upconverters": {1: {"frequency": drive_LO}},
                                    #     "band":2,
                                    # },
                                    # 4: {
                                    #     "full_scale_power_dbm": -11, #16
                                    #     "upconverters": {1: {"frequency": alice_LO}},
                                    # },
                                    7: {
                                        "full_scale_power_dbm": 4, 
                                        "upconverters": {1: {"frequency": drive_fock_LO}},
                                        
                                    },
                                    6: {
                                        "full_scale_power_dbm": 4, 
                                        "upconverters": {1: {"frequency": drive_LO}}, # SNAIL drive
                                    },
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
            tof= 400, 
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
                length=64*4,#64*8,#400,#
                I_ampx=0.015,#0.015, #0.03
                pad=64*4,#300,#64*12, #1200, #
                digital_marker=DigitalWaveform("ADC_ON"),
                # weights="C://Users//qcrew//Desktop//Juncheng//victoria//config//weights//20260612_162253_weights.npz",
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
                length=5000,
                I_ampx=0.1,#0.247/10000*52,
            ),
           
            
            GaussianPulse(
                name="qubit_gaussian_pi_24",
                sigma=6,
                chop=4,
                I_ampx=0.454*.5/.545*.5/.51*.5/.53,
                # Q_ampx = -0.020,#*-0.159,
            ),
            GaussianPulse(
                name="qubit_gaussian_pi_240",
                sigma=6*10,
                chop=4,
                I_ampx=0.454*.5/.545*.5/.51/10*.5/.45*.5/.48,
                # Q_ampx = -0.020,#*-0.159,
            ),
            GaussianPulse(
                name="qubit_gaussian_pi_48",
                sigma=12,
                chop=4,
                I_ampx=1.99/.45*.5,
                # Q_ampx = 1#*-0.159,
            ),
            GaussianPulse(
                name="qubit_gaussian_pi2_24",
                sigma=6,
                chop=4,
                I_ampx=0.454*.5/.545*.5/.51/2*.5/.514*.5/.52*.5/.49,
                Q_ampx =-0.020,#*-0.159,
            ),
            GaussianPulse(
                name="qubit_gaussian_pi2_48",
                sigma=12,
                chop=4,
                I_ampx=1.99/.45*.5/2
                # Q_ampx = 1*-0.159,
            ),
            GaussianPulse(
                name="qubit_gaussian_pi_640",
                sigma=160,
                chop=4,
                I_ampx=1.5*0.5/0.566*0.5/0.505*0.5/1.41/160*6
                # Q_ampx = 1*-0.159,
            ),
            GaussianPulse(
                name="qubit_gaussian_pi_1200",
                sigma=320,
                chop=4,
                I_ampx=0.454*.5/.545*.5/.51/1200*24
                # Q_ampx = 1*-0.159,
            ),
            GaussianPulse(
                name="qubit_gaussian_pi_2000",
                sigma=520,
                chop=4,
                I_ampx=1.99/.45*.5 /320*12/.46*.5/.53*.5*320/520/.47*.5
                # Q_ampx = 1*-0.159,
            ),
            GaussianPulse(
                name="qubit_spec_1600",
                sigma=400,
                chop=4,
                I_ampx=1
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
                name="cav_constant_300",
                length=300,
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
            ConstantPulse(
                name="cav_constant_120",
                length=120,
                I_ampx=1.3,
            ),    
            ConstantPulse(
                name="cav_constant_40",
                length=40,
                I_ampx=1,
            ),
            ConstantPulse(
                name="cav_constant_64",
                length=64,
                I_ampx=1.5,
            ),
            ConstantPulse(
                name="cav_constant_200",
                length=200,
                I_ampx=1.3,
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
                I_ampx=1.5*0.5/1.43*0.5/0.515*0.5/0.914/.53*.5,#*0.5/0.426,
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
                I_ampx=1*.5/.4,
                Q_ampx=0.0,
            ),
            GaussianPulse(
                name="qubitGF2_gaussian_pi_24",
                sigma=6,
                chop=4,
                I_ampx=2.0,#*0.5/0.426,
                Q_ampx=0.0,
            ),
            GaussianPulse(
                name="qubitGF2_gaussian_pi_192",
                sigma=48,
                chop=4,
                I_ampx=2.0,#*0.5/0.426,
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
        GaussianPulse(
                name="drive_gaussian_pi_100",
                sigma=25,
                chop=4,
                I_ampx=1.95,#*0.5/0.426,
                Q_ampx=0.0,
            ),
        ConstantPulse(
                name="drive_constant_192",
                length=4*48,
                I_ampx=2,#0.247/10000*52,
            ),
        ConstantPulse(
                name="drive_constant_400",
                length=400,
                I_ampx=1,#0.247/10000*52,
            ),
        ConstantPulse(
                name="drive_constant_2000",
                length=2000,
                I_ampx=.8,#0.247/10000*52,
            ),
        ConstantPulse(
                name="drive_constant_52",
                length=52,
                I_ampx=.8,#0.247/10000*52,
            ),
        ConstantPulse(
                name="drive_constant_600",
                length=600,
                I_ampx=1,#0.247/10000*52,
            ),
        ConstantPulse(
                name="drive_constant_5000",
                length=5000,
                I_ampx=2,#0.247/10000*52,
            ),
        ConstantPulse(
                name="drive_constant_fock1",
                length=60,
                I_ampx=.9,#0.247/10000*52,
            ),
        ConstantPulse(
                name="drive_constant_SS",
                length=6*4,
                I_ampx=1,#0.247/10000*52,
            ),
        ]
        
        drive_fock.configure(
            name="drive_fock",
            lo_name="opx1000",
            ports={"I": [1,7]},
            upconverter = 1,
            int_freq=drive_fock_IF,
            rf_switch=None,
            rf_switch_on=False,
        )
        
        drive_fock.operations = [
            
        ConstantPulse(
                name="drive_constant_2000",
                length=2000,
                I_ampx=2,#0.247/10000*52,
            ),
        ]
