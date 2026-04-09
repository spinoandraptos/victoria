
# Single QUA script generated at 2026-04-08 18:06:40.626302
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
        with for_(v2,10,(v2<6025),(v2+50)):
            r2 = declare_stream()
            save(v2, r2)
            play("cavity_drive"*amp(1.0), "cavity")
            wait(Cast.to_int((v2/4)), "cavity")
            align()
            play("qubit_pulse"*amp(1.0), "qubit")
            align("qubit", "rr")
            measure("readout_pulse"*amp(1), "rr", dual_demod.full("cos", "sin", v3), dual_demod.full("minus_sin", "cos", v4))
            wait(250000, "rr")
            r3 = declare_stream()
            save(v3, r3)
            r4 = declare_stream()
            save(v4, r4)
    with stream_processing():
        r2.buffer(121).save("time_delay")
        r3.buffer(121).save_all("I")
        r3.buffer(121).average().save("I_avg")
        r4.buffer(121).save_all("Q")
        r4.buffer(121).average().save("Q_avg")

config = {
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                "8": {
                    "type": "MW",
                    "analog_outputs": {
                        "2": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 7250220000.0,
                                },
                            },
                        },
                        "4": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 16,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 5500000000.0,
                                },
                            },
                        },
                        "1": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 16,
                            "band": 3,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 7660010000.0,
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
                                    "frequency": 5661800000.0,
                                },
                            },
                        },
                    },
                    "analog_inputs": {
                        "2": {
                            "band": 3,
                            "shareable": False,
                            "gain_db": 0,
                            "sampling_rate": 1000000000.0,
                            "downconverter_frequency": 7660010000.0,
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
                "port": ('con1', 8, 2),
            },
            "smearing": 0,
            "time_of_flight": 400,
            "intermediate_frequency": -50400000.0,
        },
        "qubit": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "qubit_pulse": "qubit.qubit_constant_pi_400",
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
                "port": ('con1', 8, 4),
                "upconverter": 1,
            },
            "intermediate_frequency": 98900000.0,
        },
        "cavity": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cavity_drive": "cavity.cav_constant_400",
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
                "port": ('con1', 8, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": 74200000.0,
        },
    },
    "pulses": {
        "rr.rr_readout_pulse": {
            "length": 704,
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
        "cavity.cav_constant_400": {
            "length": 400,
            "waveforms": {
                "I": "cavity.cav_constant_400.waveform.I",
                "Q": "cavity.cav_constant_400.waveform.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "qubit.qubit_constant_pi_400": {
            "length": 400,
            "waveforms": {
                "I": "qubit.qubit_constant_pi_400.waveform.I",
                "Q": "qubit.qubit_constant_pi_400.waveform.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.004] * 320 + [0.0] * 384,
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "cavity.cav_constant_400.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit.qubit_constant_pi_400.waveform.I": {
            "type": "constant",
            "sample": 0.00531952488,
        },
        "rr.rr_readout_pulse.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cavity.cav_constant_400.waveform.I": {
            "type": "constant",
            "sample": 0.39,
        },
        "qubit.qubit_constant_pi_400.waveform.Q": {
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
            "cosine": [(-0.015411376953125, 64), (-0.096527099609375, 64), (-0.252197265625, 64), (-0.45587158203125, 64), (-0.680328369140625, 64), (-0.873199462890625, 64), (-0.97064208984375, 64), (-0.934112548828125, 64), (-0.751922607421875, 64), (-0.518157958984375, 64), (-0.268035888671875, 64)],
            "sine": [(0.0299072265625, 64), (0.0845947265625, 64), (0.22271728515625, 64), (0.308380126953125, 64), (0.3824462890625, 64), (0.3592529296875, 64), (0.240478515625, 64), (0.13848876953125, 64), (0.041107177734375, 64), (-0.01141357421875, 64), (0.054412841796875, 64)],
        },
        "rr.rr_readout_pulse.cos": {
            "cosine": [(0.0299072265625, 64), (0.0845947265625, 64), (0.22271728515625, 64), (0.308380126953125, 64), (0.3824462890625, 64), (0.3592529296875, 64), (0.240478515625, 64), (0.13848876953125, 64), (0.041107177734375, 64), (-0.01141357421875, 64), (0.054412841796875, 64)],
            "sine": [(0.015411376953125, 64), (0.096527099609375, 64), (0.252197265625, 64), (0.45587158203125, 64), (0.680328369140625, 64), (0.873199462890625, 64), (0.97064208984375, 64), (0.934112548828125, 64), (0.751922607421875, 64), (0.518157958984375, 64), (0.268035888671875, 64)],
        },
        "rr.rr_readout_pulse.minus_sin": {
            "cosine": [(0.015411376953125, 64), (0.096527099609375, 64), (0.252197265625, 64), (0.45587158203125, 64), (0.680328369140625, 64), (0.873199462890625, 64), (0.97064208984375, 64), (0.934112548828125, 64), (0.751922607421875, 64), (0.518157958984375, 64), (0.268035888671875, 64)],
            "sine": [(-0.0299072265625, 64), (-0.0845947265625, 64), (-0.22271728515625, 64), (-0.308380126953125, 64), (-0.3824462890625, 64), (-0.3592529296875, 64), (-0.240478515625, 64), (-0.13848876953125, 64), (-0.041107177734375, 64), (0.01141357421875, 64), (-0.054412841796875, 64)],
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
                        "2": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 7250220000.0,
                                },
                            },
                        },
                        "4": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 16,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 5500000000.0,
                                },
                            },
                        },
                        "1": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 16,
                            "band": 3,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 7660010000.0,
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
                                    "frequency": 5661800000.0,
                                },
                            },
                        },
                    },
                    "analog_inputs": {
                        "2": {
                            "band": 3,
                            "shareable": False,
                            "gain_db": 0,
                            "sampling_rate": 1000000000.0,
                            "downconverter_frequency": 7660010000.0,
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
                "port": ('con1', 8, 2),
            },
            "smearing": 0,
            "time_of_flight": 400,
            "intermediate_frequency": -50400000.0,
        },
        "qubit": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "qubit_pulse": "qubit.qubit_constant_pi_400",
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
                "port": ('con1', 8, 4),
                "upconverter": 1,
            },
            "intermediate_frequency": 98900000.0,
        },
        "cavity": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cavity_drive": "cavity.cav_constant_400",
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
                "port": ('con1', 8, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": 74200000.0,
        },
    },
    "pulses": {
        "rr.rr_readout_pulse": {
            "length": 704,
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
        "cavity.cav_constant_400": {
            "length": 400,
            "waveforms": {
                "I": "cavity.cav_constant_400.waveform.I",
                "Q": "cavity.cav_constant_400.waveform.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "qubit.qubit_constant_pi_400": {
            "length": 400,
            "waveforms": {
                "I": "qubit.qubit_constant_pi_400.waveform.I",
                "Q": "qubit.qubit_constant_pi_400.waveform.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.004] * 320 + [0.0] * 384,
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "cavity.cav_constant_400.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit.qubit_constant_pi_400.waveform.I": {
            "type": "constant",
            "sample": 0.00531952488,
        },
        "rr.rr_readout_pulse.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cavity.cav_constant_400.waveform.I": {
            "type": "constant",
            "sample": 0.39,
        },
        "qubit.qubit_constant_pi_400.waveform.Q": {
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
            "cosine": [(-0.015411376953125, 64), (-0.096527099609375, 64), (-0.252197265625, 64), (-0.45587158203125, 64), (-0.680328369140625, 64), (-0.873199462890625, 64), (-0.97064208984375, 64), (-0.934112548828125, 64), (-0.751922607421875, 64), (-0.518157958984375, 64), (-0.268035888671875, 64)],
            "sine": [(0.0299072265625, 64), (0.0845947265625, 64), (0.22271728515625, 64), (0.308380126953125, 64), (0.3824462890625, 64), (0.3592529296875, 64), (0.240478515625, 64), (0.13848876953125, 64), (0.041107177734375, 64), (-0.01141357421875, 64), (0.054412841796875, 64)],
        },
        "rr.rr_readout_pulse.cos": {
            "cosine": [(0.0299072265625, 64), (0.0845947265625, 64), (0.22271728515625, 64), (0.308380126953125, 64), (0.3824462890625, 64), (0.3592529296875, 64), (0.240478515625, 64), (0.13848876953125, 64), (0.041107177734375, 64), (-0.01141357421875, 64), (0.054412841796875, 64)],
            "sine": [(0.015411376953125, 64), (0.096527099609375, 64), (0.252197265625, 64), (0.45587158203125, 64), (0.680328369140625, 64), (0.873199462890625, 64), (0.97064208984375, 64), (0.934112548828125, 64), (0.751922607421875, 64), (0.518157958984375, 64), (0.268035888671875, 64)],
        },
        "rr.rr_readout_pulse.minus_sin": {
            "cosine": [(0.015411376953125, 64), (0.096527099609375, 64), (0.252197265625, 64), (0.45587158203125, 64), (0.680328369140625, 64), (0.873199462890625, 64), (0.97064208984375, 64), (0.934112548828125, 64), (0.751922607421875, 64), (0.518157958984375, 64), (0.268035888671875, 64)],
            "sine": [(-0.0299072265625, 64), (-0.0845947265625, 64), (-0.22271728515625, 64), (-0.308380126953125, 64), (-0.3824462890625, 64), (-0.3592529296875, 64), (-0.240478515625, 64), (-0.13848876953125, 64), (-0.041107177734375, 64), (0.01141357421875, 64), (-0.054412841796875, 64)],
        },
    },
    "mixers": {},
}

