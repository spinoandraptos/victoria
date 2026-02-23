
# Single QUA script generated at 2026-02-23 19:34:23.649248
# QUA library version: 1.2.3


from qm import CompilerOptionArguments
from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    v4 = declare(fixed, )
    with for_(v1,1,(v1<50001),(v1+1)):
        r1 = declare_stream()
        save(v1, r1)
        with for_(v2,0.0,(v2<1.8075),(v2+0.015)):
            r2 = declare_stream()
            save(v2, r2)
            reset_if_phase("cavity")
            reset_frame("cavity")
            align()
            play("cav_displacement"*amp(v2), "cavity")
            align()
            play("qubit_selective_pi"*amp(1.0), "qubit")
            align()
            measure("readout_pulse"*amp(1.0), "rr", dual_demod.full("cos", "sin", v3), dual_demod.full("minus_sin", "cos", v4))
            wait(12500, "rr")
            r3 = declare_stream()
            save(v3, r3)
            r4 = declare_stream()
            save(v4, r4)
    with stream_processing():
        r2.buffer(121).save("cav_ampx")
        r3.buffer(121).save_all("I")
        r3.buffer(121).average().save("I_avg")
        r4.buffer(121).save_all("Q")
        r4.buffer(121).average().save("Q_avg")

config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                "2": {
                    "analog_outputs": {
                        "7": {
                            "full_scale_power_dbm": 7,
                            "upconverters": {
                                "1": {
                                    "frequency": 6335800000.0,
                                },
                            },
                            "band": 2,
                        },
                        "2": {
                            "full_scale_power_dbm": 16,
                            "upconverters": {
                                "1": {
                                    "frequency": 6763200000.0,
                                },
                            },
                            "band": 2,
                        },
                        "1": {
                            "full_scale_power_dbm": -11,
                            "upconverters": {
                                "1": {
                                    "frequency": 7932600000.0,
                                },
                            },
                            "band": 3,
                            "delay": 20,
                        },
                        "4": {
                            "full_scale_power_dbm": 16,
                            "upconverters": {
                                "1": {
                                    "frequency": 3850000000.0,
                                },
                            },
                            "band": 1,
                            "delay": 20,
                        },
                        "5": {
                            "full_scale_power_dbm": 16,
                            "upconverters": {
                                "1": {
                                    "frequency": 2981200000.0,
                                },
                            },
                            "band": 1,
                            "delay": 20,
                        },
                    },
                    "analog_inputs": {
                        "1": {
                            "gain_db": 0,
                            "downconverter_frequency": 7932600000.0,
                            "band": 3,
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
            "intermediate_frequency": -50000000,
            "operations": {
                "qubit_selective_pi": "qubit.qubit_constant_pi_520",
            },
        },
        "cavity": {
            "MWInput": {
                "port": ['con1'] + [2] * 2,
                "upconverter": 1,
            },
            "intermediate_frequency": -50000000,
            "operations": {
                "cav_displacement": "cavity.cav_constant_200",
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
        "qubit.qubit_constant_pi_520": {
            "operation": "control",
            "length": 520,
            "waveforms": {
                "I": "qubit.qubit_constant_pi_520.waveform.I",
                "Q": "qubit.qubit_constant_pi_520.waveform.Q",
            },
        },
        "cavity.cav_constant_200": {
            "operation": "control",
            "length": 200,
            "waveforms": {
                "I": "cavity.cav_constant_200.waveform.I",
                "Q": "cavity.cav_constant_200.waveform.Q",
            },
        },
        "rr.rr_readout_pulse": {
            "operation": "measurement",
            "length": 1600,
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
        "qubit.qubit_constant_pi_520.waveform.I": {
            "type": "constant",
            "sample": 0.016987870880044633,
        },
        "qubit.qubit_constant_pi_520.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cavity.cav_constant_200.waveform.I": {
            "type": "constant",
            "sample": 0.2,
        },
        "cavity.cav_constant_200.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.016] * 1000 + [0.0] * 600,
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
            "cosine": [[1.0, 1600]],
            "sine": [[0.0, 1600]],
        },
        "rr.rr_readout_pulse.sin": {
            "cosine": [[0.0, 1600]],
            "sine": [[1.0, 1600]],
        },
        "rr.rr_readout_pulse.minus_sin": {
            "cosine": [[0.0, 1600]],
            "sine": [[-1.0, 1600]],
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
                            "full_scale_power_dbm": 7,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 6335800000.0,
                                },
                            },
                        },
                        "2": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 16,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 6763200000.0,
                                },
                            },
                        },
                        "1": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -11,
                            "band": 3,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 7932600000.0,
                                },
                            },
                        },
                        "4": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 16,
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 3850000000.0,
                                },
                            },
                        },
                        "5": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 16,
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 2981200000.0,
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
                            "downconverter_frequency": 7932600000.0,
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
                "qubit_selective_pi": "qubit.qubit_constant_pi_520",
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
            "intermediate_frequency": -50000000.0,
        },
        "cavity": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cav_displacement": "cavity.cav_constant_200",
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
                "port": ('con1', 2, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": -50000000.0,
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
        "qubit.qubit_constant_pi_520": {
            "length": 520,
            "waveforms": {
                "I": "qubit.qubit_constant_pi_520.waveform.I",
                "Q": "qubit.qubit_constant_pi_520.waveform.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cavity.cav_constant_200": {
            "length": 200,
            "waveforms": {
                "I": "cavity.cav_constant_200.waveform.I",
                "Q": "cavity.cav_constant_200.waveform.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "rr.rr_readout_pulse": {
            "length": 1600,
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
        "qubit.qubit_constant_pi_520.waveform.I": {
            "type": "constant",
            "sample": 0.016987870880044633,
        },
        "qubit.qubit_constant_pi_520.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cavity.cav_constant_200.waveform.I": {
            "type": "constant",
            "sample": 0.2,
        },
        "cavity.cav_constant_200.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.016] * 1000 + [0.0] * 600,
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
            "cosine": [(1.0, 1600)],
            "sine": [(0.0, 1600)],
        },
        "rr.rr_readout_pulse.sin": {
            "cosine": [(0.0, 1600)],
            "sine": [(1.0, 1600)],
        },
        "rr.rr_readout_pulse.minus_sin": {
            "cosine": [(0.0, 1600)],
            "sine": [(-1.0, 1600)],
        },
    },
    "mixers": {},
}

