
# Single QUA script generated at 2026-03-26 15:01:06.734278
# QUA library version: 1.2.6


from qm import CompilerOptionArguments
from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(int, )
    v3 = declare(fixed, )
    v4 = declare(fixed, )
    with for_(v1,1,(v1<100001),(v1+1)):
        r1 = declare_stream()
        save(v1, r1)
        with for_(v2,-200000000,(v2<200200000),(v2+400000)):
            r2 = declare_stream()
            save(v2, r2)
            update_frequency("cav", v2, "Hz", False)
            play("cavity_pulse"*amp(1), "cav")
            align("cav", "qubit")
            play("qubit_pulse"*amp(1), "qubit")
            align("qubit", "rr")
            align()
            measure("readout_pulse"*amp(1), "rr", demod.full("cos", v3, ""), demod.full("sin", v4, ""))
            wait(200000, "rr")
            r3 = declare_stream()
            save(v3, r3)
            r4 = declare_stream()
            save(v4, r4)
    with stream_processing():
        r2.buffer(1001).save("cavity_frequency")
        r3.buffer(1001).save_all("I")
        r3.buffer(1001).average().save("I_avg")
        r4.buffer(1001).save_all("Q")
        r4.buffer(1001).average().save("Q_avg")

config = {
    "controllers": {
        "con1": {
            "type": "opx1",
            "analog_outputs": {
                "7": {
                    "offset": -0.01581861060694792,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "8": {
                    "offset": -0.0017682625242742,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "1": {
                    "offset": -0.0023203855264000636,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "2": {
                    "offset": -0.0043234245618805345,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "5": {
                    "offset": -0.01875000000000006,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "6": {
                    "offset": -0.021874999999999985,
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
                "lo_frequency": 7665050000.0,
            },
            "smearing": 0,
            "time_of_flight": 272,
            "intermediate_frequency": -49400000.0,
        },
        "qubit": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "qubit_pulse": "qubit.qubit_constant_pi_pulse_320",
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
                "lo_frequency": 5500000000.0,
            },
            "intermediate_frequency": 113000000.0,
        },
        "cav": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cavity_pulse": "cav.cav_constant_pulse_100000",
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
                "lo_frequency": 7190000000.0,
            },
            "intermediate_frequency": -110000000.0,
        },
    },
    "pulses": {
        "rr.rr_readout_pulse": {
            "length": 900,
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
        "cav.cav_constant_pulse_100000": {
            "length": 100000,
            "waveforms": {
                "I": "cav.cav_constant_pulse_100000.waveform.I",
                "Q": "cav.cav_constant_pulse_100000.waveform.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "qubit.qubit_constant_pi_pulse_320": {
            "length": 320,
            "waveforms": {
                "I": "qubit.qubit_constant_pi_pulse_320.waveform.I",
                "Q": "qubit.qubit_constant_pi_pulse_320.waveform.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "cav.cav_constant_pulse_100000.waveform.I": {
            "type": "constant",
            "sample": 0.39,
        },
        "qubit.qubit_constant_pi_pulse_320.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.39] * 600 + [0.0] * 300,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cav.cav_constant_pulse_100000.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit.qubit_constant_pi_pulse_320.waveform.I": {
            "type": "constant",
            "sample": 0.054000000000000006,
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
            "cosine": [(0.0, 900)],
            "sine": [(1.0, 900)],
        },
        "rr.rr_readout_pulse.cos": {
            "cosine": [(1.0, 900)],
            "sine": [(0.0, 900)],
        },
        "rr.rr_readout_pulse.minus_sin": {
            "cosine": [(0.0, 900)],
            "sine": [(-1.0, 900)],
        },
    },
    "mixers": {
        "mixer_78": [{'intermediate_frequency': -110000000.0, 'lo_frequency': 7190000000.0, 'correction': (1.0257587616707644, -0.12813655070485927, -0.12859657855134368, 1.0220893203881138)}],
        "mixer_12": [{'intermediate_frequency': 113000000.0, 'lo_frequency': 5500000000.0, 'correction': (1.0299725369555166, -0.10997229407336097, -0.1125359829460764, 1.0065086717715193)}],
        "mixer_56": [{'intermediate_frequency': -49400000.0, 'lo_frequency': 7665050000.0, 'correction': (0.9947094424941693, 0.07022825320852472, 0.06849422226510436, 1.019891960025667)}],
    },
}

loaded_config = {
    "controllers": {
        "con1": {
            "type": "opx1",
            "analog_outputs": {
                "7": {
                    "offset": -0.01581861060694792,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "8": {
                    "offset": -0.0017682625242742,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "1": {
                    "offset": -0.0023203855264000636,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "2": {
                    "offset": -0.0043234245618805345,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "5": {
                    "offset": -0.01875000000000006,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "6": {
                    "offset": -0.021874999999999985,
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
                "lo_frequency": 7665050000.0,
            },
            "smearing": 0,
            "time_of_flight": 272,
            "intermediate_frequency": -49400000.0,
        },
        "qubit": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "qubit_pulse": "qubit.qubit_constant_pi_pulse_320",
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
                "lo_frequency": 5500000000.0,
            },
            "intermediate_frequency": 113000000.0,
        },
        "cav": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cavity_pulse": "cav.cav_constant_pulse_100000",
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
                "lo_frequency": 7190000000.0,
            },
            "intermediate_frequency": -110000000.0,
        },
    },
    "pulses": {
        "rr.rr_readout_pulse": {
            "length": 900,
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
        "cav.cav_constant_pulse_100000": {
            "length": 100000,
            "waveforms": {
                "I": "cav.cav_constant_pulse_100000.waveform.I",
                "Q": "cav.cav_constant_pulse_100000.waveform.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "qubit.qubit_constant_pi_pulse_320": {
            "length": 320,
            "waveforms": {
                "I": "qubit.qubit_constant_pi_pulse_320.waveform.I",
                "Q": "qubit.qubit_constant_pi_pulse_320.waveform.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "cav.cav_constant_pulse_100000.waveform.I": {
            "type": "constant",
            "sample": 0.39,
        },
        "qubit.qubit_constant_pi_pulse_320.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.39] * 600 + [0.0] * 300,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cav.cav_constant_pulse_100000.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit.qubit_constant_pi_pulse_320.waveform.I": {
            "type": "constant",
            "sample": 0.054000000000000006,
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
            "cosine": [(0.0, 900)],
            "sine": [(1.0, 900)],
        },
        "rr.rr_readout_pulse.cos": {
            "cosine": [(1.0, 900)],
            "sine": [(0.0, 900)],
        },
        "rr.rr_readout_pulse.minus_sin": {
            "cosine": [(0.0, 900)],
            "sine": [(-1.0, 900)],
        },
    },
    "mixers": {
        "mixer_78": [{'intermediate_frequency': -110000000.0, 'lo_frequency': 7190000000.0, 'correction': (1.0257587616707644, -0.12813655070485927, -0.12859657855134368, 1.0220893203881138)}],
        "mixer_12": [{'intermediate_frequency': 113000000.0, 'lo_frequency': 5500000000.0, 'correction': (1.0299725369555166, -0.10997229407336097, -0.1125359829460764, 1.0065086717715193)}],
        "mixer_56": [{'intermediate_frequency': -49400000.0, 'lo_frequency': 7665050000.0, 'correction': (0.9947094424941693, 0.07022825320852472, 0.06849422226510436, 1.019891960025667)}],
    },
}

