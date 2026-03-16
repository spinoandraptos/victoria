
# Single QUA script generated at 2026-03-16 17:31:39.737141
# QUA library version: 1.2.6


from qm import CompilerOptionArguments
from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(int, )
    v3 = declare(fixed, )
    v4 = declare(fixed, )
    with for_(v1,1,(v1<3001),(v1+1)):
        r1 = declare_stream()
        save(v1, r1)
        with for_(v2,50000000,(v2<60062500),(v2+125000)):
            r2 = declare_stream()
            save(v2, r2)
            update_frequency("cav", v2, "Hz", False)
            play("cavity_pulse"*amp(1), "cav")
            align("cav", "qubit")
            play("qubit_pulse"*amp(1), "qubit")
            align("qubit", "rr")
            align()
            measure("readout_pulse"*amp(1), "rr", demod.full("cos", v3, ""), demod.full("sin", v4, ""))
            wait(20000, "rr")
            r3 = declare_stream()
            save(v3, r3)
            r4 = declare_stream()
            save(v4, r4)
    with stream_processing():
        r2.buffer(81).save("cavity_frequency")
        r3.buffer(81).save_all("I")
        r3.buffer(81).average().save("I_avg")
        r4.buffer(81).save_all("Q")
        r4.buffer(81).average().save("Q_avg")

