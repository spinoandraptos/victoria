
# Single QUA script generated at 2026-04-02 18:16:46.309000
# QUA library version: 1.2.6


from qm import CompilerOptionArguments
from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(int, )
    v4 = declare(fixed, )
    v5 = declare(fixed, )
    a1 = declare(fixed, value=[0.0, 1.0, 1.5])
    with for_(v1,1,(v1<500001),(v1+1)):
        r1 = declare_stream()
        save(v1, r1)
        with for_each_((v2),(a1)):
            r2 = declare_stream()
            save(v2, r2)
            with for_(v3,105000000,(v3<130062500),(v3+125000)):
                r3 = declare_stream()
                save(v3, r3)
                play("cavity_pulse"*amp(v2), "cavity")
                align()
                update_frequency("qubit", v3, "Hz", False)
                play("qubit_pulse"*amp(1.0), "qubit")
                align("qubit", "qubit_EF")
                play("qubit_ef_drive"*amp(1.0), "qubit_EF")
                align("qubit_EF", "rr")
                measure("readout_pulse"*amp(1), "rr", dual_demod.full("cos", "sin", v4), dual_demod.full("minus_sin", "cos", v5))
                wait(250000, "rr")
                r4 = declare_stream()
                save(v4, r4)
                r5 = declare_stream()
                save(v5, r5)
    with stream_processing():
        r2.buffer(3).save("cavity_drive_ampx")
        r3.buffer(201).save("qubit_frequency")
        r4.buffer(3, 201).save_all("I")
        r4.buffer(3, 201).average().save("I_avg")
        r5.buffer(3, 201).save_all("Q")
        r5.buffer(3, 201).average().save("Q_avg")

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
                            "band": 3,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 6768400000.0,
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
                                    "frequency": 6135000000.0,
                                },
                            },
                        },
                        "1": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 16,
                            "band": 3,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 7930670000.0,
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
                            "downconverter_frequency": 7930670000.0,
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
            "time_of_flight": 300,
            "intermediate_frequency": -50000000.0,
        },
        "qubit_EF": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "qubit_ef_drive": "qubit_EF.qubitEF_gaussian_pi_16",
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
            "intermediate_frequency": -118000000.0,
        },
        "qubit": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "qubit_pulse": "qubit.qubit_constant_pi_1000",
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
            "intermediate_frequency": 122000000.0,
        },
        "cavity": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cavity_pulse": "cavity.cav_constant_40",
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
        "cavity.cav_constant_40": {
            "length": 40,
            "waveforms": {
                "I": "cavity.cav_constant_40.waveform.I",
                "Q": "cavity.cav_constant_40.waveform.Q",
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
        "qubit.qubit_constant_pi_1000": {
            "length": 1000,
            "waveforms": {
                "I": "qubit.qubit_constant_pi_1000.waveform.I",
                "Q": "qubit.qubit_constant_pi_1000.waveform.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "qubit.qubit_constant_pi_1000.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.006] * 576 + [0.0] * 64,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "qubit_EF.qubitEF_gaussian_pi_16.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cavity.cav_constant_40.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit.qubit_constant_pi_1000.waveform.I": {
            "type": "constant",
            "sample": 0.0038510909442176877,
        },
        "rr.rr_readout_pulse.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit_EF.qubitEF_gaussian_pi_16.waveform.I": {
            "type": "arbitrary",
            "samples": [0.03677589218386215, 0.06049860485839427, 0.09269244513494347, 0.13226963477173145, 0.17578944985444359, 0.2175916855752196, 0.25084683325723806] + [0.26933437513268615] * 2 + [0.25084683325723806, 0.21759168557521966, 0.1757894498544436, 0.13226963477173143, 0.09269244513494347, 0.06049860485839427, 0.03677589218386215],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cavity.cav_constant_40.waveform.I": {
            "type": "constant",
            "sample": 0.030000000000000006,
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
                            "band": 3,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 6768400000.0,
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
                                    "frequency": 6135000000.0,
                                },
                            },
                        },
                        "1": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 16,
                            "band": 3,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 7930670000.0,
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
                            "downconverter_frequency": 7930670000.0,
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
            "time_of_flight": 300,
            "intermediate_frequency": -50000000.0,
        },
        "qubit_EF": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "qubit_ef_drive": "qubit_EF.qubitEF_gaussian_pi_16",
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
            "intermediate_frequency": -118000000.0,
        },
        "qubit": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "qubit_pulse": "qubit.qubit_constant_pi_1000",
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
            "intermediate_frequency": 122000000.0,
        },
        "cavity": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cavity_pulse": "cavity.cav_constant_40",
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
        "cavity.cav_constant_40": {
            "length": 40,
            "waveforms": {
                "I": "cavity.cav_constant_40.waveform.I",
                "Q": "cavity.cav_constant_40.waveform.Q",
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
        "qubit.qubit_constant_pi_1000": {
            "length": 1000,
            "waveforms": {
                "I": "qubit.qubit_constant_pi_1000.waveform.I",
                "Q": "qubit.qubit_constant_pi_1000.waveform.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "qubit.qubit_constant_pi_1000.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.006] * 576 + [0.0] * 64,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "qubit_EF.qubitEF_gaussian_pi_16.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cavity.cav_constant_40.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit.qubit_constant_pi_1000.waveform.I": {
            "type": "constant",
            "sample": 0.0038510909442176877,
        },
        "rr.rr_readout_pulse.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit_EF.qubitEF_gaussian_pi_16.waveform.I": {
            "type": "arbitrary",
            "samples": [0.03677589218386215, 0.06049860485839427, 0.09269244513494347, 0.13226963477173145, 0.17578944985444359, 0.2175916855752196, 0.25084683325723806] + [0.26933437513268615] * 2 + [0.25084683325723806, 0.21759168557521966, 0.1757894498544436, 0.13226963477173143, 0.09269244513494347, 0.06049860485839427, 0.03677589218386215],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cavity.cav_constant_40.waveform.I": {
            "type": "constant",
            "sample": 0.030000000000000006,
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

