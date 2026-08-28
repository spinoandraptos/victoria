
# Single QUA script generated at 2026-04-01 17:46:40.661960
# QUA library version: 1.2.6


from qm import CompilerOptionArguments
from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(int, )
    v4 = declare(fixed, )
    v5 = declare(fixed, )
    a1 = declare(fixed, value=[0.1, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    with for_(v1,1,(v1<100001),(v1+1)):
        r1 = declare_stream()
        save(v1, r1)
        with for_each_((v2),(a1)):
            r2 = declare_stream()
            save(v2, r2)
            with for_(v3,-60000000,(v3<-39900000),(v3+200000)):
                r3 = declare_stream()
                save(v3, r3)
                update_frequency("rr", v3, "Hz", False)
                measure("readout_pulse"*amp(v2), "rr", demod.full("cos", v4, ""), demod.full("sin", v5, ""))
                wait(2500, "rr")
                r4 = declare_stream()
                save(v4, r4)
                r5 = declare_stream()
                save(v5, r5)
    with stream_processing():
        r2.buffer(8).save("ro_ampx")
        r3.buffer(101).save("resonator_frequency")
        r4.buffer(8, 101).save_all("I")
        r4.buffer(8, 101).average().save("I_avg")
        r5.buffer(8, 101).save_all("Q")
        r5.buffer(8, 101).average().save("Q_avg")

config = {
    "controllers": {
        "con1": {
            "type": "opx1",
            "analog_outputs": {
                "5": {
                    "offset": -0.01250000000000005,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "6": {
                    "offset": -0.02343749999999998,
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
                "lo_frequency": 7343510000.0,
            },
            "smearing": 0,
            "time_of_flight": 272,
            "intermediate_frequency": -50000000.0,
        },
    },
    "pulses": {
        "rr.rr_readout_pulse": {
            "length": 700,
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
    },
    "waveforms": {
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.2] * 400 + [0.0] * 300,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
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
            "cosine": [(0.0, 700)],
            "sine": [(1.0, 700)],
        },
        "rr.rr_readout_pulse.cos": {
            "cosine": [(1.0, 700)],
            "sine": [(0.0, 700)],
        },
        "rr.rr_readout_pulse.minus_sin": {
            "cosine": [(0.0, 700)],
            "sine": [(-1.0, 700)],
        },
    },
    "mixers": {
        "mixer_56": [{'intermediate_frequency': -50000000.0, 'lo_frequency': 7343510000.0, 'correction': (1.007888779755844, -0.003100830709868901, -0.0031496626895518754, 0.9922625971239705)}],
    },
}

loaded_config = {
    "controllers": {
        "con1": {
            "type": "opx1",
            "analog_outputs": {
                "5": {
                    "offset": -0.01250000000000005,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "6": {
                    "offset": -0.02343749999999998,
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
                "lo_frequency": 7343510000.0,
            },
            "smearing": 0,
            "time_of_flight": 272,
            "intermediate_frequency": -50000000.0,
        },
    },
    "pulses": {
        "rr.rr_readout_pulse": {
            "length": 700,
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
    },
    "waveforms": {
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.2] * 400 + [0.0] * 300,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
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
            "cosine": [(0.0, 700)],
            "sine": [(1.0, 700)],
        },
        "rr.rr_readout_pulse.cos": {
            "cosine": [(1.0, 700)],
            "sine": [(0.0, 700)],
        },
        "rr.rr_readout_pulse.minus_sin": {
            "cosine": [(0.0, 700)],
            "sine": [(-1.0, 700)],
        },
    },
    "mixers": {
        "mixer_56": [{'intermediate_frequency': -50000000.0, 'lo_frequency': 7343510000.0, 'correction': (1.007888779755844, -0.003100830709868901, -0.0031496626895518754, 0.9922625971239705)}],
    },
}