config = {
    "controllers": {
        "con1": {
            "type": "opx1",
            "analog_outputs": {
                "7": {
                    "offset": 0.017144775390625002,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "8": {
                    "offset": -0.006228637695312497,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "1": {
                    "offset": 0.0070546144735999395,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "2": {
                    "offset": 0.005051575438119471,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "5": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "6": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
            },
            "analog_inputs": {
                "1": {
                    "offset": -0.020806603064903846,
                    "gain_db": 0,
                    "shareable": False,
                    "sampling_rate": 1000000000.0,
                },
            },
            "digital_outputs": {},
            "digital_inputs": {},
        },
    },
    "oscillators": {},
    "elements": {
        "rr": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 1, 1),
            },
            "operations": {
                "readout_pulse": "rr.rr_readout_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "mixInputs": {
                "I": ('con1', 1, 5),
                "Q": ('con1', 1, 6),
                "mixer": "mixer_56",
                "lo_frequency": 7927850000.0,
            },
            "smearing": 0,
            "time_of_flight": 272,
            "intermediate_frequency": 50000000.0,
        },
        "qubit": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "qubit_pulse": "qubit.qubit_constant_pi_pulse_400",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "mixInputs": {
                "I": ('con1', 1, 1),
                "Q": ('con1', 1, 2),
                "mixer": "mixer_12",
                "lo_frequency": 6195000000.0,
            },
            "intermediate_frequency": 68000000.0,
        },
        "cav": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cavity_pulse": "cav.cavity_constant_pulse_5000_weaker",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "mixInputs": {
                "I": ('con1', 1, 7),
                "Q": ('con1', 1, 8),
                "mixer": "mixer_78",
                "lo_frequency": 6665900000.0,
            },
            "intermediate_frequency": 53200000.0,
        },
    },
    "pulses": {
        "rr.rr_readout_pulse": {
            "length": 1200,
            "waveforms": {
                "I": "rr.rr_readout_pulse.waveform.I",
                "Q": "rr.rr_readout_pulse.waveform.Q",
            },
            "integration_weights": {
                "cos": "rr.rr_readout_pulse.cos",
                "sin": "rr.rr_readout_pulse.sin",
                "minus_sin": "rr.rr_readout_pulse.minus_sin",
            },
            "operation": "measurement",
            "digital_marker": "rr.rr_readout_pulse.ADC_ON",
        },
        "qubit.qubit_constant_pi_pulse_400": {
            "length": 400,
            "waveforms": {
                "I": "qubit.qubit_constant_pi_pulse_400.waveform.I",
                "Q": "qubit.qubit_constant_pi_pulse_400.waveform.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cav.cavity_constant_pulse_5000_weaker": {
            "length": 5000,
            "waveforms": {
                "I": "cav.cavity_constant_pulse_5000_weaker.waveform.I",
                "Q": "cav.cavity_constant_pulse_5000_weaker.waveform.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.04000000000000001] * 600 + [0.0] * 600,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "qubit.qubit_constant_pi_pulse_400.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cav.cavity_constant_pulse_5000_weaker.waveform.I": {
            "type": "constant",
            "sample": 0.12,
        },
        "rr.rr_readout_pulse.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit.qubit_constant_pi_pulse_400.waveform.I": {
            "type": "constant",
            "sample": 0.0029411764705882353,
        },
        "cav.cavity_constant_pulse_5000_weaker.waveform.Q": {
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
            "cosine": [(0.0, 1200)],
            "sine": [(1.0, 1200)],
        },
        "rr.rr_readout_pulse.cos": {
            "cosine": [(1.0, 1200)],
            "sine": [(0.0, 1200)],
        },
        "rr.rr_readout_pulse.minus_sin": {
            "cosine": [(0.0, 1200)],
            "sine": [(-1.0, 1200)],
        },
    },
    "mixers": {
        "mixer_78": [{'intermediate_frequency': 53200000.0, 'lo_frequency': 6665900000.0, 'correction': (0.8720115627090465, 0.18532169822217195, 0.12762627412904967, 1.2662178283697718)}],
        "mixer_12": [{'intermediate_frequency': 68000000.0, 'lo_frequency': 6195000000.0, 'correction': (0.8763427734259319, 0.25014736807116766, 0.16534419700682, 1.325809083530416)}],
        "mixer_56": [{'intermediate_frequency': 50000000.0, 'lo_frequency': 7927850000.0, 'correction': (0.8541443821454708, 0.039738479275730335, 0.028036675251831063, 1.2106427928237504)}],
    },
}

loaded_config = {
    "controllers": {
        "con1": {
            "type": "opx1",
            "analog_outputs": {
                "7": {
                    "offset": 0.017144775390625002,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "8": {
                    "offset": -0.006228637695312497,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "1": {
                    "offset": 0.0070546144735999395,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "2": {
                    "offset": 0.005051575438119471,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "5": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "6": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
            },
            "analog_inputs": {
                "1": {
                    "offset": -0.020806603064903846,
                    "gain_db": 0,
                    "shareable": False,
                    "sampling_rate": 1000000000.0,
                },
            },
            "digital_outputs": {},
            "digital_inputs": {},
        },
    },
    "oscillators": {},
    "elements": {
        "rr": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 1, 1),
            },
            "operations": {
                "readout_pulse": "rr.rr_readout_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "mixInputs": {
                "I": ('con1', 1, 5),
                "Q": ('con1', 1, 6),
                "mixer": "mixer_56",
                "lo_frequency": 7927850000.0,
            },
            "smearing": 0,
            "time_of_flight": 272,
            "intermediate_frequency": 50000000.0,
        },
        "qubit": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "qubit_pulse": "qubit.qubit_constant_pi_pulse_400",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "mixInputs": {
                "I": ('con1', 1, 1),
                "Q": ('con1', 1, 2),
                "mixer": "mixer_12",
                "lo_frequency": 6195000000.0,
            },
            "intermediate_frequency": 68000000.0,
        },
        "cav": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cavity_pulse": "cav.cavity_constant_pulse_5000_weaker",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "mixInputs": {
                "I": ('con1', 1, 7),
                "Q": ('con1', 1, 8),
                "mixer": "mixer_78",
                "lo_frequency": 6665900000.0,
            },
            "intermediate_frequency": 53200000.0,
        },
    },
    "pulses": {
        "rr.rr_readout_pulse": {
            "length": 1200,
            "waveforms": {
                "I": "rr.rr_readout_pulse.waveform.I",
                "Q": "rr.rr_readout_pulse.waveform.Q",
            },
            "integration_weights": {
                "cos": "rr.rr_readout_pulse.cos",
                "sin": "rr.rr_readout_pulse.sin",
                "minus_sin": "rr.rr_readout_pulse.minus_sin",
            },
            "operation": "measurement",
            "digital_marker": "rr.rr_readout_pulse.ADC_ON",
        },
        "qubit.qubit_constant_pi_pulse_400": {
            "length": 400,
            "waveforms": {
                "I": "qubit.qubit_constant_pi_pulse_400.waveform.I",
                "Q": "qubit.qubit_constant_pi_pulse_400.waveform.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cav.cavity_constant_pulse_5000_weaker": {
            "length": 5000,
            "waveforms": {
                "I": "cav.cavity_constant_pulse_5000_weaker.waveform.I",
                "Q": "cav.cavity_constant_pulse_5000_weaker.waveform.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.04000000000000001] * 600 + [0.0] * 600,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "qubit.qubit_constant_pi_pulse_400.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cav.cavity_constant_pulse_5000_weaker.waveform.I": {
            "type": "constant",
            "sample": 0.12,
        },
        "rr.rr_readout_pulse.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit.qubit_constant_pi_pulse_400.waveform.I": {
            "type": "constant",
            "sample": 0.0029411764705882353,
        },
        "cav.cavity_constant_pulse_5000_weaker.waveform.Q": {
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
            "cosine": [(0.0, 1200)],
            "sine": [(1.0, 1200)],
        },
        "rr.rr_readout_pulse.cos": {
            "cosine": [(1.0, 1200)],
            "sine": [(0.0, 1200)],
        },
        "rr.rr_readout_pulse.minus_sin": {
            "cosine": [(0.0, 1200)],
            "sine": [(-1.0, 1200)],
        },
    },
    "mixers": {
        "mixer_78": [{'intermediate_frequency': 53200000.0, 'lo_frequency': 6665900000.0, 'correction': (0.8720115627090465, 0.18532169822217195, 0.12762627412904967, 1.2662178283697718)}],
        "mixer_12": [{'intermediate_frequency': 68000000.0, 'lo_frequency': 6195000000.0, 'correction': (0.8763427734259319, 0.25014736807116766, 0.16534419700682, 1.325809083530416)}],
        "mixer_56": [{'intermediate_frequency': 50000000.0, 'lo_frequency': 7927850000.0, 'correction': (0.8541443821454708, 0.039738479275730335, 0.028036675251831063, 1.2106427928237504)}],
    },
}

