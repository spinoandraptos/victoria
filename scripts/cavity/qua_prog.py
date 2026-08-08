# Auto-generated standalone QUA execution script
import time
import numpy as np
import matplotlib.pyplot as plt
from qm import QuantumMachinesManager
from qm.qua import *


# Single QUA script generated at 2026-08-08 13:54:18.912970
# QUA library version: 1.3.1


from qm import CompilerOptionArguments
from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(int, )
    v3 = declare(fixed, )
    v4 = declare(fixed, )
    with for_(v1,1,(v1<501),(v1+1)):
        r1 = declare_output_stream()
        save(v1, r1)
        with for_(v2,-65000000,(v2<-61992500),(v2+15000)):
            r2 = declare_output_stream()
            save(v2, r2)
            update_frequency('cavity', v2, 'Hz', False)
            play('cavity_pulse'*amp(1), 'cavity')
            align('cavity', 'qubit')
            play('qubit_pulse'*amp(1.0), 'qubit')
            align('qubit', 'rr')
            align()
            measure('readout_pulse'*amp(1), 'rr', dual_demod.full("cos", "sin", v3), dual_demod.full("minus_sin", "cos", v4))
            wait(50000, 'rr')
            r3 = declare_output_stream()
            save(v3, r3)
            r4 = declare_output_stream()
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
                },
                "1": {
                    "type": "MW",
                    "analog_outputs": {
                        "2": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 8,
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 3500000000.0,
                                },
                            },
                        },
                        "4": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 8,
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 417200000.0,
                                },
                            },
                        },
                        "5": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 3000000000.0,
                                },
                            },
                        },
                        "6": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 5699000000.0,
                                },
                            },
                        },
                    },
                    "analog_inputs": {
                        "1": {
                            "band": 2,
                            "shareable": False,
                            "gain_db": 0,
                            "sampling_rate": 1000000000.0,
                            "downconverter_frequency": 5699000000.0,
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
        "qubit": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {'qubit_pulse': 'qubit.qubit_constant_pi_120'},
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": 57600000.0,
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
                "port": ('con1', 1, 6),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 1, 1),
            },
            "smearing": 0,
            "time_of_flight": 408,
            "intermediate_frequency": -56700000.0,
        },
        "cavity": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {'cavity_pulse': 'cavity.cav_constant_10000_spec'},
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 5),
                "upconverter": 1,
            },
            "intermediate_frequency": -63200000.0,
        },
    },
    "pulses": {
        "rr.rr_readout_pulse": {
            "length": 1280,
            "waveforms": {'Q': 'rr.rr_readout_pulse.waveform.Q', 'I': 'rr.rr_readout_pulse.waveform.I'},
            "integration_weights": {'minus_sin': 'rr.rr_readout_pulse.minus_sin', 'sin': 'rr.rr_readout_pulse.sin', 'cos': 'rr.rr_readout_pulse.cos'},
            "operation": "measurement",
        },
        "cavity.cav_constant_10000_spec": {
            "length": 10000,
            "waveforms": {'Q': 'cavity.cav_constant_10000_spec.waveform.Q', 'I': 'cavity.cav_constant_10000_spec.waveform.I'},
            "integration_weights": {},
            "operation": "control",
        },
        "qubit.qubit_constant_pi_120": {
            "length": 120,
            "waveforms": {'Q': 'qubit.qubit_constant_pi_120.waveform.Q', 'I': 'qubit.qubit_constant_pi_120.waveform.I'},
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "qubit.qubit_constant_pi_120.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "rr.rr_readout_pulse.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.068] * 640 + [0.0] * 640,
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "qubit.qubit_constant_pi_120.waveform.I": {
            "type": "constant",
            "sample": 0.25,
        },
        "cavity.cav_constant_10000_spec.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cavity.cav_constant_10000_spec.waveform.I": {
            "type": "constant",
            "sample": 0.0014700452643474902,
        },
    },
    "digital_waveforms": {
        "rr.rr_readout_pulse.ADC_ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "rr.rr_readout_pulse.cos": {
            "cosine": [(1.0, 1280)],
            "sine": [(0.0, 1280)],
        },
        "rr.rr_readout_pulse.sin": {
            "cosine": [(0.0, 1280)],
            "sine": [(1.0, 1280)],
        },
        "rr.rr_readout_pulse.minus_sin": {
            "cosine": [(0.0, 1280)],
            "sine": [(-1.0, 1280)],
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
                            "full_scale_power_dbm": 8,
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 3500000000.0,
                                },
                            },
                        },
                        "4": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 8,
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 417200000.0,
                                },
                            },
                        },
                        "5": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 3000000000.0,
                                },
                            },
                        },
                        "6": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 5699000000.0,
                                },
                            },
                        },
                    },
                    "analog_inputs": {
                        "1": {
                            "band": 2,
                            "shareable": False,
                            "gain_db": 0,
                            "sampling_rate": 1000000000.0,
                            "downconverter_frequency": 5699000000.0,
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
        "qubit": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {'qubit_pulse': 'qubit.qubit_constant_pi_120'},
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": 57600000.0,
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
                "port": ('con1', 1, 6),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 1, 1),
            },
            "smearing": 0,
            "time_of_flight": 408,
            "intermediate_frequency": -56700000.0,
        },
        "cavity": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {'cavity_pulse': 'cavity.cav_constant_10000_spec'},
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 5),
                "upconverter": 1,
            },
            "intermediate_frequency": -63200000.0,
        },
    },
    "pulses": {
        "rr.rr_readout_pulse": {
            "length": 1280,
            "waveforms": {'Q': 'rr.rr_readout_pulse.waveform.Q', 'I': 'rr.rr_readout_pulse.waveform.I'},
            "integration_weights": {'minus_sin': 'rr.rr_readout_pulse.minus_sin', 'sin': 'rr.rr_readout_pulse.sin', 'cos': 'rr.rr_readout_pulse.cos'},
            "operation": "measurement",
        },
        "cavity.cav_constant_10000_spec": {
            "length": 10000,
            "waveforms": {'Q': 'cavity.cav_constant_10000_spec.waveform.Q', 'I': 'cavity.cav_constant_10000_spec.waveform.I'},
            "integration_weights": {},
            "operation": "control",
        },
        "qubit.qubit_constant_pi_120": {
            "length": 120,
            "waveforms": {'Q': 'qubit.qubit_constant_pi_120.waveform.Q', 'I': 'qubit.qubit_constant_pi_120.waveform.I'},
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "qubit.qubit_constant_pi_120.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "rr.rr_readout_pulse.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.068] * 640 + [0.0] * 640,
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "qubit.qubit_constant_pi_120.waveform.I": {
            "type": "constant",
            "sample": 0.25,
        },
        "cavity.cav_constant_10000_spec.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cavity.cav_constant_10000_spec.waveform.I": {
            "type": "constant",
            "sample": 0.0014700452643474902,
        },
    },
    "digital_waveforms": {
        "rr.rr_readout_pulse.ADC_ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "rr.rr_readout_pulse.cos": {
            "cosine": [(1.0, 1280)],
            "sine": [(0.0, 1280)],
        },
        "rr.rr_readout_pulse.sin": {
            "cosine": [(0.0, 1280)],
            "sine": [(1.0, 1280)],
        },
        "rr.rr_readout_pulse.minus_sin": {
            "cosine": [(0.0, 1280)],
            "sine": [(-1.0, 1280)],
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
