# Auto-generated standalone QUA execution script
import time
import numpy as np
import matplotlib.pyplot as plt
from qm import QuantumMachinesManager
from qm.qua import *


# Single QUA script generated at 2026-08-26 10:21:52.517191
# QUA library version: 1.3.1


from qm import CompilerOptionArguments
from qm.qua import *

with program() as prog:
    v1 = declare(fixed, value=0.0)
    v2 = declare(int, )
    v3 = declare(int, )
    v4 = declare(fixed, )
    v5 = declare(fixed, )
    v6 = declare(fixed, )
    with for_(v2,1,(v2<5001),(v2+1)):
        r2 = declare_output_stream()
        save(v2, r2)
        with for_(v3,16,(v3<10020),(v3+40)):
            r3 = declare_output_stream()
            save(v3, r3)
            assign(v6, 0.002)
            reset_frame('qubit')
            reset_if_phase('qubit')
            play('qubit_drive'*amp(1.0), 'qubit')
            wait(Cast.to_int(((v3/2)/4)), 'qubit')
            play('echo_pulse'*amp(1.0), 'qubit')
            wait(Cast.to_int(((v3/2)/4)), 'qubit')
            assign(v1, Cast.mul_fixed_by_int(v6,v3))
            frame_rotation_2pi(v1, 'qubit')
            play('qubit_drive'*amp(1.0), 'qubit')
            frame_rotation_2pi((0.0-v1), 'qubit')
            align('qubit', 'rr')
            measure('readout_pulse'*amp(1), 'rr', dual_demod.full("cos", "sin", v4), dual_demod.full("minus_sin", "cos", v5))
            wait(25000, 'rr')
            r4 = declare_output_stream()
            save(v4, r4)
            r5 = declare_output_stream()
            save(v5, r5)
    with stream_processing():
        r3.buffer(251).save("time_delay")
        r4.buffer(251).save_all("I")
        r4.buffer(251).average().save("I_avg")
        r5.buffer(251).save_all("Q")
        r5.buffer(251).average().save("Q_avg")

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
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 4461000000.0,
                                },
                            },
                        },
                        "3": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -2,
                            "band": 3,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 7688900000.0,
                                },
                            },
                        },
                        "4": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 7,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 6605000000.0,
                                },
                            },
                        },
                        "6": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 8,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 5682600000.0,
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
                            "downconverter_frequency": 7688900000.0,
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
            "operations": {'qubit_drive': 'qubit.qubit_gaussian_pi2_pulse_24', 'echo_pulse': 'qubit.qubit_gaussian_pi_pulse_24'},
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
            "intermediate_frequency": 50000000.0,
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
                "port": ('con1', 1, 3),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 1, 1),
            },
            "smearing": 0,
            "time_of_flight": 396,
            "intermediate_frequency": -50000000.0,
        },
    },
    "pulses": {
        "qubit.qubit_gaussian_pi_pulse_24": {
            "length": 24,
            "waveforms": {'Q': 'qubit.qubit_gaussian_pi_pulse_24.waveform.Q', 'I': 'qubit.qubit_gaussian_pi_pulse_24.waveform.I'},
            "integration_weights": {},
            "operation": "control",
        },
        "rr.rr_readout_pulse": {
            "length": 1280,
            "waveforms": {'Q': 'rr.rr_readout_pulse.waveform.Q', 'I': 'rr.rr_readout_pulse.waveform.I'},
            "integration_weights": {'minus_sin': 'rr.rr_readout_pulse.minus_sin', 'sin': 'rr.rr_readout_pulse.sin', 'cos': 'rr.rr_readout_pulse.cos'},
            "operation": "measurement",
        },
        "qubit.qubit_gaussian_pi2_pulse_24": {
            "length": 24,
            "waveforms": {'Q': 'qubit.qubit_gaussian_pi2_pulse_24.waveform.Q', 'I': 'qubit.qubit_gaussian_pi2_pulse_24.waveform.I'},
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "qubit.qubit_gaussian_pi2_pulse_24.waveform.I": {
            "type": "arbitrary",
            "samples": [0.011410299746780378, 0.015914325010438105, 0.02153494823175368, 0.02827247834481747, 0.0360120933470676, 0.04450382031203782, 0.0533593657529302, 0.062070960129838135, 0.07005364008808962, 0.07670742240922568, 0.08149078684690056] + [0.08399318929421015] * 2 + [0.08149078684690056, 0.07670742240922569, 0.07005364008808962, 0.06207096012983814, 0.0533593657529302, 0.04450382031203784, 0.036012093347067606, 0.02827247834481747, 0.02153494823175369, 0.015914325010438116, 0.011410299746780378],
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "rr.rr_readout_pulse.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.008749999999999999] * 640 + [0.0] * 640,
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "qubit.qubit_gaussian_pi_pulse_24.waveform.Q": {
            "type": "arbitrary",
            "samples": [0.0007524961559032438, 0.0009582678421294457, 0.0011732128992160864, 0.0013781363811872318, 0.0015488844600977983, 0.0016588993691936543, 0.0016829946684994155, 0.0016018076701384237, 0.0014060738878650992, 0.001099731816927566, 0.0007009857059508271, 0.00024083714397096816, -0.0002408371439709674, -0.0007009857059508271, -0.0010997318169275656, -0.0014060738878650992, -0.0016018076701384235, -0.0016829946684994155, -0.0016588993691936547, -0.0015488844600977981, -0.0013781363811872318, -0.0011732128992160867, -0.0009582678421294462, -0.0007524961559032438],
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "qubit.qubit_gaussian_pi2_pulse_24.waveform.Q": {
            "type": "arbitrary",
            "samples": [0.0003762480779516219, 0.00047913392106472283, 0.0005866064496080432, 0.0006890681905936159, 0.0007744422300488992, 0.0008294496845968272, 0.0008414973342497077, 0.0008009038350692119, 0.0007030369439325496, 0.000549865908463783, 0.00035049285297541355, 0.00012041857198548408, -0.0001204185719854837, -0.00035049285297541355, -0.0005498659084637828, -0.0007030369439325496, -0.0008009038350692117, -0.0008414973342497077, -0.0008294496845968274, -0.0007744422300488991, -0.0006890681905936159, -0.0005866064496080433, -0.0004791339210647231, -0.0003762480779516219],
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "qubit.qubit_gaussian_pi_pulse_24.waveform.I": {
            "type": "arbitrary",
            "samples": [0.022820599493560755, 0.03182865002087621, 0.04306989646350736, 0.05654495668963494, 0.0720241866941352, 0.08900764062407564, 0.1067187315058604, 0.12414192025967627, 0.14010728017617924, 0.15341484481845136, 0.16298157369380112] + [0.1679863785884203] * 2 + [0.16298157369380112, 0.15341484481845138, 0.14010728017617924, 0.12414192025967628, 0.1067187315058604, 0.08900764062407568, 0.07202418669413521, 0.05654495668963494, 0.04306989646350738, 0.03182865002087623, 0.022820599493560755],
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
    },
    "digital_waveforms": {
        "rr.rr_readout_pulse.ADC_ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "rr.rr_readout_pulse.cos": {
            "cosine": [(-0.02685546875, 64), (0.03436279296875, 64), (0.034820556640625, 64), (0.0902099609375, 64), (-0.00579833984375, 64), (-0.097076416015625, 64), (-0.148223876953125, 64), (-0.014373779296875, 64), (0.0296630859375, 64), (-0.097747802734375, 64), (-0.09478759765625, 64), (-0.26995849609375, 64), (-0.44439697265625, 64), (-0.32989501953125, 64), (-0.254486083984375, 64), (-0.030975341796875, 64), (-0.2650146484375, 64), (-0.3665771484375, 64), (-0.36962890625, 64), (-0.2196044921875, 64)],
            "sine": [(0.08917236328125, 64), (0.0191650390625, 64), (0.352386474609375, 64), (0.33746337890625, 64), (0.514190673828125, 64), (0.424224853515625, 64), (0.607574462890625, 64), (0.642181396484375, 64), (0.65460205078125, 64), (0.920318603515625, 64), (0.8701171875, 64), (0.962860107421875, 64), (0.803466796875, 64), (0.566558837890625, 64), (0.519683837890625, 64), (0.53485107421875, 64), (0.746795654296875, 64), (0.60693359375, 64), (0.638214111328125, 64), (0.579254150390625, 64)],
        },
        "rr.rr_readout_pulse.sin": {
            "cosine": [(-0.08917236328125, 64), (-0.0191650390625, 64), (-0.352386474609375, 64), (-0.33746337890625, 64), (-0.514190673828125, 64), (-0.424224853515625, 64), (-0.607574462890625, 64), (-0.642181396484375, 64), (-0.65460205078125, 64), (-0.920318603515625, 64), (-0.8701171875, 64), (-0.962860107421875, 64), (-0.803466796875, 64), (-0.566558837890625, 64), (-0.519683837890625, 64), (-0.53485107421875, 64), (-0.746795654296875, 64), (-0.60693359375, 64), (-0.638214111328125, 64), (-0.579254150390625, 64)],
            "sine": [(-0.02685546875, 64), (0.03436279296875, 64), (0.034820556640625, 64), (0.0902099609375, 64), (-0.00579833984375, 64), (-0.097076416015625, 64), (-0.148223876953125, 64), (-0.014373779296875, 64), (0.0296630859375, 64), (-0.097747802734375, 64), (-0.09478759765625, 64), (-0.26995849609375, 64), (-0.44439697265625, 64), (-0.32989501953125, 64), (-0.254486083984375, 64), (-0.030975341796875, 64), (-0.2650146484375, 64), (-0.3665771484375, 64), (-0.36962890625, 64), (-0.2196044921875, 64)],
        },
        "rr.rr_readout_pulse.minus_sin": {
            "cosine": [(0.08917236328125, 64), (0.0191650390625, 64), (0.352386474609375, 64), (0.33746337890625, 64), (0.514190673828125, 64), (0.424224853515625, 64), (0.607574462890625, 64), (0.642181396484375, 64), (0.65460205078125, 64), (0.920318603515625, 64), (0.8701171875, 64), (0.962860107421875, 64), (0.803466796875, 64), (0.566558837890625, 64), (0.519683837890625, 64), (0.53485107421875, 64), (0.746795654296875, 64), (0.60693359375, 64), (0.638214111328125, 64), (0.579254150390625, 64)],
            "sine": [(0.02685546875, 64), (-0.03436279296875, 64), (-0.034820556640625, 64), (-0.0902099609375, 64), (0.00579833984375, 64), (0.097076416015625, 64), (0.148223876953125, 64), (0.014373779296875, 64), (-0.0296630859375, 64), (0.097747802734375, 64), (0.09478759765625, 64), (0.26995849609375, 64), (0.44439697265625, 64), (0.32989501953125, 64), (0.254486083984375, 64), (0.030975341796875, 64), (0.2650146484375, 64), (0.3665771484375, 64), (0.36962890625, 64), (0.2196044921875, 64)],
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
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 4461000000.0,
                                },
                            },
                        },
                        "3": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -2,
                            "band": 3,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 7688900000.0,
                                },
                            },
                        },
                        "4": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 7,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 6605000000.0,
                                },
                            },
                        },
                        "6": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 8,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 5682600000.0,
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
                            "downconverter_frequency": 7688900000.0,
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
            "operations": {'qubit_drive': 'qubit.qubit_gaussian_pi2_pulse_24', 'echo_pulse': 'qubit.qubit_gaussian_pi_pulse_24'},
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
            "intermediate_frequency": 50000000.0,
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
                "port": ('con1', 1, 3),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 1, 1),
            },
            "smearing": 0,
            "time_of_flight": 396,
            "intermediate_frequency": -50000000.0,
        },
    },
    "pulses": {
        "qubit.qubit_gaussian_pi_pulse_24": {
            "length": 24,
            "waveforms": {'Q': 'qubit.qubit_gaussian_pi_pulse_24.waveform.Q', 'I': 'qubit.qubit_gaussian_pi_pulse_24.waveform.I'},
            "integration_weights": {},
            "operation": "control",
        },
        "rr.rr_readout_pulse": {
            "length": 1280,
            "waveforms": {'Q': 'rr.rr_readout_pulse.waveform.Q', 'I': 'rr.rr_readout_pulse.waveform.I'},
            "integration_weights": {'minus_sin': 'rr.rr_readout_pulse.minus_sin', 'sin': 'rr.rr_readout_pulse.sin', 'cos': 'rr.rr_readout_pulse.cos'},
            "operation": "measurement",
        },
        "qubit.qubit_gaussian_pi2_pulse_24": {
            "length": 24,
            "waveforms": {'Q': 'qubit.qubit_gaussian_pi2_pulse_24.waveform.Q', 'I': 'qubit.qubit_gaussian_pi2_pulse_24.waveform.I'},
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "qubit.qubit_gaussian_pi2_pulse_24.waveform.I": {
            "type": "arbitrary",
            "samples": [0.011410299746780378, 0.015914325010438105, 0.02153494823175368, 0.02827247834481747, 0.0360120933470676, 0.04450382031203782, 0.0533593657529302, 0.062070960129838135, 0.07005364008808962, 0.07670742240922568, 0.08149078684690056] + [0.08399318929421015] * 2 + [0.08149078684690056, 0.07670742240922569, 0.07005364008808962, 0.06207096012983814, 0.0533593657529302, 0.04450382031203784, 0.036012093347067606, 0.02827247834481747, 0.02153494823175369, 0.015914325010438116, 0.011410299746780378],
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "rr.rr_readout_pulse.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.008749999999999999] * 640 + [0.0] * 640,
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "qubit.qubit_gaussian_pi_pulse_24.waveform.Q": {
            "type": "arbitrary",
            "samples": [0.0007524961559032438, 0.0009582678421294457, 0.0011732128992160864, 0.0013781363811872318, 0.0015488844600977983, 0.0016588993691936543, 0.0016829946684994155, 0.0016018076701384237, 0.0014060738878650992, 0.001099731816927566, 0.0007009857059508271, 0.00024083714397096816, -0.0002408371439709674, -0.0007009857059508271, -0.0010997318169275656, -0.0014060738878650992, -0.0016018076701384235, -0.0016829946684994155, -0.0016588993691936547, -0.0015488844600977981, -0.0013781363811872318, -0.0011732128992160867, -0.0009582678421294462, -0.0007524961559032438],
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "qubit.qubit_gaussian_pi2_pulse_24.waveform.Q": {
            "type": "arbitrary",
            "samples": [0.0003762480779516219, 0.00047913392106472283, 0.0005866064496080432, 0.0006890681905936159, 0.0007744422300488992, 0.0008294496845968272, 0.0008414973342497077, 0.0008009038350692119, 0.0007030369439325496, 0.000549865908463783, 0.00035049285297541355, 0.00012041857198548408, -0.0001204185719854837, -0.00035049285297541355, -0.0005498659084637828, -0.0007030369439325496, -0.0008009038350692117, -0.0008414973342497077, -0.0008294496845968274, -0.0007744422300488991, -0.0006890681905936159, -0.0005866064496080433, -0.0004791339210647231, -0.0003762480779516219],
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "qubit.qubit_gaussian_pi_pulse_24.waveform.I": {
            "type": "arbitrary",
            "samples": [0.022820599493560755, 0.03182865002087621, 0.04306989646350736, 0.05654495668963494, 0.0720241866941352, 0.08900764062407564, 0.1067187315058604, 0.12414192025967627, 0.14010728017617924, 0.15341484481845136, 0.16298157369380112] + [0.1679863785884203] * 2 + [0.16298157369380112, 0.15341484481845138, 0.14010728017617924, 0.12414192025967628, 0.1067187315058604, 0.08900764062407568, 0.07202418669413521, 0.05654495668963494, 0.04306989646350738, 0.03182865002087623, 0.022820599493560755],
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
    },
    "digital_waveforms": {
        "rr.rr_readout_pulse.ADC_ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "rr.rr_readout_pulse.cos": {
            "cosine": [(-0.02685546875, 64), (0.03436279296875, 64), (0.034820556640625, 64), (0.0902099609375, 64), (-0.00579833984375, 64), (-0.097076416015625, 64), (-0.148223876953125, 64), (-0.014373779296875, 64), (0.0296630859375, 64), (-0.097747802734375, 64), (-0.09478759765625, 64), (-0.26995849609375, 64), (-0.44439697265625, 64), (-0.32989501953125, 64), (-0.254486083984375, 64), (-0.030975341796875, 64), (-0.2650146484375, 64), (-0.3665771484375, 64), (-0.36962890625, 64), (-0.2196044921875, 64)],
            "sine": [(0.08917236328125, 64), (0.0191650390625, 64), (0.352386474609375, 64), (0.33746337890625, 64), (0.514190673828125, 64), (0.424224853515625, 64), (0.607574462890625, 64), (0.642181396484375, 64), (0.65460205078125, 64), (0.920318603515625, 64), (0.8701171875, 64), (0.962860107421875, 64), (0.803466796875, 64), (0.566558837890625, 64), (0.519683837890625, 64), (0.53485107421875, 64), (0.746795654296875, 64), (0.60693359375, 64), (0.638214111328125, 64), (0.579254150390625, 64)],
        },
        "rr.rr_readout_pulse.sin": {
            "cosine": [(-0.08917236328125, 64), (-0.0191650390625, 64), (-0.352386474609375, 64), (-0.33746337890625, 64), (-0.514190673828125, 64), (-0.424224853515625, 64), (-0.607574462890625, 64), (-0.642181396484375, 64), (-0.65460205078125, 64), (-0.920318603515625, 64), (-0.8701171875, 64), (-0.962860107421875, 64), (-0.803466796875, 64), (-0.566558837890625, 64), (-0.519683837890625, 64), (-0.53485107421875, 64), (-0.746795654296875, 64), (-0.60693359375, 64), (-0.638214111328125, 64), (-0.579254150390625, 64)],
            "sine": [(-0.02685546875, 64), (0.03436279296875, 64), (0.034820556640625, 64), (0.0902099609375, 64), (-0.00579833984375, 64), (-0.097076416015625, 64), (-0.148223876953125, 64), (-0.014373779296875, 64), (0.0296630859375, 64), (-0.097747802734375, 64), (-0.09478759765625, 64), (-0.26995849609375, 64), (-0.44439697265625, 64), (-0.32989501953125, 64), (-0.254486083984375, 64), (-0.030975341796875, 64), (-0.2650146484375, 64), (-0.3665771484375, 64), (-0.36962890625, 64), (-0.2196044921875, 64)],
        },
        "rr.rr_readout_pulse.minus_sin": {
            "cosine": [(0.08917236328125, 64), (0.0191650390625, 64), (0.352386474609375, 64), (0.33746337890625, 64), (0.514190673828125, 64), (0.424224853515625, 64), (0.607574462890625, 64), (0.642181396484375, 64), (0.65460205078125, 64), (0.920318603515625, 64), (0.8701171875, 64), (0.962860107421875, 64), (0.803466796875, 64), (0.566558837890625, 64), (0.519683837890625, 64), (0.53485107421875, 64), (0.746795654296875, 64), (0.60693359375, 64), (0.638214111328125, 64), (0.579254150390625, 64)],
            "sine": [(0.02685546875, 64), (-0.03436279296875, 64), (-0.034820556640625, 64), (-0.0902099609375, 64), (0.00579833984375, 64), (0.097076416015625, 64), (0.148223876953125, 64), (0.014373779296875, 64), (-0.0296630859375, 64), (0.097747802734375, 64), (0.09478759765625, 64), (0.26995849609375, 64), (0.44439697265625, 64), (0.32989501953125, 64), (0.254486083984375, 64), (0.030975341796875, 64), (0.2650146484375, 64), (0.3665771484375, 64), (0.36962890625, 64), (0.2196044921875, 64)],
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
