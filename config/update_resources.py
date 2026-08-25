""" """

from qcore.helpers import Stage
from qcore.modes import *
from qcore.pulses import *
from qualang_tools.units import unit
from experiment_config import MODES_CONFIG

if __name__ == "__main__":
    """ """
    with Stage(configpath=MODES_CONFIG, remote=True) as stage:
        
        # (opx1000, qubit, rr, cav, qubit_EF, qubit_GF2, drive, yoko1, snail_drive, snail_drive_EF,fock_drive) = stage.get("opx1000", "qubit", "rr", "cavity", "qubit_EF", "qubit_GF2", "drive","yoko1", "snail_drive", "snail_drive_EF","fock_drive")
        (opx1000, yoko1, qubit, rr, cav, qubit_EF, qubit_GF2, snail_drive,fock_drive,snail_stark_drive) = stage.get("opx1000", "yoko1", "qubit", "rr", "cavity", "qubit_EF", "qubit_GF2", "snail_drive","fock_drive","snail_stark_drive")
        u = unit(coerce_to_integer=True)
        
        rr_LO = 7.61e9+50e6+2.9e6-0.05e6 #7.415e9+50e6+0.5e6 
        rr_IF = -50e6
        # rr_LO = 7.773e9+50e6#7.415e9+50e6+0.5e6 
        # rr_IF = -49.7e6
        
        # rr_LO = 3.88e9+50e6#7.415e9+50e6+0.5e6 
        # rr_IF = -55.6e6
        
        # rr_LO = 3.7e9+50e6#5.6118e9+50e6 #fock
        # rr_IF = -50e6#124e6#-40e6 #-55.95e6 #-43.8e6# -76e6  -92e6#
        
        qubit_LO = 4.8e9-250e6-250e6-14e6-300e3#5.6e9+50e6-400e6#+50e6+800e6#5.7e9+50e6-150E6
        qubit_IF = 50e6
        
        # qubit_LO =  6.659e9+50e6#6.659e9+50e6+1e8 #-800e6-800e6-800e6#5.6118e9+50e6
        # qubit_IF = 9.8e7#-2.9e8#5.9e7 #-2.643e8#124.15e6+1e3#-40e6 #-55.95e6 #-43.8e6# -76e6  -92e6#
        
        cav_LO = 2.9e9 + 50e6 + 25.2e6-94e3+9.51e3+52e3/2
        cav_IF = -50e6 # at 3.5mA
        # cav_IF = -33.7e6 # at 5mA
        # cav_IF = -34.0e6 # at 4.5mA
        #cav_IF = -34.56e6 # at 4mA
        # cav_IF = -36.8e6 # at 3mA
        # cav_IF = -40.2e6 # at 2.5mA
        # cav_IF = -45.1e6 # at 2.2mA
        # cav_IF = -47.7e6 # at 2.1mA
        # cav_IF = -51.6e6 # at 2mA
        # cav_IF = -33.3e6 # at 6mA
        #cav_IF = -26e6 #-94.6e6#-6.3762e7#-1.365e8#-6.1813e7 #-1.365e8#-1.0608e8#-9.7255e7#-1.365e8#-6.1813e7#-93e6-380e3+60e3 #-52.6e6
        
        qubitEF_IF = 22e6 #-118e6# -76e6
        qubitGF2_IF = 115e6#59.5e6 #3.2e6 no stark shift #stark shift 59.5e6
        
        # drive_LO = 3.7e9+50e6#5.6118e9+50e6 #fock
        # drive_IF = 124e6#-40e6 #-55.95e6 #-43.8e6# -76e6  -92e6#
        
        # fock_drive_LO = 4.1046e9+50e6 #3e9-800e6#2.4e9#5.6118e9+50e6 #fock
        # fock_drive_IF = -50e6#-40e6 #-55.95e6 #-43.8e6# -76e6  -92e6#
        #three tnoe cavity spec Malaysia
        fock_drive_LO = 2.897e9+50e6
        fock_drive_IF = -9.88e6
        
        # drive_LO = 7.6556e9+50e6#7.415e9+50e6+0.5e6 
        # drive_IF = -45.6e6
        # snail_drive_LO = 3.676E9+50e6#-800e6#5.6118e9+50e6 #fock
        snail_drive_LO = 6.61e9 + 50e6
        snail_drive_IF = -90e6#-40e6 #-55.95e6 #-43.8e6# -76e6  -92e6#
        
        snail_stark_drive_LO = 3.7e9+50e6 #3e9-800e6#2.4e9#5.6118e9+50e6 #fock
        snail_stark_drive_IF = -50e6
        
        # SNAIL_drive_LO =  6.659e9+50e6#6.659e9+50e6+1e8 #-800e6-800e6-800e6#5.6118e9+50e6
        # SNAIL_drive_IF = 9.8e7#-2.9e8#5.9e7 #-2.643e8#124.15e6+1e3#-40e6 #-55.95e6 #-43.8e6# -76e6  -92e6#
        
        # SNAIL_drive_LO = 6.659e9+50e6+350e6#-400E6-400e6#3.7e9+50e6#6.659e9+50e6#3.7e9+50e6#5.6118e9+50e6
        # SNAIL_drive_IF = -188e6#-40e6 #-55.95e6 #-43.8e6# -76e6  -92e6#
        # SNAIL_drive_EF_IF = 5e7
        
        # drive_LO = SNAIL_drive_LO#2.4e9#5.6118e9+50e6
        # drive_IF = -129e6#-40e6 #-55.95e6 #-43.8e6# -76e6  -92e6#
        
      

        yoko1.output = True
        yoko1.ramp(0e-3, step=1e-4) #-0.0125
        

        
        settings = {
                "controllers": {
                    "con1": {
                        "fems": {
                            1: {
                                "analog_outputs": {
                                    
                                    1: {
                                        "full_scale_power_dbm": 4, 
                                        "upconverters": {1: {"frequency": snail_stark_drive_LO}},
                                        "band":1,
                                    },
                                    
                                    2: {
                                        "full_scale_power_dbm": 4, 
                                        "upconverters": {1: {"frequency": fock_drive_LO}},
                                        "band":1,
                                    },
                                    3: {
                                        "full_scale_power_dbm": -2, #16
                                        "upconverters": {1: {"frequency": rr_LO}},
                                        "band":3,
                                    },
                                    
                                    4: {
                                        "full_scale_power_dbm": 4, #only in increments of 3s -11
                                        "upconverters": {1: {"frequency":  cav_LO}},
                                        "band":1,
                                    },
                                    # 5: {
                                    #     "full_scale_power_dbm": 4, 
                                    #     "upconverters": {1: {"frequency": snail_drive_LO}},
                                    #     "band":2,
                                    # },
                                    
                                    6: {
                                        "full_scale_power_dbm": 8, #4 for rrB
                                        "upconverters": {1: {"frequency": qubit_LO}},
                                        "band":2
                                    },
                                },
                                "analog_inputs": {
                                    1: {
                                        "downconverter_frequency": rr_LO,
                                        "band":3
                                        },  # for down-conversion
                                    
                
                                },
                            },
                            
                            # 8: {
                            #     "analog_outputs": {
                            #         6: {
                            #             "full_scale_power_dbm": 8, #4 for rrB
                            #             "upconverters": {1: {"frequency": qubit_LO}},
                            #             "band":2
                            #         },
   
                            #     },
                               
                            # },
                            
                        } 
                    }
                }
            } 
             
        opx1000.settings = settings
        
        rr.configure(
            name="rr",
            lo_name="opx1000",  # either octave or labbrick
            ports={
                "I": [1,3], "out1": [1,1] 
            },  # OPX has two separate inputs (I, Q), from the Octave
            # ports={"I": 1, "Q": 2, "out": 1}, # OPX has I,Q combined in 1 input, from Labbrick downconversion
            upconverter = 1,
            int_freq=rr_IF,
            tof= 360+46, 
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
                I_ampx=0.23,
                Q_ampx=0.0,
            ),
            # ConstantReadoutPulse(
            #         name="rr_readout_pulse",
            #         length=64*12,#64*8,#400,#
            #         I_ampx=1,#0.05*0.7*.8*.8*.6, #0.03
            #         pad=64*10,#300,#64*12, #1200, #
            #         digital_marker=DigitalWaveform("ADC_ON"),
            #         # weights="C:\\Users\\qcrew\\Desktop\\Juncheng\\victoria\\config\\weights\\20260724_161936_weights.npz",
            #     ),
            ConstantReadoutPulse(
                name="rr_readout_pulse",
                length=64*10,#64*8,#400,#
                I_ampx=0.0675,#0.05*0.7*.8*.8*.6, #0.03
                pad=64*10,#300,#64*12, #1200, #
                digital_marker=DigitalWaveform("ADC_ON"),
                # weights=r"C:\Users\qcrew\Desktop\Juncheng\victoria\config\weights\20260817_095646_weights.npz",
            ),
            # ConstantReadoutPulse(
            #     name="rr_readout_pulse",
            #     length=64*20,#64*8,#400,#
            #     I_ampx=0.1, #0.03
            #     pad=64*20,#300,#64*12, #1200, #
            #     digital_marker=DigitalWaveform("ADC_ON"),
            #     # weights="C:\\Users\\qcrew\\Desktop\\Juncheng\\victoria\\config\\weights\\20260702_102842_weights.npz",
            # ),
        ]
        

        qubit.configure(
            name="qubit",
            lo_name="opx1000",
            ports={"I": [1,6]},
            upconverter = 1,
            int_freq=qubit_IF,
            rf_switch=None,
            rf_switch_on=False,
        )

        qubit.operations = [
            GaussianPulse(
                name="qubit_gaussian_pi_pulse_24",
                sigma=6,
                chop=4,
                I_ampx=1.0*0.5/0.84,
                Q_ampx=0.0,
            ),
            GaussianPulse(
                name="qubit_gaussian_pi2_pulse_24",
                sigma=6,
                chop=4,
                I_ampx=1.0*0.5/0.84/2,
                Q_ampx=0.0,
            ),
            GaussianPulse(
                name="qubit_gaussian_pulse_60",
                sigma=15,
                chop=4,
                I_ampx=1.5*0.5/0.483*.5/.42*.5/.6,
                Q_ampx=0.0,
            ),
            GaussianPulse(
                name="qubit_gaussian_pi2_pulse_60",
                sigma=15,
                chop=4,
                I_ampx=1.5*0.5/0.483*.5/.42/2*.5/.6,
                Q_ampx=0.0,
            ),
            GaussianPulse(
                name="qubit_gaussian_pi_pulse_1200",
                sigma=300,
                chop=4,
                I_ampx=1.0*0.5/0.84*24/1200*0.5/0.44*0.5/0.487*0.5/0.482,
                Q_ampx=0.0,
            ),
            ConstantPulse(
                name="qubit_constant_pulse_1000",
                length=1000,
                I_ampx=1,#0.247/10000*52,
                
            ),
            ConstantPulse(
                name="qubit_constant_pulse_10000",
                length=10000,
                I_ampx=0.08,#0.247/10000*52,
                
            ),
            ConstantPulse(
                name="qubit_constant_pi_pulse_1000",
                length=1000,
                I_ampx=1.0*0.5/0.84,#0.247/10000*52,
                
            ),
            ConstantPulse(
                name="qubit_constant_pi_pulse_1200",
                length=1200,
                I_ampx=1.0*0.5/0.84*24/1200*0.5/0.44*0.5/0.487*0.5/0.482/2,#0.247/10000*52,
                
            ),
            ConstantPulse(
                name="qubit_constant_pi_pulse_500",
                length=500,
                I_ampx=1*0.5/4.62*0.5/0.454,#0.247/10000*52,
                
            ),
            ConstantPulse(
                name="qubit_constant_pi_36",
                length=36,
                I_ampx=1.5*0.5/0.46*0.5/0.516,#0.247/10000*52,
                
            ),
            ConstantPulse(
                name="qubit_constant_pi_120",
                length=120,
                I_ampx=1.5*0.5/0.46*0.5/0.516/4*0.5/0.392,#0.247/10000*52,
                
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
                name="cav_gaussian_pulse_1600",
                sigma=400,
                chop=4,
                I_ampx=1.1/9/1.5/3*1.5*1/1.2,
                Q_ampx=0.0,
            ),
            GaussianPulse(
                name="cav_gaussian_1000",
                sigma=250,
                chop=4,
                I_ampx=1*52/1000,
            ),
          
            ConstantPulse(
                name="cav_constant_40",
                length=40,
                I_ampx=1,#.195,
            ),
            ConstantPulse(
                name="cav_constant_200",
                length=200,
                I_ampx=0.1,
            ),
            ConstantPulse(
                name="cav_constant_4000",
                length=4000,
                I_ampx=0.1,
            ),
            ConstantPulse(
                name="cav_constant_2000",
                length=2000,
                I_ampx=1.95,
            ),
            ConstantPulse(
                name="cav_constant_1000",
                length=1000,
                I_ampx=1.85,
            ),
            ConstantPulse(
                name="cav_constant_1800",
                length=1800,
                I_ampx=1.95,
            ),
            ConstantPulse(
                name="cav_constant_10000",
                length=10000,
                I_ampx=0.05,
            ),
            ConstantPulse(
                name="cav_constant_15000",
                length=15000,
                I_ampx=0.03*.8,
            ),
            ConstantPulse(
                name="cav_constant_200_low_power",
                length=100,
                I_ampx=.5,
            ),
            
            

        ]
        
        qubit_EF.configure(
            name="qubit_EF",
            lo_name="opx1000",
            ports={"I": [8,6]},
            upconveter = 1,
            int_freq=qubitEF_IF,
            rf_switch=None,
            rf_switch_on=False,
        )

        qubit_EF.operations = [
            GaussianPulse(
                name="qubit_gaussian_pi_pulse_24",
                sigma=6,
                chop=4,
                I_ampx=1.0*0.5/0.84,
                Q_ampx=0.0,
            ),
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
                I_ampx=1.5*0.5/1.43*0.5/0.515/.7*.5*0.5/0.479,#*0.5/0.426,
                Q_ampx=0.0,
            ),
            ConstantPulse(
                name="qubitEF_constant_pi_24",
                length=24,
                I_ampx=1*0.5/0.52,#0.247/10000*52,
                
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
            ports={"I": [8,6]},
            upconveter = 1,
            int_freq=qubitGF2_IF,
            rf_switch=None,
            rf_switch_on=False,
        )

        qubit_GF2.operations = [
            ConstantPulse(
                name="qubitGF2_constant_pi_200",
                length=200,
                I_ampx=1.5,#0.247/10000*52,
                
            ),
            GaussianPulse(
                name="qubitGF2_gaussian_pi_16",
                sigma=4,
                chop=4,
                I_ampx=1,
                Q_ampx=0.0,
            ),
            GaussianPulse(
                name="qubitGF2_gaussian_pi_24",
                sigma=6,
                chop=4,
                I_ampx=1,#*0.5/0.426,
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
        
        # snail_drive.configure(
        #     name="snail_drive",
        #     lo_name="opx1000",
        #     ports={"I": [1,1]},
        #     upconverter = 1,
        #     int_freq=snail_drive_IF,
        #     rf_switch=None,
        #     rf_switch_on=False,
        # )
       
        
        # snail_drive.operations = [
        # ConstantPulse(
        #         name="snail_drive_constant_2000",
        #         length=2000,
        #         I_ampx=1,#0.247/10000*52,
        #     ),
            
        # GaussianPulse(
        #         name="drive_gaussian_pi_24",
        #         sigma=6,
        #         chop=4,
        #         I_ampx=1.95,#*0.5/0.426,
        #         Q_ampx=0.0,
        #     ),
      
        # ]
        fock_drive.configure(
            name="fock_drive",
            lo_name="opx1000",
            ports={"I": [1,2]},
            upconverter = 1,
            int_freq=fock_drive_IF,
            rf_switch=None,
            rf_switch_on=False,
        )
        
        fock_drive.operations = [
            ConstantPulse(
                name="fock_drive_constant_2000",
                length=2000,
                I_ampx=1.95,#0.247/10000*52,
            ),
            ConstantPulse(
                name="fock_drive_constant_1200",
                length=1200,
                I_ampx=1.95,#0.247/10000*52,
            ),
            
                    ConstantPulse(
                name="drive_constant_56",
                length=56,
                I_ampx=2,#0.247/10000*52,
            ),
            ConstantPulse(
                name="fock_drive_constant_32",
                length=32,
                I_ampx=1,#0.247/10000*52,
            ),
            ConstantPulse(
                name="fock_drive_constant_72",
                length=72,
                I_ampx=1,#0.247/10000*52,
            ),
            ConstantPulse(
                name="fock_drive_constant_200",
                length=200,
                I_ampx=1,#0.247/10000*52,
            ),
            ConstantPulse(
                name="fock_drive_constant_172",
                length=172,
                I_ampx=1,#0.247/10000*52,
            ),
            ConstantPulse(
                name="three_tone_cav_constant_2000",
                length=2000,
                I_ampx=1,#0.247/10000*52,
            ),
            # ConstantPulse(
            #     name="three_tone_cav_constant_1000",
            #     length=1600,
            #     I_ampx=0.04,#0.247/10000*52,
            # ),
        ]
        
        snail_drive.configure(
            name="snail_drive",
            lo_name="opx1000",
            ports={"I": [1,5]},
            upconverter = 1,
            int_freq=snail_drive_IF,
            rf_switch=None,
            rf_switch_on=False,
        )
        
        snail_drive.operations = [
            ConstantPulse(
                name="snail_drive_constant_10000",
                length=10000,
                I_ampx=2,#0.247/10000*52,
            ),
            ConstantPulse(
                name="snail_drive_constant_100",
                length=100,
                I_ampx=2,#0.247/10000*52,
            ),
            ConstantPulse(
                name="snail_drive_constant_2000",
                length=2000,
                I_ampx=2,#0.247/10000*52,
            ),
        
        ]
        
        # snail_drive_EF.configure(
        #     name="snail_drive_EF",
        #     lo_name="opx1000",
        #     ports={"I": [1,5]},
        #     upconverter = 1,
        #     int_freq=SNAIL_drive_EF_IF,
        #     rf_switch=None,
        #     rf_switch_on=False,
        # )
        
        # snail_drive_EF.operations = [
        #     ConstantPulse(
        #         name="snail_drive_EF_constant_100",
        #         length=100,
        #         I_ampx=2,#0.247/10000*52,
        #     ),
        #     ConstantPulse(
        #         name="snail_drive_EF_constant_10000",
        #         length=10000,
        #         I_ampx=2,#0.247/10000*52,
        #     ),
        #     ConstantPulse(
        #         name="snail_drive_EF_constant_pi",
        #         length=200,
        #         I_ampx=1.5,#0.247/10000*52,
        #     ),
        #     GaussianPulse(
        #         name="snail_drive_EF_gaussian_200",
        #         sigma=40,
        #         chop=4,
        #         I_ampx=2.5
        #         # Q_ampx = 1*-0.159,
        #     ),
        # ]
        snail_stark_drive.configure(
            name="snail_stark_drive",
            lo_name="opx1000",
            ports={"I": [1,1]},
            upconverter = 1,
            int_freq=snail_stark_drive_IF,
            rf_switch=None,
            rf_switch_on=False,
        )
        
        snail_stark_drive.operations = [
            ConstantPulse(
                name="snail_stark_drive_constant_10000",
                length=10000,
                I_ampx=2,#0.247/10000*52,
            ),
            ConstantPulse(
                name="snail_stark_drive_constant_2000",
                length=2000,
                I_ampx=2,#0.247/10000*52,
            ),
        ]
