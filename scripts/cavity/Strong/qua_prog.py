# Auto-generated standalone QUA execution script
import time
import numpy as np
import matplotlib.pyplot as plt
from qm import QuantumMachinesManager
from qm.qua import *


# Single QUA script generated at 2026-08-26 10:42:23.103457
# QUA library version: 1.3.1


from qm import CompilerOptionArguments
from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    v4 = declare(fixed, )
    with for_(v1,1,(v1<10001),(v1+1)):
        r1 = declare_output_stream()
        save(v1, r1)
        with for_(v2,-2.0,(v2<2.04),(v2+0.08000000000000007)):
            r2 = declare_output_stream()
            save(v2, r2)
            reset_if_phase('cavity')
            reset_if_phase('qubit')
            reset_frame('cavity')
            align()
            play('cavity_pulse'*amp(0.0, (0.0-v2), v2, 0.0), 'cavity')
            align('cavity', 'qubit')
            play('qubit_pulse'*amp(1.0), 'qubit')
            wait(302, 'qubit')
            play('qubit_pulse'*amp(1.0), 'qubit')
            align()
            measure('readout_pulse'*amp(1), 'rr', dual_demod.full("cos", "sin", v3), dual_demod.full("minus_sin", "cos", v4))
            wait(150000, 'rr')
            r3 = declare_output_stream()
            save(v3, r3)
            r4 = declare_output_stream()
            save(v4, r4)
    with stream_processing():
        r2.buffer(51).save("cavity_drive_Q")
        r3.buffer(51).save_all("I")
        r3.buffer(51).average().save("I_avg")
        r4.buffer(51).save_all("Q")
        r4.buffer(51).average().save("Q_avg")

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
            "operations": {'qubit_snap_pi_pulse': 'qubit.qubit_constant_pi_pulse_6000', 'qubit_pulse': 'qubit.qubit_gaussian_pi2_pulse_24'},
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
        "cavity": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {'cavity_pulse': 'cavity.cav_constant_200'},
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 4),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
    },
    "pulses": {
        "qubit.qubit_constant_pi_pulse_6000": {
            "length": 6000,
            "waveforms": {'Q': 'qubit.qubit_constant_pi_pulse_6000.waveform.Q', 'I': 'qubit.qubit_constant_pi_pulse_6000.waveform.I'},
            "integration_weights": {},
            "operation": "control",
        },
        "rr.rr_readout_pulse": {
            "length": 1280,
            "waveforms": {'Q': 'rr.rr_readout_pulse.waveform.Q', 'I': 'rr.rr_readout_pulse.waveform.I'},
            "integration_weights": {'minus_sin': 'rr.rr_readout_pulse.minus_sin', 'sin': 'rr.rr_readout_pulse.sin', 'cos': 'rr.rr_readout_pulse.cos'},
            "operation": "measurement",
        },
        "cavity.cav_constant_200": {
            "length": 200,
            "waveforms": {'Q': 'cavity.cav_constant_200.waveform.Q', 'I': 'cavity.cav_constant_200.waveform.I'},
            "integration_weights": {},
            "operation": "control",
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
        "qubit.qubit_gaussian_pi2_pulse_24.waveform.Q": {
            "type": "arbitrary",
            "samples": [0.0003762480779516219, 0.00047913392106472283, 0.0005866064496080432, 0.0006890681905936159, 0.0007744422300488992, 0.0008294496845968272, 0.0008414973342497077, 0.0008009038350692119, 0.0007030369439325496, 0.000549865908463783, 0.00035049285297541355, 0.00012041857198548408, -0.0001204185719854837, -0.00035049285297541355, -0.0005498659084637828, -0.0007030369439325496, -0.0008009038350692117, -0.0008414973342497077, -0.0008294496845968274, -0.0007744422300488991, -0.0006890681905936159, -0.0005866064496080433, -0.0004791339210647231, -0.0003762480779516219],
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "qubit.qubit_constant_pi_pulse_6000.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cavity.cav_constant_200.waveform.I": {
            "type": "constant",
            "sample": 0.25,
        },
        "cavity.cav_constant_200.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit.qubit_constant_pi_pulse_6000.waveform.I": {
            "type": "constant",
            "sample": 0.0004929752991768496,
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
            "operations": {'qubit_snap_pi_pulse': 'qubit.qubit_constant_pi_pulse_6000', 'qubit_pulse': 'qubit.qubit_gaussian_pi2_pulse_24'},
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
        "cavity": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {'cavity_pulse': 'cavity.cav_constant_200'},
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 4),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
    },
    "pulses": {
        "qubit.qubit_constant_pi_pulse_6000": {
            "length": 6000,
            "waveforms": {'Q': 'qubit.qubit_constant_pi_pulse_6000.waveform.Q', 'I': 'qubit.qubit_constant_pi_pulse_6000.waveform.I'},
            "integration_weights": {},
            "operation": "control",
        },
        "rr.rr_readout_pulse": {
            "length": 1280,
            "waveforms": {'Q': 'rr.rr_readout_pulse.waveform.Q', 'I': 'rr.rr_readout_pulse.waveform.I'},
            "integration_weights": {'minus_sin': 'rr.rr_readout_pulse.minus_sin', 'sin': 'rr.rr_readout_pulse.sin', 'cos': 'rr.rr_readout_pulse.cos'},
            "operation": "measurement",
        },
        "cavity.cav_constant_200": {
            "length": 200,
            "waveforms": {'Q': 'cavity.cav_constant_200.waveform.Q', 'I': 'cavity.cav_constant_200.waveform.I'},
            "integration_weights": {},
            "operation": "control",
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
        "qubit.qubit_gaussian_pi2_pulse_24.waveform.Q": {
            "type": "arbitrary",
            "samples": [0.0003762480779516219, 0.00047913392106472283, 0.0005866064496080432, 0.0006890681905936159, 0.0007744422300488992, 0.0008294496845968272, 0.0008414973342497077, 0.0008009038350692119, 0.0007030369439325496, 0.000549865908463783, 0.00035049285297541355, 0.00012041857198548408, -0.0001204185719854837, -0.00035049285297541355, -0.0005498659084637828, -0.0007030369439325496, -0.0008009038350692117, -0.0008414973342497077, -0.0008294496845968274, -0.0007744422300488991, -0.0006890681905936159, -0.0005866064496080433, -0.0004791339210647231, -0.0003762480779516219],
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "qubit.qubit_constant_pi_pulse_6000.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cavity.cav_constant_200.waveform.I": {
            "type": "constant",
            "sample": 0.25,
        },
        "cavity.cav_constant_200.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit.qubit_constant_pi_pulse_6000.waveform.I": {
            "type": "constant",
            "sample": 0.0004929752991768496,
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
