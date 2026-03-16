
# Single QUA script generated at 2026-03-16 13:39:22.798563
# QUA library version: 1.2.6


from qm import CompilerOptionArguments
from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(int, )
    v3 = declare(fixed, )
    v4 = declare(fixed, )
    with for_(v1,1,(v1<50001),(v1+1)):
        r1 = declare_stream()
        save(v1, r1)
        with for_(v2,-200000000,(v2<202000000),(v2+4000000)):
            r2 = declare_stream()
            save(v2, r2)
            play("qubit_pi_pulse"*amp(1.0), "qubit")
            align("qubit", "qubitEF")
            update_frequency("qubitEF", v2, "Hz", False)
            play("qubitEF_drive"*amp(1.0), "qubitEF")
            align("qubit", "qubitEF")
            play("qubit_pi_pulse"*amp(1.0), "qubit")
            align("rr", "qubit")
            measure("readout_pulse"*amp(1), "rr", demod.full("cos", v3, ""), demod.full("sin", v4, ""))
            wait(2000, "rr")
            r3 = declare_stream()
            save(v3, r3)
            r4 = declare_stream()
            save(v4, r4)
    with stream_processing():
        r2.buffer(101).save("qubitEF_frequency")
        r3.buffer(101).save_all("I")
        r3.buffer(101).average().save("I_avg")
        r4.buffer(101).save_all("Q")
        r4.buffer(101).average().save("Q_avg")

config = {
    "controllers": {
        "con1": {
            "type": "opx1",
            "analog_outputs": {
                "1": {
                    "offset": 0.0071526846615597595,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "2": {
                    "offset": 0.005089394142851233,
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
                "lo_frequency": 7731635520.0,
            },
            "smearing": 0,
            "time_of_flight": 272,
            "intermediate_frequency": -49790000.0,
        },
        "qubit": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "qubit_pi_pulse": "qubit.qubit_constant_pi_pulse_16",
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
                "lo_frequency": 6410200000.0,
            },
            "intermediate_frequency": 100000000.0,
        },
        "qubitEF": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "qubitEF_drive": "qubitEF.qubitEF_constant_pulse_10000",
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
                "lo_frequency": 6410200000.0,
            },
            "intermediate_frequency": -124600000.0,
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
        "qubitEF.qubitEF_constant_pulse_10000": {
            "length": 10000,
            "waveforms": {
                "I": "qubitEF.qubitEF_constant_pulse_10000.waveform.I",
                "Q": "qubitEF.qubitEF_constant_pulse_10000.waveform.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "qubit.qubit_constant_pi_pulse_16": {
            "length": 16,
            "waveforms": {
                "I": "qubit.qubit_constant_pi_pulse_16.waveform.I",
                "Q": "qubit.qubit_constant_pi_pulse_16.waveform.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.1] * 600 + [0.0] * 600,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "qubit.qubit_constant_pi_pulse_16.waveform.I": {
            "type": "constant",
            "sample": 0.11363636363636365,
        },
        "qubitEF.qubitEF_constant_pulse_10000.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "rr.rr_readout_pulse.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit.qubit_constant_pi_pulse_16.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubitEF.qubitEF_constant_pulse_10000.waveform.I": {
            "type": "constant",
            "sample": 0.1,
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
        "mixer_12": [
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 6410200000.0, 'correction': (0.8763427734259319, 0.25014736807116766, 0.16534419700682, 1.325809083530416)},
            {'intermediate_frequency': -124600000.0, 'lo_frequency': 6410200000.0, 'correction': (0.8560976043586231, -0.12962779773615266, -0.08876352406551911, 1.2502212847958925)},
        ],
        "mixer_56": [{'intermediate_frequency': -49790000.0, 'lo_frequency': 7731635520.0, 'correction': (0.8541443821454708, 0.039738479275730335, 0.028036675251831063, 1.2106427928237504)}],
    },
}

loaded_config = {
    "controllers": {
        "con1": {
            "type": "opx1",
            "analog_outputs": {
                "1": {
                    "offset": 0.0071526846615597595,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "2": {
                    "offset": 0.005089394142851233,
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
                "lo_frequency": 7731635520.0,
            },
            "smearing": 0,
            "time_of_flight": 272,
            "intermediate_frequency": -49790000.0,
        },
        "qubit": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "qubit_pi_pulse": "qubit.qubit_constant_pi_pulse_16",
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
                "lo_frequency": 6410200000.0,
            },
            "intermediate_frequency": 100000000.0,
        },
        "qubitEF": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "qubitEF_drive": "qubitEF.qubitEF_constant_pulse_10000",
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
                "lo_frequency": 6410200000.0,
            },
            "intermediate_frequency": -124600000.0,
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
        "qubitEF.qubitEF_constant_pulse_10000": {
            "length": 10000,
            "waveforms": {
                "I": "qubitEF.qubitEF_constant_pulse_10000.waveform.I",
                "Q": "qubitEF.qubitEF_constant_pulse_10000.waveform.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "qubit.qubit_constant_pi_pulse_16": {
            "length": 16,
            "waveforms": {
                "I": "qubit.qubit_constant_pi_pulse_16.waveform.I",
                "Q": "qubit.qubit_constant_pi_pulse_16.waveform.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.1] * 600 + [0.0] * 600,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "qubit.qubit_constant_pi_pulse_16.waveform.I": {
            "type": "constant",
            "sample": 0.11363636363636365,
        },
        "qubitEF.qubitEF_constant_pulse_10000.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "rr.rr_readout_pulse.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit.qubit_constant_pi_pulse_16.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubitEF.qubitEF_constant_pulse_10000.waveform.I": {
            "type": "constant",
            "sample": 0.1,
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
        "mixer_12": [
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 6410200000.0, 'correction': (0.8763427734259319, 0.25014736807116766, 0.16534419700682, 1.325809083530416)},
            {'intermediate_frequency': -124600000.0, 'lo_frequency': 6410200000.0, 'correction': (0.8560976043586231, -0.12962779773615266, -0.08876352406551911, 1.2502212847958925)},
        ],
        "mixer_56": [{'intermediate_frequency': -49790000.0, 'lo_frequency': 7731635520.0, 'correction': (0.8541443821454708, 0.039738479275730335, 0.028036675251831063, 1.2106427928237504)}],
    },
}

