
# Single QUA script generated at 2026-04-03 15:16:37.799352
# QUA library version: 1.2.6


from qm import CompilerOptionArguments
from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(int, )
    v3 = declare(fixed, )
    v4 = declare(fixed, )
    with for_(v1,1,(v1<10001),(v1+1)):
        r1 = declare_stream()
        save(v1, r1)
        with for_(v2,-200000000,(v2<201000000),(v2+2000000)):
            r2 = declare_stream()
            save(v2, r2)
            update_frequency("cavity", v2, "Hz", False)
            play("cavity_pulse"*amp(1), "cavity")
            align("cavity", "qubit")
            play("qubit_pulse"*amp(1.0), "qubit")
            align("qubit", "rr")
            align()
            measure("readout_pulse"*amp(1), "rr", dual_demod.full("cos", "sin", v3), dual_demod.full("minus_sin", "cos", v4))
            wait(200000, "rr")
            r3 = declare_stream()
            save(v3, r3)
            r4 = declare_stream()
            save(v4, r4)
    with stream_processing():
        r2.buffer(201).save("cavity_frequency")
        r3.buffer(201).save_all("I")
        r3.buffer(201).average().save("I_avg")
        r4.buffer(201).save_all("Q")
        r4.buffer(201).average().save("Q_avg")

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
                            "full_scale_power_dbm": 16,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 6300000000.0,
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
                                    "frequency": 7665170000.0,
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
                            "downconverter_frequency": 7665170000.0,
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
            "intermediate_frequency": 115000000.0,
        },
        "cavity": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cavity_pulse": "cavity.cav_constant_10000",
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
            "intermediate_frequency": -108000000.0,
        },
    },
    "pulses": {
        "rr.rr_readout_pulse": {
            "length": 832,
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
        "qubit.qubit_constant_pi_400": {
            "length": 400,
            "waveforms": {
                "I": "qubit.qubit_constant_pi_400.waveform.I",
                "Q": "qubit.qubit_constant_pi_400.waveform.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cavity.cav_constant_10000": {
            "length": 100000,
            "waveforms": {
                "I": "cavity.cav_constant_10000.waveform.I",
                "Q": "cavity.cav_constant_10000.waveform.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "cavity.cav_constant_10000.waveform.I": {
            "type": "constant",
            "sample": 0.39,
        },
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.003] * 640 + [0.0] * 192,
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "qubit.qubit_constant_pi_400.waveform.I": {
            "type": "constant",
            "sample": 0.009200650234988778,
        },
        "cavity.cav_constant_10000.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "rr.rr_readout_pulse.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
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
            "cosine": [(-0.014190673828125, 64), (-0.41510009765625, 64), (-0.6307373046875, 64), (-0.788238525390625, 64), (-0.84185791015625, 64), (-0.890289306640625, 64), (-0.88525390625, 64), (-0.87408447265625, 64), (-0.695404052734375, 64), (-0.691162109375, 64)],
            "sine": [(-0.004150390625, 64), (0.22967529296875, 64), (-0.462188720703125, 64), (-0.33447265625, 64), (-0.365966796875, 64), (-0.374420166015625, 64), (-0.43670654296875, 64), (-0.48577880859375, 64), (-0.41729736328125, 64), (-0.3333740234375, 64)],
        },
        "rr.rr_readout_pulse.cos": {
            "cosine": [(-0.004150390625, 64), (0.22967529296875, 64), (-0.462188720703125, 64), (-0.33447265625, 64), (-0.365966796875, 64), (-0.374420166015625, 64), (-0.43670654296875, 64), (-0.48577880859375, 64), (-0.41729736328125, 64), (-0.3333740234375, 64)],
            "sine": [(0.014190673828125, 64), (0.41510009765625, 64), (0.6307373046875, 64), (0.788238525390625, 64), (0.84185791015625, 64), (0.890289306640625, 64), (0.88525390625, 64), (0.87408447265625, 64), (0.695404052734375, 64), (0.691162109375, 64)],
        },
        "rr.rr_readout_pulse.minus_sin": {
            "cosine": [(0.014190673828125, 64), (0.41510009765625, 64), (0.6307373046875, 64), (0.788238525390625, 64), (0.84185791015625, 64), (0.890289306640625, 64), (0.88525390625, 64), (0.87408447265625, 64), (0.695404052734375, 64), (0.691162109375, 64)],
            "sine": [(0.004150390625, 64), (-0.22967529296875, 64), (0.462188720703125, 64), (0.33447265625, 64), (0.365966796875, 64), (0.374420166015625, 64), (0.43670654296875, 64), (0.48577880859375, 64), (0.41729736328125, 64), (0.3333740234375, 64)],
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
                            "full_scale_power_dbm": 16,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 6300000000.0,
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
                                    "frequency": 7665170000.0,
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
                            "downconverter_frequency": 7665170000.0,
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
            "intermediate_frequency": 115000000.0,
        },
        "cavity": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cavity_pulse": "cavity.cav_constant_10000",
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
            "intermediate_frequency": -108000000.0,
        },
    },
    "pulses": {
        "rr.rr_readout_pulse": {
            "length": 832,
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
        "qubit.qubit_constant_pi_400": {
            "length": 400,
            "waveforms": {
                "I": "qubit.qubit_constant_pi_400.waveform.I",
                "Q": "qubit.qubit_constant_pi_400.waveform.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cavity.cav_constant_10000": {
            "length": 100000,
            "waveforms": {
                "I": "cavity.cav_constant_10000.waveform.I",
                "Q": "cavity.cav_constant_10000.waveform.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "cavity.cav_constant_10000.waveform.I": {
            "type": "constant",
            "sample": 0.39,
        },
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.003] * 640 + [0.0] * 192,
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "qubit.qubit_constant_pi_400.waveform.I": {
            "type": "constant",
            "sample": 0.009200650234988778,
        },
        "cavity.cav_constant_10000.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "rr.rr_readout_pulse.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
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
            "cosine": [(-0.014190673828125, 64), (-0.41510009765625, 64), (-0.6307373046875, 64), (-0.788238525390625, 64), (-0.84185791015625, 64), (-0.890289306640625, 64), (-0.88525390625, 64), (-0.87408447265625, 64), (-0.695404052734375, 64), (-0.691162109375, 64)],
            "sine": [(-0.004150390625, 64), (0.22967529296875, 64), (-0.462188720703125, 64), (-0.33447265625, 64), (-0.365966796875, 64), (-0.374420166015625, 64), (-0.43670654296875, 64), (-0.48577880859375, 64), (-0.41729736328125, 64), (-0.3333740234375, 64)],
        },
        "rr.rr_readout_pulse.cos": {
            "cosine": [(-0.004150390625, 64), (0.22967529296875, 64), (-0.462188720703125, 64), (-0.33447265625, 64), (-0.365966796875, 64), (-0.374420166015625, 64), (-0.43670654296875, 64), (-0.48577880859375, 64), (-0.41729736328125, 64), (-0.3333740234375, 64)],
            "sine": [(0.014190673828125, 64), (0.41510009765625, 64), (0.6307373046875, 64), (0.788238525390625, 64), (0.84185791015625, 64), (0.890289306640625, 64), (0.88525390625, 64), (0.87408447265625, 64), (0.695404052734375, 64), (0.691162109375, 64)],
        },
        "rr.rr_readout_pulse.minus_sin": {
            "cosine": [(0.014190673828125, 64), (0.41510009765625, 64), (0.6307373046875, 64), (0.788238525390625, 64), (0.84185791015625, 64), (0.890289306640625, 64), (0.88525390625, 64), (0.87408447265625, 64), (0.695404052734375, 64), (0.691162109375, 64)],
            "sine": [(0.004150390625, 64), (-0.22967529296875, 64), (0.462188720703125, 64), (0.33447265625, 64), (0.365966796875, 64), (0.374420166015625, 64), (0.43670654296875, 64), (0.48577880859375, 64), (0.41729736328125, 64), (0.3333740234375, 64)],
        },
    },
    "mixers": {},
}

