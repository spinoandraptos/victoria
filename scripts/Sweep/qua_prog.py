
# Single QUA script generated at 2026-02-27 02:46:36.399869
# QUA library version: 1.2.3


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
        with for_(v2,-200000000,(v2<200666667),(v2+1333333)):
            r2 = declare_stream()
            save(v2, r2)
            reset_if_phase("rr")
            update_frequency("qubit", v2, "Hz", False)
            play("qubit_drive"*amp(1.0), "qubit")
            align()
            measure("readout_pulse"*amp(1.0), "rr", dual_demod.full("cos", "sin", v3), dual_demod.full("minus_sin", "cos", v4))
            wait(1500, "rr")
            r3 = declare_stream()
            save(v3, r3)
            r4 = declare_stream()
            save(v4, r4)
    with stream_processing():
        r2.buffer(301).save("qubit_frequency")
        r3.buffer(301).save_all("I")
        r3.buffer(301).average().save("I_avg")
        r4.buffer(301).save_all("Q")
        r4.buffer(301).average().save("Q_avg")

config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                "2": {
                    "analog_outputs": {
                        "7": {
                            "full_scale_power_dbm": 16,
                            "upconverters": {
                                "1": {
                                    "frequency": 5400000000.0,
                                },
                            },
                            "band": 2,
                        },
                        "1": {
                            "full_scale_power_dbm": -11,
                            "upconverters": {
                                "1": {
                                    "frequency": 3918011000.0,
                                },
                            },
                            "band": 1,
                            "delay": 20,
                        },
                    },
                    "analog_inputs": {
                        "1": {
                            "gain_db": 0,
                            "downconverter_frequency": 3918011000.0,
                            "band": 1,
                        },
                    },
                    "type": "MW",
                },
                "1": {
                    "type": "MW",
                    "analog_outputs": {},
                    "analog_inputs": {},
                },
            },
        },
    },
    "elements": {
        "qubit": {
            "MWInput": {
                "port": ['con1', 2, 7],
                "upconverter": 1,
            },
            "intermediate_frequency": -20000000,
            "operations": {
                "qubit_drive": "qubit.qubit_constant_pi_1500",
            },
        },
        "rr": {
            "MWInput": {
                "port": ['con1', 2, 1],
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ['con1', 2, 1],
            },
            "intermediate_frequency": -50000000,
            "time_of_flight": 300,
            "smearing": 0,
            "operations": {
                "readout_pulse": "rr.rr_readout_pulse",
            },
        },
    },
    "pulses": {
        "qubit.qubit_constant_pi_1500": {
            "operation": "control",
            "length": 1500,
            "waveforms": {
                "I": "qubit.qubit_constant_pi_1500.waveform.I",
                "Q": "qubit.qubit_constant_pi_1500.waveform.Q",
            },
        },
        "rr.rr_readout_pulse": {
            "operation": "measurement",
            "length": 1200,
            "waveforms": {
                "I": "rr.rr_readout_pulse.waveform.I",
                "Q": "rr.rr_readout_pulse.waveform.Q",
            },
            "digital_marker": "rr.rr_readout_pulse.ADC_ON",
            "integration_weights": {
                "cos": "rr.rr_readout_pulse.cos",
                "sin": "rr.rr_readout_pulse.sin",
                "minus_sin": "rr.rr_readout_pulse.minus_sin",
            },
        },
    },
    "waveforms": {
        "qubit.qubit_constant_pi_1500.waveform.I": {
            "type": "constant",
            "sample": 0.020000000000000004,
        },
        "qubit.qubit_constant_pi_1500.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.04000000000000001] * 600 + [0.0] * 600,
        },
        "rr.rr_readout_pulse.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
    },
    "digital_waveforms": {
        "rr.rr_readout_pulse.ADC_ON": {
            "samples": [[1, 0]],
        },
    },
    "integration_weights": {
        "rr.rr_readout_pulse.cos": {
            "cosine": [[1.0, 1200]],
            "sine": [[0.0, 1200]],
        },
        "rr.rr_readout_pulse.sin": {
            "cosine": [[0.0, 1200]],
            "sine": [[1.0, 1200]],
        },
        "rr.rr_readout_pulse.minus_sin": {
            "cosine": [[0.0, 1200]],
            "sine": [[-1.0, 1200]],
        },
    },
}

loaded_config = {
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                "2": {
                    "type": "MW",
                    "analog_outputs": {
                        "7": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 16,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 5400000000.0,
                                },
                            },
                        },
                        "1": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -11,
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 3918011000.0,
                                },
                            },
                        },
                    },
                    "analog_inputs": {
                        "1": {
                            "band": 1,
                            "shareable": False,
                            "gain_db": 0,
                            "sampling_rate": 1000000000.0,
                            "downconverter_frequency": 3918011000.0,
                        },
                    },
                },
                "1": {
                    "type": "MW",
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
            "operations": {
                "qubit_drive": "qubit.qubit_constant_pi_1500",
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
                "port": ('con1', 2, 7),
                "upconverter": 1,
            },
            "intermediate_frequency": -20000000.0,
        },
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
                "port": ('con1', 2, 1),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 2, 1),
            },
            "smearing": 0,
            "time_of_flight": 300,
            "intermediate_frequency": -50000000.0,
        },
    },
    "pulses": {
        "qubit.qubit_constant_pi_1500": {
            "length": 1500,
            "waveforms": {
                "I": "qubit.qubit_constant_pi_1500.waveform.I",
                "Q": "qubit.qubit_constant_pi_1500.waveform.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
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
    },
    "waveforms": {
        "qubit.qubit_constant_pi_1500.waveform.I": {
            "type": "constant",
            "sample": 0.020000000000000004,
        },
        "qubit.qubit_constant_pi_1500.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.04000000000000001] * 600 + [0.0] * 600,
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
        "rr.rr_readout_pulse.cos": {
            "cosine": [(1.0, 1200)],
            "sine": [(0.0, 1200)],
        },
        "rr.rr_readout_pulse.sin": {
            "cosine": [(0.0, 1200)],
            "sine": [(1.0, 1200)],
        },
        "rr.rr_readout_pulse.minus_sin": {
            "cosine": [(0.0, 1200)],
            "sine": [(-1.0, 1200)],
        },
    },
    "mixers": {},
}

