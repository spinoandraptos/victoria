
# Single QUA script generated at 2026-02-25 17:40:02.999297
# QUA library version: 1.2.3


from qm import CompilerOptionArguments
from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(int, )
    v4 = declare(fixed, )
    v5 = declare(fixed, )
    a1 = declare(fixed, value=[1.0, 1.5, 2.0])
    with for_(v1,1,(v1<100001),(v1+1)):
        r1 = declare_stream()
        save(v1, r1)
        with for_each_((v2),(a1)):
            r2 = declare_stream()
            save(v2, r2)
            with for_(v3,-60000000,(v3<-39900000),(v3+200000)):
                r3 = declare_stream()
                save(v3, r3)
                update_frequency("rr_MR", v3, "Hz", False)
                measure("readout_pulse"*amp(v2), "rr_MR", dual_demod.full("cos", "sin", v4), dual_demod.full("minus_sin", "cos", v5))
                wait(1250, "rr_MR")
                r4 = declare_stream()
                save(v4, r4)
                r5 = declare_stream()
                save(v5, r5)
    with stream_processing():
        r2.buffer(3).save("ro_ampx")
        r3.buffer(101).save("resonator_frequency")
        r4.buffer(3, 101).save_all("I")
        r4.buffer(3, 101).average().save("I_avg")
        r5.buffer(3, 101).save_all("Q")
        r5.buffer(3, 101).average().save("Q_avg")

config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                "2": {
                    "analog_outputs": {
                        "8": {
                            "full_scale_power_dbm": -11,
                            "upconverters": {
                                "1": {
                                    "frequency": 3916921000.0,
                                },
                            },
                            "band": 1,
                            "delay": 20,
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
                        "2": {
                            "full_scale_power_dbm": 16,
                            "upconverters": {
                                "1": {
                                    "frequency": 6763200000.0,
                                },
                            },
                            "band": 2,
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
                        "7": {
                            "full_scale_power_dbm": 7,
                            "upconverters": {
                                "1": {
                                    "frequency": 6335800000.0,
                                },
                            },
                            "band": 2,
                        },
                    },
                    "analog_inputs": {
                        "2": {
                            "gain_db": 0,
                            "downconverter_frequency": 3916921000.0,
                            "band": 1,
                        },
                        "1": {
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
        "rr_MR": {
            "MWInput": {
                "port": ['con1', 2, 8],
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ['con1'] + [2] * 2,
            },
            "intermediate_frequency": -50000000,
            "time_of_flight": 300,
            "smearing": 0,
            "operations": {
                "readout_pulse": "rr_MR.rr_MR_readout_pulse",
            },
        },
    },
    "pulses": {
        "rr_MR.rr_MR_readout_pulse": {
            "operation": "measurement",
            "length": 1600,
            "waveforms": {
                "I": "rr_MR.rr_MR_readout_pulse.waveform.I",
                "Q": "rr_MR.rr_MR_readout_pulse.waveform.Q",
            },
            "digital_marker": "rr_MR.rr_MR_readout_pulse.ADC_ON",
            "integration_weights": {
                "cos": "rr_MR.rr_MR_readout_pulse.cos",
                "sin": "rr_MR.rr_MR_readout_pulse.sin",
                "minus_sin": "rr_MR.rr_MR_readout_pulse.minus_sin",
            },
        },
    },
    "waveforms": {
        "rr_MR.rr_MR_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.04000000000000001] * 1000 + [0.0] * 600,
        },
        "rr_MR.rr_MR_readout_pulse.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
    },
    "digital_waveforms": {
        "rr_MR.rr_MR_readout_pulse.ADC_ON": {
            "samples": [[1, 0]],
        },
    },
    "integration_weights": {
        "rr_MR.rr_MR_readout_pulse.cos": {
            "cosine": [[1.0, 1600]],
            "sine": [[0.0, 1600]],
        },
        "rr_MR.rr_MR_readout_pulse.sin": {
            "cosine": [[0.0, 1600]],
            "sine": [[1.0, 1600]],
        },
        "rr_MR.rr_MR_readout_pulse.minus_sin": {
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
                        "8": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -11,
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 3916921000.0,
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
                    },
                    "analog_inputs": {
                        "2": {
                            "band": 1,
                            "shareable": False,
                            "gain_db": 0,
                            "sampling_rate": 1000000000.0,
                            "downconverter_frequency": 3916921000.0,
                        },
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
        "rr_MR": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "readout_pulse": "rr_MR.rr_MR_readout_pulse",
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
                "port": ('con1', 2, 8),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 2, 2),
            },
            "smearing": 0,
            "time_of_flight": 300,
            "intermediate_frequency": -50000000.0,
        },
    },
    "pulses": {
        "rr_MR.rr_MR_readout_pulse": {
            "length": 1600,
            "waveforms": {
                "I": "rr_MR.rr_MR_readout_pulse.waveform.I",
                "Q": "rr_MR.rr_MR_readout_pulse.waveform.Q",
            },
            "integration_weights": {
                "cos": "rr_MR.rr_MR_readout_pulse.cos",
                "sin": "rr_MR.rr_MR_readout_pulse.sin",
                "minus_sin": "rr_MR.rr_MR_readout_pulse.minus_sin",
            },
            "operation": "measurement",
            "digital_marker": "rr_MR.rr_MR_readout_pulse.ADC_ON",
        },
    },
    "waveforms": {
        "rr_MR.rr_MR_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.04000000000000001] * 1000 + [0.0] * 600,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "rr_MR.rr_MR_readout_pulse.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
    },
    "digital_waveforms": {
        "rr_MR.rr_MR_readout_pulse.ADC_ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "rr_MR.rr_MR_readout_pulse.cos": {
            "cosine": [(1.0, 1600)],
            "sine": [(0.0, 1600)],
        },
        "rr_MR.rr_MR_readout_pulse.sin": {
            "cosine": [(0.0, 1600)],
            "sine": [(1.0, 1600)],
        },
        "rr_MR.rr_MR_readout_pulse.minus_sin": {
            "cosine": [(0.0, 1600)],
            "sine": [(-1.0, 1600)],
        },
    },
    "mixers": {},
}

