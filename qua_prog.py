
# Single QUA script generated at 2026-04-22 11:13:41.169632
# QUA library version: 1.2.6


from qm import CompilerOptionArguments
from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    v4 = declare(fixed, )
    v5 = declare(fixed, )
    a1 = declare(fixed, value=[0.0, 1.0])
    with for_(v1,1,(v1<500001),(v1+1)):
        r1 = declare_stream()
        save(v1, r1)
        with for_each_((v2),(a1)):
            r2 = declare_stream()
            save(v2, r2)
            with for_(v3,-1.4,(v3<1.428),(v3+0.05600000000000005)):
                r3 = declare_stream()
                save(v3, r3)
                play("qubit_pi_pulse"*amp(v2), "qubit")
                align("qubit", "qubit_EF")
                play("qubitEF_pi_pulse"*amp(v3), "qubit_EF")
                align("qubit_EF", "qubit")
                play("qubit_pi_pulse"*amp(1.0), "qubit")
                align("qubit", "rr")
                measure("readout_pulse"*amp(1), "rr", dual_demod.full("cos", "sin", v4), dual_demod.full("minus_sin", "cos", v5))
                wait(25000, "rr")
                r4 = declare_stream()
                save(v4, r4)
                r5 = declare_stream()
                save(v5, r5)
    with stream_processing():
        r2.buffer(2).save("qubitGE_pulse_amplitude")
        r3.buffer(51).save("qubitEF_pulse_amplitude")
        r4.buffer(2, 51).save_all("I")
        r4.buffer(2, 51).average().save("I_avg")
        r5.buffer(2, 51).save_all("Q")
        r5.buffer(2, 51).average().save("Q_avg")

config = {
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                "8": {
                    "type": "MW",
                    "analog_outputs": {
                        "4": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 6116580000.0,
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
                                    "frequency": 7922670000.0,
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
                        "2": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 6709000000.0,
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
                            "downconverter_frequency": 7922670000.0,
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
            "intermediate_frequency": -50000000.0,
        },
        "qubit_EF": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "qubitEF_pi_pulse": "qubit_EF.qubitEF_gaussian_pi_16",
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
            "intermediate_frequency": -90000000.0,
        },
        "qubit": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "qubit_pi_pulse": "qubit.qubit_gaussian_pi_16",
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
            "intermediate_frequency": 153000000.0,
        },
    },
    "pulses": {
        "rr.rr_readout_pulse": {
            "length": 640,
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
        "qubit.qubit_gaussian_pi_16": {
            "length": 16,
            "waveforms": {
                "I": "qubit.qubit_gaussian_pi_16.waveform.I",
                "Q": "qubit.qubit_gaussian_pi_16.waveform.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "qubit_EF.qubitEF_gaussian_pi_16": {
            "length": 16,
            "waveforms": {
                "I": "qubit_EF.qubitEF_gaussian_pi_16.waveform.I",
                "Q": "qubit_EF.qubitEF_gaussian_pi_16.waveform.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.006] * 320 + [0.0] * 320,
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "qubit_EF.qubitEF_gaussian_pi_16.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit.qubit_gaussian_pi_16.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "rr.rr_readout_pulse.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit_EF.qubitEF_gaussian_pi_16.waveform.I": {
            "type": "arbitrary",
            "samples": [0.0193853060403857, 0.03189002089556305, 0.04886003601459968, 0.06972196179716936, 0.09266212406383961, 0.11469691600221657, 0.13222636741596197] + [0.14197151935947547] * 2 + [0.13222636741596197, 0.11469691600221658, 0.09266212406383963, 0.06972196179716933, 0.04886003601459968, 0.03189002089556305, 0.0193853060403857],
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "qubit.qubit_gaussian_pi_16.waveform.I": {
            "type": "arbitrary",
            "samples": [0.02584707472051427, 0.04252002786075075, 0.06514671468613292, 0.09296261572955915, 0.12354949875178617, 0.1529292213362888, 0.17630182322128266] + [0.18929535914596735] * 2 + [0.17630182322128266, 0.1529292213362888, 0.1235494987517862, 0.09296261572955913, 0.06514671468613292, 0.04252002786075075, 0.02584707472051427],
            "is_overridable": False,
            "max_allowed_error": 1.0,
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
                        "4": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 6116580000.0,
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
                                    "frequency": 7922670000.0,
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
                        "2": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 6709000000.0,
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
                            "downconverter_frequency": 7922670000.0,
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
            "intermediate_frequency": -50000000.0,
        },
        "qubit_EF": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "qubitEF_pi_pulse": "qubit_EF.qubitEF_gaussian_pi_16",
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
            "intermediate_frequency": -90000000.0,
        },
        "qubit": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "qubit_pi_pulse": "qubit.qubit_gaussian_pi_16",
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
            "intermediate_frequency": 153000000.0,
        },
    },
    "pulses": {
        "rr.rr_readout_pulse": {
            "length": 640,
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
        "qubit.qubit_gaussian_pi_16": {
            "length": 16,
            "waveforms": {
                "I": "qubit.qubit_gaussian_pi_16.waveform.I",
                "Q": "qubit.qubit_gaussian_pi_16.waveform.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "qubit_EF.qubitEF_gaussian_pi_16": {
            "length": 16,
            "waveforms": {
                "I": "qubit_EF.qubitEF_gaussian_pi_16.waveform.I",
                "Q": "qubit_EF.qubitEF_gaussian_pi_16.waveform.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.006] * 320 + [0.0] * 320,
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "qubit_EF.qubitEF_gaussian_pi_16.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit.qubit_gaussian_pi_16.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "rr.rr_readout_pulse.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit_EF.qubitEF_gaussian_pi_16.waveform.I": {
            "type": "arbitrary",
            "samples": [0.0193853060403857, 0.03189002089556305, 0.04886003601459968, 0.06972196179716936, 0.09266212406383961, 0.11469691600221657, 0.13222636741596197] + [0.14197151935947547] * 2 + [0.13222636741596197, 0.11469691600221658, 0.09266212406383963, 0.06972196179716933, 0.04886003601459968, 0.03189002089556305, 0.0193853060403857],
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "qubit.qubit_gaussian_pi_16.waveform.I": {
            "type": "arbitrary",
            "samples": [0.02584707472051427, 0.04252002786075075, 0.06514671468613292, 0.09296261572955915, 0.12354949875178617, 0.1529292213362888, 0.17630182322128266] + [0.18929535914596735] * 2 + [0.17630182322128266, 0.1529292213362888, 0.1235494987517862, 0.09296261572955913, 0.06514671468613292, 0.04252002786075075, 0.02584707472051427],
            "is_overridable": False,
            "max_allowed_error": 1.0,
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

