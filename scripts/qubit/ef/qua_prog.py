# Auto-generated standalone QUA execution script
import time
import numpy as np
import matplotlib.pyplot as plt
from qm import QuantumMachinesManager
from qm.qua import *


# Single QUA script generated at 2026-07-29 18:08:52.495007
# QUA library version: 1.3.1


from qm import CompilerOptionArguments
from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    v4 = declare(fixed, )
    v5 = declare(fixed, )
    a1 = declare(fixed, value=[0.0, 1.0])
    with for_(v1,1,(v1<500001),(v1+1)):
        r1 = declare_output_stream()
        save(v1, r1)
        with for_each_((v2),(a1)):
            r2 = declare_output_stream()
            save(v2, r2)
            with for_(v3,-1.4,(v3<1.428),(v3+0.05600000000000005)):
                r3 = declare_output_stream()
                save(v3, r3)
                play('qubit_pi_pulse'*amp(v2), 'qubit')
                align('qubit', 'qubit_EF')
                play('qubitEF_pi_pulse'*amp(v3), 'qubit_EF')
                align('qubit_EF', 'qubit')
                play('qubit_pi_pulse'*amp(1.0), 'qubit')
                align('qubit', 'rr')
                measure('readout_pulse'*amp(1), 'rr', dual_demod.full("cos", "sin", v4), dual_demod.full("minus_sin", "cos", v5))
                wait(30000, 'rr')
                r4 = declare_output_stream()
                save(v4, r4)
                r5 = declare_output_stream()
                save(v5, r5)
    with stream_processing():
        r2.buffer(2).save("qubitGE_pulse_amplitude")
        r3.buffer(51).save("qubitEF_pulse_amplitude")
        r4.buffer(2, 51).save_all("I")
        r4.buffer(2, 51).average().save("I_avg")
        r5.buffer(2, 51).save_all("Q")
        r5.buffer(2, 51).average().save("Q_avg")

