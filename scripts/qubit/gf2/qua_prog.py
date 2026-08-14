# Auto-generated standalone QUA execution script
import time
import numpy as np
import matplotlib.pyplot as plt
from qm import QuantumMachinesManager
from qm.qua import *


# Single QUA script generated at 2026-08-14 17:44:47.446470
# QUA library version: 1.3.1


from qm import CompilerOptionArguments
from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    v4 = declare(fixed, )
    with for_(v1,1,(v1<100001),(v1+1)):
        r1 = declare_output_stream()
        save(v1, r1)
        with for_(v2,-1.4,(v2<1.4233333333333333),(v2+0.046666666666666634)):
            r2 = declare_output_stream()
            save(v2, r2)
            play('qubit_gf2_drive'*amp(v2), 'qubit_GF2')
            align('qubit_GF2', 'rr')
            measure('readout_pulse'*amp(1), 'rr', dual_demod.full("cos", "sin", v3), dual_demod.full("minus_sin", "cos", v4))
            wait(37500, 'rr')
            r3 = declare_output_stream()
            save(v3, r3)
            r4 = declare_output_stream()
            save(v4, r4)
    with stream_processing():
        r2.buffer(61).save("qubit_pulse_amplitude")
        r3.buffer(61).save_all("I")
        r3.buffer(61).average().save("I_avg")
        r4.buffer(61).save_all("Q")
        r4.buffer(61).average().save("Q_avg")

