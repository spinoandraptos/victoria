
# Single QUA script generated at 2026-03-16 14:21:26.324276
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
            update_frequency("rr", v2, "Hz", False)
            measure("readout_pulse"*amp(1), "rr", dual_demod.full("cos", "sin", v3), dual_demod.full("minus_sin", "cos", v4))
            wait(2500, "rr")
            r3 = declare_stream()
            save(v3, r3)
            r4 = declare_stream()
            save(v4, r4)
    with stream_processing():
        r2.buffer(1001).save("resonator_frequency")
        r3.buffer(1001).save_all("I")
        r3.buffer(1001).average().save("I_avg")
        r4.buffer(1001).save_all("Q")
        r4.buffer(1001).average().save("Q_avg")

config = {
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                "8": {
                    "type": "MW",
                    "analog_outputs": {
                        "1": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 16,
                            "band": 3,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 7831635520.0,
                                },
                            },
                        },
                        "3": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 16,
                            "band": 3,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 7463300000.0,
                                },
                            },
                        },
                        "5": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 16,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 5935800000.0,
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
                            "downconverter_frequency": 7831635520.0,
                        },
                    },
                },
                "1": {
                    "type": "MW",
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
        "rr": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
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
            "MWInput": {
                "port": ('con1', 8, 1),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 8, 1),
            },
            "smearing": 0,
            "time_of_flight": 300,
            "intermediate_frequency": -50000000.0,
        },
    },
    "pulses": {
        "rr.rr_readout_pulse": {
            "length": 5600,
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
            "samples": [0.2] * 5000 + [0.0] * 600,
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
            "cosine": [(0.0, 5600)],
            "sine": [(1.0, 5600)],
        },
        "rr.rr_readout_pulse.cos": {
            "cosine": [(1.0, 5600)],
            "sine": [(0.0, 5600)],
        },
        "rr.rr_readout_pulse.minus_sin": {
            "cosine": [(0.0, 5600)],
            "sine": [(-1.0, 5600)],
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
                    "analog_outputs": {
                        "1": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 16,
                            "band": 3,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 7831635520.0,
                                },
                            },
                        },
                        "3": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 16,
                            "band": 3,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 7463300000.0,
                                },
                            },
                        },
                        "5": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 16,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 5935800000.0,
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
                            "downconverter_frequency": 7831635520.0,
                        },
                    },
                },
                "1": {
                    "type": "MW",
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
        "rr": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
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
            "MWInput": {
                "port": ('con1', 8, 1),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 8, 1),
            },
            "smearing": 0,
            "time_of_flight": 300,
            "intermediate_frequency": -50000000.0,
        },
    },
    "pulses": {
        "rr.rr_readout_pulse": {
            "length": 5600,
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
            "samples": [0.2] * 5000 + [0.0] * 600,
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
            "cosine": [(0.0, 5600)],
            "sine": [(1.0, 5600)],
        },
        "rr.rr_readout_pulse.cos": {
            "cosine": [(1.0, 5600)],
            "sine": [(0.0, 5600)],
        },
        "rr.rr_readout_pulse.minus_sin": {
            "cosine": [(0.0, 5600)],
            "sine": [(-1.0, 5600)],
        },
    },
    "mixers": {},
}