config = {
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                "8": {
                    "type": "MW",
                },
                "1": {
                    "type": "MW",
                    "analog_outputs": {
                        "1": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 3750000000.0,
                                },
                            },
                        },
                        "2": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 6709000000.0,
                                },
                            },
                        },
                        "3": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 4650000000.0,
                                },
                            },
                        },
                        "4": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 2400000000.0,
                                },
                            },
                        },
                        "5": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 3350000000.0,
                                },
                            },
                        },
                        "6": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 16,
                            "band": 3,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 7705600000.0,
                                },
                            },
                        },
                    },
                    "analog_inputs": {
                        "1": {
                            "band": 3,
                            "shareable": False,
                            "gain_db": 0,
                            "sampling_rate": 1000000000.0,
                            "downconverter_frequency": 7705600000.0,
                        },
                    },
                },
                "3": {
                    "type": "MW",
                },
                "6": {
                    "type": "LF",
                },
            },
        },
    },
    "oscillators": {},
    "elements": {
        "qubit": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {'qubit_pi_pulse': 'qubit.qubit_gaussian_pi_24'},
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": 96440000.0,
        },
        "qubit_EF": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {'qubitEF_pi_pulse': 'qubit_EF.qubitEF_gaussian_pi_24'},
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": -100000000.0,
        },
        "rr": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {'readout_pulse': 'rr.rr_readout_pulse'},
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 6),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 1, 1),
            },
            "smearing": 0,
            "time_of_flight": 360,
            "intermediate_frequency": -45400000.0,
        },
    },
    "pulses": {
        "rr.rr_readout_pulse": {
            "length": 1792,
            "waveforms": {'I': 'rr.rr_readout_pulse.waveform.I', 'Q': 'rr.rr_readout_pulse.waveform.Q'},
            "integration_weights": {'cos': 'rr.rr_readout_pulse.cos', 'sin': 'rr.rr_readout_pulse.sin', 'minus_sin': 'rr.rr_readout_pulse.minus_sin'},
            "operation": "measurement",
        },
        "qubit_EF.qubitEF_gaussian_pi_24": {
            "length": 24,
            "waveforms": {'I': 'qubit_EF.qubitEF_gaussian_pi_24.waveform.I', 'Q': 'qubit_EF.qubitEF_gaussian_pi_24.waveform.Q'},
            "integration_weights": {},
            "operation": "control",
        },
        "qubit.qubit_gaussian_pi_24": {
            "length": 24,
            "waveforms": {'I': 'qubit.qubit_gaussian_pi_24.waveform.I', 'Q': 'qubit.qubit_gaussian_pi_24.waveform.Q'},
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "qubit_EF.qubitEF_gaussian_pi_24.waveform.I": {
            "type": "arbitrary",
            "samples": [0.010276269571021186, 0.01433265536203396, 0.019394664306687504, 0.025462574635182835, 0.032432976106141924, 0.040080739736555446, 0.04805616318454292, 0.055901942366265, 0.0630912514090294, 0.06908373734860192, 0.07339169976053182] + [0.07564539709490663] * 2 + [0.07339169976053182, 0.06908373734860192, 0.0630912514090294, 0.055901942366265014, 0.04805616318454292, 0.04008073973655546, 0.03243297610614193, 0.025462574635182835, 0.01939466430668751, 0.014332655362033968, 0.010276269571021186],
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "qubit_EF.qubitEF_gaussian_pi_24.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit.qubit_gaussian_pi_24.waveform.I": {
            "type": "arbitrary",
            "samples": [0.012088147498694248, 0.0168597418418054, 0.02281426749333528, 0.02995205174011549, 0.038151451388376736, 0.047147643456000865, 0.05652926723859271, 0.06575838830586114, 0.07421529258635057, 0.08126435386493724, 0.08633188198828372] + [0.08898294379695419] * 2 + [0.08633188198828372, 0.08126435386493726, 0.07421529258635057, 0.06575838830586116, 0.05652926723859271, 0.047147643456000886, 0.03815145138837674, 0.02995205174011549, 0.022814267493335292, 0.01685974184180541, 0.012088147498694248],
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.002688] * 1280 + [0.0] * 512,
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "qubit.qubit_gaussian_pi_24.waveform.Q": {
            "type": "arbitrary",
            "samples": [0.00047831966170698613, 0.0006091171981096152, 0.0007457457326007476, 0.000876004113063304, 0.0009845391038415443, 0.0010544694200147753, 0.0010697854522924767, 0.001018179424425899, 0.0008937624213792502, 0.0006990379240008222, 0.000445577353587099, 0.0001530866840009244, -0.0001530866840009239, -0.000445577353587099, -0.0006990379240008218, -0.0008937624213792502, -0.001018179424425899, -0.0010697854522924767, -0.0010544694200147755, -0.0009845391038415443, -0.000876004113063304, -0.0007457457326007477, -0.0006091171981096156, -0.00047831966170698613],
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "rr.rr_readout_pulse.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
    },
    "digital_waveforms": {
        "rr.rr_readout_pulse.ADC_ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "rr.rr_readout_pulse.sin": {
            "cosine": [(-0.003265380859375, 64), (0.031036376953125, 64), (-0.060516357421875, 64), (-0.122406005859375, 64), (-0.146270751953125, 64), (-0.172637939453125, 64), (-0.147796630859375, 64), (-0.186431884765625, 64), (-0.20745849609375, 64), (-0.22222900390625, 64), (-0.207244873046875, 64), (-0.2347412109375, 64), (-0.2313232421875, 64), (-0.24981689453125, 64), (-0.252838134765625, 64), (-0.242828369140625, 64), (-0.24774169921875, 64), (-0.253326416015625, 64), (-0.26953125, 64), (-0.2706298828125, 64), (-0.233489990234375, 64), (-0.072906494140625, 64), (0.049835205078125, 64), (0.034637451171875, 64), (0.0147705078125, 64), (0.02313232421875, 64), (-0.0084228515625, 64), (0.016021728515625, 64)],
            "sine": [(0.03515625, 64), (0.35382080078125, 64), (0.775054931640625, 64), (0.962371826171875, 64), (0.9892578125, 64), (0.984466552734375, 64), (0.987884521484375, 64), (0.97845458984375, 64), (0.975830078125, 64), (0.96734619140625, 64), (0.965423583984375, 64), (0.948028564453125, 64), (0.949493408203125, 64), (0.925750732421875, 64), (0.94195556640625, 64), (0.939849853515625, 64), (0.927825927734375, 64), (0.921966552734375, 64), (0.918853759765625, 64), (0.90850830078125, 64), (0.84381103515625, 64), (0.431732177734375, 64), (0.167266845703125, 64), (0.046112060546875, 64), (0.00848388671875, 64), (-0.003631591796875, 64), (0.001617431640625, 64), (0.002288818359375, 64)],
        },
        "rr.rr_readout_pulse.cos": {
            "cosine": [(0.03515625, 64), (0.35382080078125, 64), (0.775054931640625, 64), (0.962371826171875, 64), (0.9892578125, 64), (0.984466552734375, 64), (0.987884521484375, 64), (0.97845458984375, 64), (0.975830078125, 64), (0.96734619140625, 64), (0.965423583984375, 64), (0.948028564453125, 64), (0.949493408203125, 64), (0.925750732421875, 64), (0.94195556640625, 64), (0.939849853515625, 64), (0.927825927734375, 64), (0.921966552734375, 64), (0.918853759765625, 64), (0.90850830078125, 64), (0.84381103515625, 64), (0.431732177734375, 64), (0.167266845703125, 64), (0.046112060546875, 64), (0.00848388671875, 64), (-0.003631591796875, 64), (0.001617431640625, 64), (0.002288818359375, 64)],
            "sine": [(0.003265380859375, 64), (-0.031036376953125, 64), (0.060516357421875, 64), (0.122406005859375, 64), (0.146270751953125, 64), (0.172637939453125, 64), (0.147796630859375, 64), (0.186431884765625, 64), (0.20745849609375, 64), (0.22222900390625, 64), (0.207244873046875, 64), (0.2347412109375, 64), (0.2313232421875, 64), (0.24981689453125, 64), (0.252838134765625, 64), (0.242828369140625, 64), (0.24774169921875, 64), (0.253326416015625, 64), (0.26953125, 64), (0.2706298828125, 64), (0.233489990234375, 64), (0.072906494140625, 64), (-0.049835205078125, 64), (-0.034637451171875, 64), (-0.0147705078125, 64), (-0.02313232421875, 64), (0.0084228515625, 64), (-0.016021728515625, 64)],
        },
        "rr.rr_readout_pulse.minus_sin": {
            "cosine": [(0.003265380859375, 64), (-0.031036376953125, 64), (0.060516357421875, 64), (0.122406005859375, 64), (0.146270751953125, 64), (0.172637939453125, 64), (0.147796630859375, 64), (0.186431884765625, 64), (0.20745849609375, 64), (0.22222900390625, 64), (0.207244873046875, 64), (0.2347412109375, 64), (0.2313232421875, 64), (0.24981689453125, 64), (0.252838134765625, 64), (0.242828369140625, 64), (0.24774169921875, 64), (0.253326416015625, 64), (0.26953125, 64), (0.2706298828125, 64), (0.233489990234375, 64), (0.072906494140625, 64), (-0.049835205078125, 64), (-0.034637451171875, 64), (-0.0147705078125, 64), (-0.02313232421875, 64), (0.0084228515625, 64), (-0.016021728515625, 64)],
            "sine": [(-0.03515625, 64), (-0.35382080078125, 64), (-0.775054931640625, 64), (-0.962371826171875, 64), (-0.9892578125, 64), (-0.984466552734375, 64), (-0.987884521484375, 64), (-0.97845458984375, 64), (-0.975830078125, 64), (-0.96734619140625, 64), (-0.965423583984375, 64), (-0.948028564453125, 64), (-0.949493408203125, 64), (-0.925750732421875, 64), (-0.94195556640625, 64), (-0.939849853515625, 64), (-0.927825927734375, 64), (-0.921966552734375, 64), (-0.918853759765625, 64), (-0.90850830078125, 64), (-0.84381103515625, 64), (-0.431732177734375, 64), (-0.167266845703125, 64), (-0.046112060546875, 64), (-0.00848388671875, 64), (0.003631591796875, 64), (-0.001617431640625, 64), (-0.002288818359375, 64)],
        },
    },
    "mixers": {},
}

loaded_config = {
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                "8": {
                    "type": "MW",
                },
                "1": {
                    "type": "MW",
                    "analog_outputs": {
                        "1": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 3750000000.0,
                                },
                            },
                        },
                        "2": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 6709000000.0,
                                },
                            },
                        },
                        "3": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 4650000000.0,
                                },
                            },
                        },
                        "4": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 2400000000.0,
                                },
                            },
                        },
                        "5": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 3350000000.0,
                                },
                            },
                        },
                        "6": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 16,
                            "band": 3,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 7705600000.0,
                                },
                            },
                        },
                    },
                    "analog_inputs": {
                        "1": {
                            "band": 3,
                            "shareable": False,
                            "gain_db": 0,
                            "sampling_rate": 1000000000.0,
                            "downconverter_frequency": 7705600000.0,
                        },
                    },
                },
                "3": {
                    "type": "MW",
                },
                "6": {
                    "type": "LF",
                },
            },
        },
    },
    "oscillators": {},
    "elements": {
        "qubit": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {'qubit_pi_pulse': 'qubit.qubit_gaussian_pi_24'},
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": 96440000.0,
        },
        "qubit_EF": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {'qubitEF_pi_pulse': 'qubit_EF.qubitEF_gaussian_pi_24'},
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": -100000000.0,
        },
        "rr": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {'readout_pulse': 'rr.rr_readout_pulse'},
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 6),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 1, 1),
            },
            "smearing": 0,
            "time_of_flight": 360,
            "intermediate_frequency": -45400000.0,
        },
    },
    "pulses": {
        "rr.rr_readout_pulse": {
            "length": 1792,
            "waveforms": {'I': 'rr.rr_readout_pulse.waveform.I', 'Q': 'rr.rr_readout_pulse.waveform.Q'},
            "integration_weights": {'cos': 'rr.rr_readout_pulse.cos', 'sin': 'rr.rr_readout_pulse.sin', 'minus_sin': 'rr.rr_readout_pulse.minus_sin'},
            "operation": "measurement",
        },
        "qubit_EF.qubitEF_gaussian_pi_24": {
            "length": 24,
            "waveforms": {'I': 'qubit_EF.qubitEF_gaussian_pi_24.waveform.I', 'Q': 'qubit_EF.qubitEF_gaussian_pi_24.waveform.Q'},
            "integration_weights": {},
            "operation": "control",
        },
        "qubit.qubit_gaussian_pi_24": {
            "length": 24,
            "waveforms": {'I': 'qubit.qubit_gaussian_pi_24.waveform.I', 'Q': 'qubit.qubit_gaussian_pi_24.waveform.Q'},
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "qubit_EF.qubitEF_gaussian_pi_24.waveform.I": {
            "type": "arbitrary",
            "samples": [0.010276269571021186, 0.01433265536203396, 0.019394664306687504, 0.025462574635182835, 0.032432976106141924, 0.040080739736555446, 0.04805616318454292, 0.055901942366265, 0.0630912514090294, 0.06908373734860192, 0.07339169976053182] + [0.07564539709490663] * 2 + [0.07339169976053182, 0.06908373734860192, 0.0630912514090294, 0.055901942366265014, 0.04805616318454292, 0.04008073973655546, 0.03243297610614193, 0.025462574635182835, 0.01939466430668751, 0.014332655362033968, 0.010276269571021186],
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "qubit_EF.qubitEF_gaussian_pi_24.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit.qubit_gaussian_pi_24.waveform.I": {
            "type": "arbitrary",
            "samples": [0.012088147498694248, 0.0168597418418054, 0.02281426749333528, 0.02995205174011549, 0.038151451388376736, 0.047147643456000865, 0.05652926723859271, 0.06575838830586114, 0.07421529258635057, 0.08126435386493724, 0.08633188198828372] + [0.08898294379695419] * 2 + [0.08633188198828372, 0.08126435386493726, 0.07421529258635057, 0.06575838830586116, 0.05652926723859271, 0.047147643456000886, 0.03815145138837674, 0.02995205174011549, 0.022814267493335292, 0.01685974184180541, 0.012088147498694248],
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.002688] * 1280 + [0.0] * 512,
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "qubit.qubit_gaussian_pi_24.waveform.Q": {
            "type": "arbitrary",
            "samples": [0.00047831966170698613, 0.0006091171981096152, 0.0007457457326007476, 0.000876004113063304, 0.0009845391038415443, 0.0010544694200147753, 0.0010697854522924767, 0.001018179424425899, 0.0008937624213792502, 0.0006990379240008222, 0.000445577353587099, 0.0001530866840009244, -0.0001530866840009239, -0.000445577353587099, -0.0006990379240008218, -0.0008937624213792502, -0.001018179424425899, -0.0010697854522924767, -0.0010544694200147755, -0.0009845391038415443, -0.000876004113063304, -0.0007457457326007477, -0.0006091171981096156, -0.00047831966170698613],
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "rr.rr_readout_pulse.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
    },
    "digital_waveforms": {
        "rr.rr_readout_pulse.ADC_ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "rr.rr_readout_pulse.sin": {
            "cosine": [(-0.003265380859375, 64), (0.031036376953125, 64), (-0.060516357421875, 64), (-0.122406005859375, 64), (-0.146270751953125, 64), (-0.172637939453125, 64), (-0.147796630859375, 64), (-0.186431884765625, 64), (-0.20745849609375, 64), (-0.22222900390625, 64), (-0.207244873046875, 64), (-0.2347412109375, 64), (-0.2313232421875, 64), (-0.24981689453125, 64), (-0.252838134765625, 64), (-0.242828369140625, 64), (-0.24774169921875, 64), (-0.253326416015625, 64), (-0.26953125, 64), (-0.2706298828125, 64), (-0.233489990234375, 64), (-0.072906494140625, 64), (0.049835205078125, 64), (0.034637451171875, 64), (0.0147705078125, 64), (0.02313232421875, 64), (-0.0084228515625, 64), (0.016021728515625, 64)],
            "sine": [(0.03515625, 64), (0.35382080078125, 64), (0.775054931640625, 64), (0.962371826171875, 64), (0.9892578125, 64), (0.984466552734375, 64), (0.987884521484375, 64), (0.97845458984375, 64), (0.975830078125, 64), (0.96734619140625, 64), (0.965423583984375, 64), (0.948028564453125, 64), (0.949493408203125, 64), (0.925750732421875, 64), (0.94195556640625, 64), (0.939849853515625, 64), (0.927825927734375, 64), (0.921966552734375, 64), (0.918853759765625, 64), (0.90850830078125, 64), (0.84381103515625, 64), (0.431732177734375, 64), (0.167266845703125, 64), (0.046112060546875, 64), (0.00848388671875, 64), (-0.003631591796875, 64), (0.001617431640625, 64), (0.002288818359375, 64)],
        },
        "rr.rr_readout_pulse.cos": {
            "cosine": [(0.03515625, 64), (0.35382080078125, 64), (0.775054931640625, 64), (0.962371826171875, 64), (0.9892578125, 64), (0.984466552734375, 64), (0.987884521484375, 64), (0.97845458984375, 64), (0.975830078125, 64), (0.96734619140625, 64), (0.965423583984375, 64), (0.948028564453125, 64), (0.949493408203125, 64), (0.925750732421875, 64), (0.94195556640625, 64), (0.939849853515625, 64), (0.927825927734375, 64), (0.921966552734375, 64), (0.918853759765625, 64), (0.90850830078125, 64), (0.84381103515625, 64), (0.431732177734375, 64), (0.167266845703125, 64), (0.046112060546875, 64), (0.00848388671875, 64), (-0.003631591796875, 64), (0.001617431640625, 64), (0.002288818359375, 64)],
            "sine": [(0.003265380859375, 64), (-0.031036376953125, 64), (0.060516357421875, 64), (0.122406005859375, 64), (0.146270751953125, 64), (0.172637939453125, 64), (0.147796630859375, 64), (0.186431884765625, 64), (0.20745849609375, 64), (0.22222900390625, 64), (0.207244873046875, 64), (0.2347412109375, 64), (0.2313232421875, 64), (0.24981689453125, 64), (0.252838134765625, 64), (0.242828369140625, 64), (0.24774169921875, 64), (0.253326416015625, 64), (0.26953125, 64), (0.2706298828125, 64), (0.233489990234375, 64), (0.072906494140625, 64), (-0.049835205078125, 64), (-0.034637451171875, 64), (-0.0147705078125, 64), (-0.02313232421875, 64), (0.0084228515625, 64), (-0.016021728515625, 64)],
        },
        "rr.rr_readout_pulse.minus_sin": {
            "cosine": [(0.003265380859375, 64), (-0.031036376953125, 64), (0.060516357421875, 64), (0.122406005859375, 64), (0.146270751953125, 64), (0.172637939453125, 64), (0.147796630859375, 64), (0.186431884765625, 64), (0.20745849609375, 64), (0.22222900390625, 64), (0.207244873046875, 64), (0.2347412109375, 64), (0.2313232421875, 64), (0.24981689453125, 64), (0.252838134765625, 64), (0.242828369140625, 64), (0.24774169921875, 64), (0.253326416015625, 64), (0.26953125, 64), (0.2706298828125, 64), (0.233489990234375, 64), (0.072906494140625, 64), (-0.049835205078125, 64), (-0.034637451171875, 64), (-0.0147705078125, 64), (-0.02313232421875, 64), (0.0084228515625, 64), (-0.016021728515625, 64)],
            "sine": [(-0.03515625, 64), (-0.35382080078125, 64), (-0.775054931640625, 64), (-0.962371826171875, 64), (-0.9892578125, 64), (-0.984466552734375, 64), (-0.987884521484375, 64), (-0.97845458984375, 64), (-0.975830078125, 64), (-0.96734619140625, 64), (-0.965423583984375, 64), (-0.948028564453125, 64), (-0.949493408203125, 64), (-0.925750732421875, 64), (-0.94195556640625, 64), (-0.939849853515625, 64), (-0.927825927734375, 64), (-0.921966552734375, 64), (-0.918853759765625, 64), (-0.90850830078125, 64), (-0.84381103515625, 64), (-0.431732177734375, 64), (-0.167266845703125, 64), (-0.046112060546875, 64), (-0.00848388671875, 64), (0.003631591796875, 64), (-0.001617431640625, 64), (-0.002288818359375, 64)],
        },
    },
    "mixers": {},
}



if __name__ == '__main__':
    # 1. Connect to QM and execute
    qmm = QuantumMachinesManager('192.168.111.181')
    qm = qmm.open_qm(config, close_other_machines=True)
    job = qm.execute(prog)
    print('>>> Program execution started!')

    results = job.result_handles
    handles = {name: results.get(name) for name in results.keys()}
    print(f'Available result handles: {list(handles.keys())}')

    # 2. Track execution progress if 'iteration' or 'r1' is streamed
    iter_handle = handles.get('iteration') or handles.get('r1')
    if iter_handle:
        while results.is_processing():
            try:
                completed = iter_handle.count_so_far()
                print(f'Progress: {completed} iterations completed', end='\r')
            except Exception:
                pass
            time.sleep(0.3)
        print('\n>>> Execution complete on hardware!')
    else:
        print('Waiting for job completion...')
        results.wait_for_all_values()

    # 3. Automatically fetch and plot all streams
    fetched_data = {}
    for name, handle in handles.items():
        if handle is None:
            continue
        try:
            data = handle.fetch_all()
            if data is not None and getattr(data, 'size', 0) > 0:
                # Convert complex IQ data to magnitude
                if np.iscomplexobj(data):
                    data = np.abs(data)
                fetched_data[name] = data
                print(f'Fetched stream [{name}] with shape: {data.shape}')
        except Exception as e:
            print(f'Could not fetch stream [{name}]: {e}')

    # 4. Auto Plotting
    plot_keys = [k for k in fetched_data.keys() if k not in ['iteration', 'r1', 'r2']]
    if plot_keys:
        plt.figure(figsize=(9, 4.5))
        for key in plot_keys:
            d = fetched_data[key]
            if d.ndim == 1:
                plt.plot(d, label=key, linewidth=1.5)
            elif d.ndim == 2:
                plt.imshow(d, aspect='auto', origin='lower')
                plt.colorbar(label=key)
        plt.title('QUA Program Results')
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.show()
    else:
        print('No plottable data streams were found.')
