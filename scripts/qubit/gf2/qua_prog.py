# Auto-generated standalone QUA execution script
import time
import numpy as np
import matplotlib.pyplot as plt
from qm import QuantumMachinesManager
from qm.qua import *


# Single QUA script generated at 2026-08-05 20:53:04.542996
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
            wait(5000, 'rr')
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
                            "full_scale_power_dbm": 8,
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 4094900000.0,
                                },
                            },
                        },
                        "4": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 8,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 5250000000.0,
                                },
                            },
                        },
                        "5": {
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
                            "full_scale_power_dbm": -11,
                            "band": 3,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 7520000000.0,
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
                            "downconverter_frequency": 7520000000.0,
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
            "operations": {'qubit_gf2_drive': 'qubit_GF2.qubitGF2_constant_pi_200'},
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 4),
                "upconverter": 1,
            },
            "intermediate_frequency": 115000000.0,
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
            "intermediate_frequency": -48600000.0,
        },
    },
    "pulses": {
        "qubit_GF2.qubitGF2_constant_pi_200": {
            "length": 200,
            "waveforms": {'Q': 'qubit_GF2.qubitGF2_constant_pi_200.waveform.Q', 'I': 'qubit_GF2.qubitGF2_constant_pi_200.waveform.I'},
            "integration_weights": {},
            "operation": "control",
        },
        "rr.rr_readout_pulse": {
            "length": 640,
            "waveforms": {'Q': 'rr.rr_readout_pulse.waveform.Q', 'I': 'rr.rr_readout_pulse.waveform.I'},
            "integration_weights": {'minus_sin': 'rr.rr_readout_pulse.minus_sin', 'sin': 'rr.rr_readout_pulse.sin', 'cos': 'rr.rr_readout_pulse.cos'},
            "operation": "measurement",
        },
    },
    "waveforms": {
        "rr.rr_readout_pulse.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.04000000000000001] * 320 + [0.0] * 320,
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "qubit_GF2.qubitGF2_constant_pi_200.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit_GF2.qubitGF2_constant_pi_200.waveform.I": {
            "type": "constant",
            "sample": 0.30000000000000004,
        },
    },
    "digital_waveforms": {
        "rr.rr_readout_pulse.ADC_ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "rr.rr_readout_pulse.cos": {
            "cosine": [(0.00079345703125, 64), (0.250732421875, 64), (0.3436279296875, 64), (0.308837890625, 64), (0.13897705078125, 64), (0.091217041015625, 64), (-0.06060791015625, 64), (-0.07135009765625, 64), (0.1973876953125, 64), (0.3499755859375, 64)],
            "sine": [(0.073211669921875, 64), (0.110626220703125, 64), (0.392333984375, 64), (0.871490478515625, 64), (0.95623779296875, 64), (0.995819091796875, 64), (0.951202392578125, 64), (0.7540283203125, 64), (0.552581787109375, 64), (0.42462158203125, 64)],
        },
        "rr.rr_readout_pulse.sin": {
            "cosine": [(-0.073211669921875, 64), (-0.110626220703125, 64), (-0.392333984375, 64), (-0.871490478515625, 64), (-0.95623779296875, 64), (-0.995819091796875, 64), (-0.951202392578125, 64), (-0.7540283203125, 64), (-0.552581787109375, 64), (-0.42462158203125, 64)],
            "sine": [(0.00079345703125, 64), (0.250732421875, 64), (0.3436279296875, 64), (0.308837890625, 64), (0.13897705078125, 64), (0.091217041015625, 64), (-0.06060791015625, 64), (-0.07135009765625, 64), (0.1973876953125, 64), (0.3499755859375, 64)],
        },
        "rr.rr_readout_pulse.minus_sin": {
            "cosine": [(0.073211669921875, 64), (0.110626220703125, 64), (0.392333984375, 64), (0.871490478515625, 64), (0.95623779296875, 64), (0.995819091796875, 64), (0.951202392578125, 64), (0.7540283203125, 64), (0.552581787109375, 64), (0.42462158203125, 64)],
            "sine": [(-0.00079345703125, 64), (-0.250732421875, 64), (-0.3436279296875, 64), (-0.308837890625, 64), (-0.13897705078125, 64), (-0.091217041015625, 64), (0.06060791015625, 64), (0.07135009765625, 64), (-0.1973876953125, 64), (-0.3499755859375, 64)],
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
                                    "frequency": 4094900000.0,
                                },
                            },
                        },
                        "4": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 8,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 5250000000.0,
                                },
                            },
                        },
                        "5": {
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
                            "full_scale_power_dbm": -11,
                            "band": 3,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 7520000000.0,
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
                            "downconverter_frequency": 7520000000.0,
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
            "operations": {'qubit_gf2_drive': 'qubit_GF2.qubitGF2_constant_pi_200'},
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 4),
                "upconverter": 1,
            },
            "intermediate_frequency": 115000000.0,
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
            "intermediate_frequency": -48600000.0,
        },
    },
    "pulses": {
        "qubit_GF2.qubitGF2_constant_pi_200": {
            "length": 200,
            "waveforms": {'Q': 'qubit_GF2.qubitGF2_constant_pi_200.waveform.Q', 'I': 'qubit_GF2.qubitGF2_constant_pi_200.waveform.I'},
            "integration_weights": {},
            "operation": "control",
        },
        "rr.rr_readout_pulse": {
            "length": 640,
            "waveforms": {'Q': 'rr.rr_readout_pulse.waveform.Q', 'I': 'rr.rr_readout_pulse.waveform.I'},
            "integration_weights": {'minus_sin': 'rr.rr_readout_pulse.minus_sin', 'sin': 'rr.rr_readout_pulse.sin', 'cos': 'rr.rr_readout_pulse.cos'},
            "operation": "measurement",
        },
    },
    "waveforms": {
        "rr.rr_readout_pulse.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.04000000000000001] * 320 + [0.0] * 320,
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "qubit_GF2.qubitGF2_constant_pi_200.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit_GF2.qubitGF2_constant_pi_200.waveform.I": {
            "type": "constant",
            "sample": 0.30000000000000004,
        },
    },
    "digital_waveforms": {
        "rr.rr_readout_pulse.ADC_ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "rr.rr_readout_pulse.cos": {
            "cosine": [(0.00079345703125, 64), (0.250732421875, 64), (0.3436279296875, 64), (0.308837890625, 64), (0.13897705078125, 64), (0.091217041015625, 64), (-0.06060791015625, 64), (-0.07135009765625, 64), (0.1973876953125, 64), (0.3499755859375, 64)],
            "sine": [(0.073211669921875, 64), (0.110626220703125, 64), (0.392333984375, 64), (0.871490478515625, 64), (0.95623779296875, 64), (0.995819091796875, 64), (0.951202392578125, 64), (0.7540283203125, 64), (0.552581787109375, 64), (0.42462158203125, 64)],
        },
        "rr.rr_readout_pulse.sin": {
            "cosine": [(-0.073211669921875, 64), (-0.110626220703125, 64), (-0.392333984375, 64), (-0.871490478515625, 64), (-0.95623779296875, 64), (-0.995819091796875, 64), (-0.951202392578125, 64), (-0.7540283203125, 64), (-0.552581787109375, 64), (-0.42462158203125, 64)],
            "sine": [(0.00079345703125, 64), (0.250732421875, 64), (0.3436279296875, 64), (0.308837890625, 64), (0.13897705078125, 64), (0.091217041015625, 64), (-0.06060791015625, 64), (-0.07135009765625, 64), (0.1973876953125, 64), (0.3499755859375, 64)],
        },
        "rr.rr_readout_pulse.minus_sin": {
            "cosine": [(0.073211669921875, 64), (0.110626220703125, 64), (0.392333984375, 64), (0.871490478515625, 64), (0.95623779296875, 64), (0.995819091796875, 64), (0.951202392578125, 64), (0.7540283203125, 64), (0.552581787109375, 64), (0.42462158203125, 64)],
            "sine": [(-0.00079345703125, 64), (-0.250732421875, 64), (-0.3436279296875, 64), (-0.308837890625, 64), (-0.13897705078125, 64), (-0.091217041015625, 64), (0.06060791015625, 64), (0.07135009765625, 64), (-0.1973876953125, 64), (-0.3499755859375, 64)],
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