config = {
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                "8": {
                    "type": "MW",
                },
                "1": {
                    "type": "MW",
                    "analog_outputs": {
                        "2": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 4361000000.0,
                                },
                            },
                        },
                        "3": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 3,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 7679500000.0,
                                },
                            },
                        },
                        "4": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 6660000000.0,
                                },
                            },
                        },
                        "6": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 8,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 5698000000.0,
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
                            "downconverter_frequency": 7679500000.0,
                        },
                    },
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
        "qubit_GF2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {'qubit_gf2_drive': 'qubit_GF2.qubitGF2_gaussian_pi_48'},
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 6),
                "upconverter": 1,
            },
            "intermediate_frequency": -49000000.0,
        },
        "rr": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {'readout_pulse': 'rr.rr_readout_pulse'},
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 3),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 1, 1),
            },
            "smearing": 0,
            "time_of_flight": 408,
            "intermediate_frequency": -40600000.0,
        },
    },
    "pulses": {
        "rr.rr_readout_pulse": {
            "length": 768,
            "waveforms": {'Q': 'rr.rr_readout_pulse.waveform.Q', 'I': 'rr.rr_readout_pulse.waveform.I'},
            "integration_weights": {'minus_sin': 'rr.rr_readout_pulse.minus_sin', 'sin': 'rr.rr_readout_pulse.sin', 'cos': 'rr.rr_readout_pulse.cos'},
            "operation": "measurement",
        },
        "qubit_GF2.qubitGF2_gaussian_pi_48": {
            "length": 48,
            "waveforms": {'Q': 'qubit_GF2.qubitGF2_gaussian_pi_48.waveform.Q', 'I': 'qubit_GF2.qubitGF2_gaussian_pi_48.waveform.I'},
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "qubit_GF2.qubitGF2_gaussian_pi_48.waveform.I": {
            "type": "arbitrary",
            "samples": [0.040600584970983816, 0.04796030513411972, 0.056245262410470794, 0.06548537521967554, 0.07569323322607498, 0.08686086617573445, 0.09895679440992976, 0.1119235416099775, 0.1256757926571024, 0.140099370920127, 0.15505118885014657, 0.17036029327464733, 0.1858300829456258, 0.2012417223552192, 0.21635871515699936, 0.23093253609953396, 0.24470915618226402, 0.2574362361159598, 0.2688707124618901, 0.27878646304957755, 0.2869817167598583, 0.2932858698352459, 0.29756538762739637] + [0.2997285068058678] * 2 + [0.29756538762739637, 0.2932858698352459, 0.28698171675985834, 0.27878646304957755, 0.26887071246189015, 0.25743623611595984, 0.24470915618226405, 0.23093253609953399, 0.2163587151569994, 0.20124172235521925, 0.1858300829456259, 0.17036029327464738, 0.15505118885014663, 0.14009937092012706, 0.1256757926571025, 0.11192354160997761, 0.09895679440992981, 0.08686086617573453, 0.07569323322607505, 0.06548537521967561, 0.05624526241047086, 0.047960305134119766, 0.040600584970983816],
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.020000000000000004] * 512 + [0.0] * 256,
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "rr.rr_readout_pulse.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit_GF2.qubitGF2_gaussian_pi_48.waveform.Q": {
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
            "cosine": [(0.059326171875, 64), (0.159423828125, 64), (0.225738525390625, 64), (0.052581787109375, 64), (-0.303924560546875, 64), (-0.731048583984375, 64), (-0.930633544921875, 64), (-0.829742431640625, 64), (-0.555450439453125, 64), (-0.354766845703125, 64), (-0.150543212890625, 64), (0.089263916015625, 64)],
            "sine": [(0.032196044921875, 64), (0.220123291015625, 64), (0.477630615234375, 64), (0.690277099609375, 64), (0.854461669921875, 64), (0.682342529296875, 64), (0.196197509765625, 64), (-0.213714599609375, 64), (-0.43701171875, 64), (-0.58258056640625, 64), (-0.737762451171875, 64), (-0.788360595703125, 64)],
        },
        "rr.rr_readout_pulse.sin": {
            "cosine": [(-0.032196044921875, 64), (-0.220123291015625, 64), (-0.477630615234375, 64), (-0.690277099609375, 64), (-0.854461669921875, 64), (-0.682342529296875, 64), (-0.196197509765625, 64), (0.213714599609375, 64), (0.43701171875, 64), (0.58258056640625, 64), (0.737762451171875, 64), (0.788360595703125, 64)],
            "sine": [(0.059326171875, 64), (0.159423828125, 64), (0.225738525390625, 64), (0.052581787109375, 64), (-0.303924560546875, 64), (-0.731048583984375, 64), (-0.930633544921875, 64), (-0.829742431640625, 64), (-0.555450439453125, 64), (-0.354766845703125, 64), (-0.150543212890625, 64), (0.089263916015625, 64)],
        },
        "rr.rr_readout_pulse.minus_sin": {
            "cosine": [(0.032196044921875, 64), (0.220123291015625, 64), (0.477630615234375, 64), (0.690277099609375, 64), (0.854461669921875, 64), (0.682342529296875, 64), (0.196197509765625, 64), (-0.213714599609375, 64), (-0.43701171875, 64), (-0.58258056640625, 64), (-0.737762451171875, 64), (-0.788360595703125, 64)],
            "sine": [(-0.059326171875, 64), (-0.159423828125, 64), (-0.225738525390625, 64), (-0.052581787109375, 64), (0.303924560546875, 64), (0.731048583984375, 64), (0.930633544921875, 64), (0.829742431640625, 64), (0.555450439453125, 64), (0.354766845703125, 64), (0.150543212890625, 64), (-0.089263916015625, 64)],
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
                },
                "1": {
                    "type": "MW",
                    "analog_outputs": {
                        "2": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 4361000000.0,
                                },
                            },
                        },
                        "3": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 3,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 7679500000.0,
                                },
                            },
                        },
                        "4": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 6660000000.0,
                                },
                            },
                        },
                        "6": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 8,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 5698000000.0,
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
                            "downconverter_frequency": 7679500000.0,
                        },
                    },
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
        "qubit_GF2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {'qubit_gf2_drive': 'qubit_GF2.qubitGF2_gaussian_pi_48'},
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 6),
                "upconverter": 1,
            },
            "intermediate_frequency": -49000000.0,
        },
        "rr": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {'readout_pulse': 'rr.rr_readout_pulse'},
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 3),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 1, 1),
            },
            "smearing": 0,
            "time_of_flight": 408,
            "intermediate_frequency": -40600000.0,
        },
    },
    "pulses": {
        "rr.rr_readout_pulse": {
            "length": 768,
            "waveforms": {'Q': 'rr.rr_readout_pulse.waveform.Q', 'I': 'rr.rr_readout_pulse.waveform.I'},
            "integration_weights": {'minus_sin': 'rr.rr_readout_pulse.minus_sin', 'sin': 'rr.rr_readout_pulse.sin', 'cos': 'rr.rr_readout_pulse.cos'},
            "operation": "measurement",
        },
        "qubit_GF2.qubitGF2_gaussian_pi_48": {
            "length": 48,
            "waveforms": {'Q': 'qubit_GF2.qubitGF2_gaussian_pi_48.waveform.Q', 'I': 'qubit_GF2.qubitGF2_gaussian_pi_48.waveform.I'},
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "qubit_GF2.qubitGF2_gaussian_pi_48.waveform.I": {
            "type": "arbitrary",
            "samples": [0.040600584970983816, 0.04796030513411972, 0.056245262410470794, 0.06548537521967554, 0.07569323322607498, 0.08686086617573445, 0.09895679440992976, 0.1119235416099775, 0.1256757926571024, 0.140099370920127, 0.15505118885014657, 0.17036029327464733, 0.1858300829456258, 0.2012417223552192, 0.21635871515699936, 0.23093253609953396, 0.24470915618226402, 0.2574362361159598, 0.2688707124618901, 0.27878646304957755, 0.2869817167598583, 0.2932858698352459, 0.29756538762739637] + [0.2997285068058678] * 2 + [0.29756538762739637, 0.2932858698352459, 0.28698171675985834, 0.27878646304957755, 0.26887071246189015, 0.25743623611595984, 0.24470915618226405, 0.23093253609953399, 0.2163587151569994, 0.20124172235521925, 0.1858300829456259, 0.17036029327464738, 0.15505118885014663, 0.14009937092012706, 0.1256757926571025, 0.11192354160997761, 0.09895679440992981, 0.08686086617573453, 0.07569323322607505, 0.06548537521967561, 0.05624526241047086, 0.047960305134119766, 0.040600584970983816],
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.020000000000000004] * 512 + [0.0] * 256,
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "rr.rr_readout_pulse.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit_GF2.qubitGF2_gaussian_pi_48.waveform.Q": {
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
            "cosine": [(0.059326171875, 64), (0.159423828125, 64), (0.225738525390625, 64), (0.052581787109375, 64), (-0.303924560546875, 64), (-0.731048583984375, 64), (-0.930633544921875, 64), (-0.829742431640625, 64), (-0.555450439453125, 64), (-0.354766845703125, 64), (-0.150543212890625, 64), (0.089263916015625, 64)],
            "sine": [(0.032196044921875, 64), (0.220123291015625, 64), (0.477630615234375, 64), (0.690277099609375, 64), (0.854461669921875, 64), (0.682342529296875, 64), (0.196197509765625, 64), (-0.213714599609375, 64), (-0.43701171875, 64), (-0.58258056640625, 64), (-0.737762451171875, 64), (-0.788360595703125, 64)],
        },
        "rr.rr_readout_pulse.sin": {
            "cosine": [(-0.032196044921875, 64), (-0.220123291015625, 64), (-0.477630615234375, 64), (-0.690277099609375, 64), (-0.854461669921875, 64), (-0.682342529296875, 64), (-0.196197509765625, 64), (0.213714599609375, 64), (0.43701171875, 64), (0.58258056640625, 64), (0.737762451171875, 64), (0.788360595703125, 64)],
            "sine": [(0.059326171875, 64), (0.159423828125, 64), (0.225738525390625, 64), (0.052581787109375, 64), (-0.303924560546875, 64), (-0.731048583984375, 64), (-0.930633544921875, 64), (-0.829742431640625, 64), (-0.555450439453125, 64), (-0.354766845703125, 64), (-0.150543212890625, 64), (0.089263916015625, 64)],
        },
        "rr.rr_readout_pulse.minus_sin": {
            "cosine": [(0.032196044921875, 64), (0.220123291015625, 64), (0.477630615234375, 64), (0.690277099609375, 64), (0.854461669921875, 64), (0.682342529296875, 64), (0.196197509765625, 64), (-0.213714599609375, 64), (-0.43701171875, 64), (-0.58258056640625, 64), (-0.737762451171875, 64), (-0.788360595703125, 64)],
            "sine": [(-0.059326171875, 64), (-0.159423828125, 64), (-0.225738525390625, 64), (-0.052581787109375, 64), (0.303924560546875, 64), (0.731048583984375, 64), (0.930633544921875, 64), (0.829742431640625, 64), (0.555450439453125, 64), (0.354766845703125, 64), (0.150543212890625, 64), (-0.089263916015625, 64)],
        },
    },
    "mixers": {},
}



