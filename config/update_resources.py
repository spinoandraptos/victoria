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
        (opx1000, qubit, rr, cav, qubit_EF, qubit_GF2, drive, snail_drive, snail_drive_EF,fock_drive) = stage.get("opx1000", "qubit", "rr", "cavity", "qubit_EF", "qubit_GF2", "drive", "snail_drive", "snail_drive_EF","fock_drive")
        u = unit(coerce_to_integer=True)
        
        rr_LO = 5.649e9+50e6#7.415e9+50e6+0.5e6 
        rr_IF = -56.8e6
        # rr_LO = 7.773e9+50e6#7.415e9+50e6+0.5e6 
        # rr_IF = -49.7e6
        
        # rr_LO = 3.88e9+50e6#7.415e9+50e6+0.5e6 
        # rr_IF = -55.6e6
        
        # rr_LO = 3.7e9+50e6#5.6118e9+50e6 #fock
        # rr_IF = -50e6#124e6#-40e6 #-55.95e6 #-43.8e6# -76e6  -92e6#
        
        qubit_LO = 4e9-800e6#5.6e9+50e6-400e6#+50e6+800e6#5.7e9+50e6-150E6
        qubit_IF =-379e6
        
        # qubit_LO =  6.659e9+50e6#6.659e9+50e6+1e8 #-800e6-800e6-800e6#5.6118e9+50e6
        # qubit_IF = 9.8e7#-2.9e8#5.9e7 #-2.643e8#124.15e6+1e3#-40e6 #-55.95e6 #-43.8e6# -76e6  -92e6#
        
        cav_LO = 3e9 + 50e6
        cav_IF = -26e6 #-94.6e6#-6.3762e7#-1.365e8#-6.1813e7 #-1.365e8#-1.0608e8#-9.7255e7#-1.365e8#-6.1813e7#-93e6-380e3+60e3 #-52.6e6
        
        qubitEF_IF = 22e6 #-118e6# -76e6
        qubitGF2_IF = 115e6#59.5e6 #3.2e6 no stark shift #stark shift 59.5e6
        
        # drive_LO = 3.7e9+50e6#5.6118e9+50e6 #fock
        # drive_IF = 124e6#-40e6 #-55.95e6 #-43.8e6# -76e6  -92e6#
        
        fock_drive_LO = 4.0949e9 #3e9-800e6#2.4e9#5.6118e9+50e6 #fock
        fock_drive_IF = -359e6#-40e6 #-55.95e6 #-43.8e6# -76e6  -92e6#
        
        # drive_LO = 7.6556e9+50e6#7.415e9+50e6+0.5e6 
        # drive_IF = -45.6e6
        # SNAIL_drive_LO = 3.7e9-400e6+50e6#5.6118e9+50e6 #fock
        # SNAIL_drive_IF = -33.3e6#-40e6 #-55.95e6 #-43.8e6# -76e6  -92e6#
        
        # SNAIL_drive_LO =  6.659e9+50e6#6.659e9+50e6+1e8 #-800e6-800e6-800e6#5.6118e9+50e6
        # SNAIL_drive_IF = 9.8e7#-2.9e8#5.9e7 #-2.643e8#124.15e6+1e3#-40e6 #-55.95e6 #-43.8e6# -76e6  -92e6#
        
        # SNAIL_drive_LO = 6.659e9+50e6+350e6#-400E6-400e6#3.7e9+50e6#6.659e9+50e6#3.7e9+50e6#5.6118e9+50e6
        # SNAIL_drive_IF = -188e6#-40e6 #-55.95e6 #-43.8e6# -76e6  -92e6#
        # SNAIL_drive_EF_IF = 5e7
        
        # drive_LO = SNAIL_drive_LO#2.4e9#5.6118e9+50e6
        # drive_IF = -129e6#-40e6 #-55.95e6 #-43.8e6# -76e6  -92e6#
        
      

        # yoko1.output = True
        # yoko1.ramp(0e-3, step=1e-4) #-0.0125
        settings = {
                "controllers": {
                    "con1": {
                        "fems": {
                            1: {
                                "analog_outputs": {
                                    6: {
                                        "full_scale_power_dbm": -2, #only in increments of 3s -11
                                        "upconverters": {1: {"frequency":  rr_LO}},
                                        "band":3,
                                    },
   
                                    4: {
                                        "full_scale_power_dbm": 8, 
                                        "upconverters": {1: {"frequency": qubit_LO}},
                                        "band":1,
                                    },
                                    # 5: {
                                    #     "full_scale_power_dbm": 4, #-11 to 16
                                    #     "upconverters": {1: {"frequency": SNAIL_drive_LO}},
                                    #     "band":2,
                                    # },
                                    2: {
                                        "full_scale_power_dbm": 8, #16
                                        "upconverters": {1: {"frequency": fock_drive_LO}},
                                        "band":1,
                                    },
                                    # 5: {
                                    #     "full_scale_power_dbm": 16, 
                                    #     "upconverters": {1: {"frequency": qubit_LO}},
                                    #     "band":2,
                                    # },
                                    # 1: {
                                    #     "full_scale_power_dbm": 4, 
                                    #     "upconverters": {1: {"frequency": drive_LO}},
                                    #     "band":2,
                                    # },
                                    5: {
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
                            
                            # 8: {
                            #     "analog_outputs": {
                            #         8: {
                            #             "full_scale_power_dbm": 4, #only in increments of 3s -11
                            #             "upconverters": {1: {"frequency":  drive_LO}},
                            #             "band":2,
                            #         },
   
                            #     },
                            #     "analog_inputs": {
                            #         1: {
                            #             "downconverter_frequency": rr_LO,
                            #             "band":3
                            #             },  # for down-conversion
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
                "I": [1,6], "out1": [1,1] 
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
                I_ampx=1.0,
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
                length=64*5,#64*8,#400,#
                I_ampx=1.72,#0.05*0.7*.8*.8*.6, #0.03
                pad=64*5,#300,#64*12, #1200, #
                digital_marker=DigitalWaveform("ADC_ON"),
                # weights=r"C:\Users\qcrew\Desktop\Juncheng\victoria\config\weights\20260806_103504_weights.npz",
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
            ports={"I": [1,4]},
            upconverter = 1,
            int_freq=qubit_IF,
            rf_switch=None,
            rf_switch_on=False,
        )

        qubit.operations = [
            ConstantPulse(
                name="qubit_constant_pulse",
                length=1000,
                I_ampx=1,#0.247/10000*52,
                
            ),
            ConstantPulse(
                name="qubit_constant_pulse_10000",
                length=10000,
                I_ampx=1,#0.247/10000*52,
                
            ),
            ConstantPulse(
                name="qubit_constant_pi_pulse_1000",
                length=1000,
                I_ampx=0.05*0.5/0.386,#0.247/10000*52,
                
            ),
            ConstantPulse(
                name="qubit_constant_pi_pulse_1200",
                length=1200,
                I_ampx=0.05*0.5/0.386*1000/1200*0.5/0.435*0.5/0.583,#0.247/10000*52,
                
            ),
            ConstantPulse(
                name="qubit_constant_pi_36",
                length=36,
                I_ampx=1.5*0.5/0.46*0.5/0.516,#0.247/10000*52,
                
            ),
            ConstantPulse(
                name="qubit_constant_pi_100",
                length=100,
                I_ampx=1,#0.247/10000*52,
                
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
            ports={"I": [1,5]},
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
            GaussianPulse(
                name="cav_gaussian_1000",
                sigma=250,
                chop=4,
                I_ampx=1*52/1000,
            ),
          
            ConstantPulse(
                name="cav_constant_160",
                length=160,
                I_ampx=1,
            ),
            ConstantPulse(
                name="cav_constant_200",
                length=200,
                I_ampx=1,
            ),
            ConstantPulse(
                name="cav_constant_4000",
                length=4000,
                I_ampx=1,
            ),
            
            

        ]
        
        qubit_EF.configure(
            name="qubit_EF",
            lo_name="opx1000",
            ports={"I": [1,4]},
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
            ports={"I": [1,4]},
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
        # drive.configure(
        #     name="drive",
        #     lo_name="opx1000",
        #     ports={"I": [1,4]},
        #     upconverter = 1,
        #     int_freq=drive_IF,
        #     rf_switch=None,
        #     rf_switch_on=False,
        # )
        # drive.configure(
        #     name="drive",
        #     lo_name="opx1000",
        #     ports={"I": [1,1]},
        #     upconverter = 1,
        #     int_freq=drive_IF,
        #     rf_switch=None,
        #     rf_switch_on=False,
        # )
        
        # drive.operations = [
        #                 ConstantPulse(
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
        # ConstantPulse(
        #         name="drive_constant_56",
        #         length=56,
        #         I_ampx=2,#0.247/10000*52,
        #     ),
        # ConstantPulse(
        #         name="drive_constant_24",
        #         length=24,
        #         I_ampx=2,#0.247/10000*52,
        #     ),
        # ConstantPulse(
        #         name="drive_constant_192",
        #         length=4*48,
        #         I_ampx=2,#0.247/10000*52,
        #     ),
        # ConstantPulse(
        #         name="drive_constant_100",
        #         length=100,
        #         I_ampx=1,#0.247/10000*52,
        #     ),
        # ConstantPulse(
        #         name="drive_constant_500",
        #         length=500,
        #         I_ampx=1,#0.247/10000*52,
        #     ),
        # ConstantPulse(
        #         name="drive_constant_1000",
        #         length=1000,
        #         I_ampx=1,#0.247/10000*52,
        #     ),
        # ConstantPulse(
        #         name="drive_constant_2000",
        #         length=2000,
        #         I_ampx=2,#0.247/10000*52,
        #     ),
        # ConstantPulse(
        #         name="drive_constant_4000",
        #         length=4000,
        #         I_ampx=1,#0.247/10000*52,
        #     ),
        # ConstantPulse(
        #         name="drive_constant_5000",
        #         length=5000,
        #         I_ampx=1,#0.247/10000*52,
        #     ),
        # ConstantPulse(
        #         name="drive_constant_10000",
        #         length=10000,
        #         I_ampx=1,#0.247/10000*52,
        #     ),
        # ConstantPulse(
        #         name="drive_constant_fock1",
        #         length=60,
        #         I_ampx=.9,#0.247/10000*52,
        #     ),
        # ConstantPulse(
        #         name="drive_constant_fock1",
        #         length=24,
        #         I_ampx=2,#0.247/10000*52,
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
                I_ampx=1,#0.247/10000*52,
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
        ]
        
        # snail_drive.configure(
        #     name="snail_drive",
        #     lo_name="opx1000",
        #     ports={"I": [1,5]},
        #     upconverter = 1,
        #     int_freq=SNAIL_drive_IF,
        #     rf_switch=None,
        #     rf_switch_on=False,
        # )
        
        # snail_drive.operations = [
        #     ConstantPulse(
        #         name="snail_drive_constant_10000",
        #         length=10000,
        #         I_ampx=2,#0.247/10000*52,
        #     ),
        #     ConstantPulse(
        #         name="snail_drive_constant_100",
        #         length=100,
        #         I_ampx=2,#0.247/10000*52,
        #     ),
        #     ConstantPulse(
        #         name="snail_drive_constant_2000",
        #         length=2000,
        #         I_ampx=2,#0.247/10000*52,
        #     ),
        #     ConstantPulse(
        #         name="snail_drive_constant_500",
        #         length=500,
        #         I_ampx=2,#0.247/10000*52,
        #     ),
        #     ConstantPulse(
        #         name="snail_drive_constant_1000",
        #         length=1000,
        #         I_ampx=1,#0.247/10000*52,
        #     ),
        #     ConstantPulse(
        #         name="snail_drive_constant_5000",
        #         length=5000,
        #         I_ampx=2,#0.247/10000*52,
        #     ),
        #     ConstantPulse(
        #         name="snail_drive_constant_60",
        #         length=60,
        #         I_ampx=1,#0.247/10000*52,
        #     ),
        #     ConstantPulse(
        #         name="snail_drive_constant_4000",
        #         length=4000,
        #         I_ampx=1,#0.247/10000*52,
        #     ),
        #     ConstantPulse(
        #         name="snail_drive_gaussian_4000",
        #         sigma=100,
        #         chop=40,
        #         I_ampx=2,#0.247/10000*52,
        #     ),
        #     # ConstantPulse(
        #     #     name="snail_drive_constant_pi",
        #     #     length=100,
        #     #     I_ampx=1.33,#0.247/10000*52,
        #     # ),
        #     GaussianPulse(
        #         name="snail_drive_gaussian_200",
        #         sigma=50,
        #         chop=4,
        #         I_ampx=2
        #         # Q_ampx = 1*-0.159,
        #     ),
        #     ConstantPulse(
        #         name="snail_drive_constant_pi",
        #         length=200,
        #         I_ampx=1.5,#0.247/10000*52,
        #     ),
        #     ConstantPulse(
        #         name="snail_drive_constant_pi2",
        #         length=92,
        #         I_ampx=2,#0.247/10000*52,
        #     ),
        #     # ConstantPulse(
        #     #     name="snail_drive_constant_pi2",
        #     #     length=1000,
        #     #     I_ampx=1.33*0.5/0.4/2*0.5/0.3,#0.247/10000*52,
        #     # ),
        #     GaussianPulse(
        #         name="snail_drive_gaussian_2000",
        #         sigma=520,
        #         chop=4,
        #         I_ampx=2
        #         # Q_ampx = 1*-0.159,
        #     ),
        # ]
        
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