if __name__ == '__main__':
    # 1. Connect to QM and execute
    qmm = QuantumMachinesManager('192.168.111.181')
    qm = qmm.open_qm(config, close_other_machines=True)
    job = qm.execute(prog)
    print('>>> Program execution started!')

    results = job.result_handles
    handles = {name: results.get(name) for name in results.keys()}
    print(f'Available result handles: {list(handles.keys())}')

    # 2. Track execution progress if 'iteration' or 'r1' is streamed
    iter_handle = handles.get('iteration') or handles.get('r1')
    if iter_handle:
        while results.is_processing():
            try:
                completed = iter_handle.count_so_far()
                print(f'Progress: {completed} iterations completed', end='\r')
            except Exception:
                pass
            time.sleep(0.3)
        print('\n>>> Execution complete on hardware!')
    else:
        print('Waiting for job completion...')
        results.wait_for_all_values()

    # 3. Automatically fetch and plot all streams
    fetched_data = {}
    for name, handle in handles.items():
        if handle is None:
            continue
        try:
            data = handle.fetch_all()
            if data is not None and getattr(data, 'size', 0) > 0:
                # Convert complex IQ data to magnitude
                if np.iscomplexobj(data):
                    data = np.abs(data)
                fetched_data[name] = data
                print(f'Fetched stream [{name}] with shape: {data.shape}')
        except Exception as e:
            print(f'Could not fetch stream [{name}]: {e}')

    # 4. Auto Plotting
    plot_keys = [k for k in fetched_data.keys() if k not in ['iteration', 'r1', 'r2']]
    if plot_keys:
        plt.figure(figsize=(9, 4.5))
        for key in plot_keys:
            d = fetched_data[key]
            if d.ndim == 1:
                plt.plot(d, label=key, linewidth=1.5)
            elif d.ndim == 2:
                plt.imshow(d, aspect='auto', origin='lower')
                plt.colorbar(label=key)
        plt.title('QUA Program Results')
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.show()
    else:
        print('No plottable data streams were found.')
