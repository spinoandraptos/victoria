# Auto-generated standalone QUA execution script
import time
import numpy as np
import matplotlib.pyplot as plt
from qm import QuantumMachinesManager
from qm.qua import *


# Single QUA script generated at 2026-08-18 09:48:00.506084
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
        with for_(v2,-1.5,(v2<1.732),(v2+0.06400000000000006)):
            r2 = declare_output_stream()
            save(v2, r2)
            reset_if_phase('qubit')
            reset_frame('qubit')
            play('qubit_drive'*amp(v2), 'qubit')
            align('qubit', 'rr')
            measure('readout_pulse'*amp(1), 'rr', dual_demod.full("cos", "sin", v3), dual_demod.full("minus_sin", "cos", v4))
            wait(37500, 'rr')
            r3 = declare_output_stream()
            save(v3, r3)
            r4 = declare_output_stream()
            save(v4, r4)
    with stream_processing():
        r2.buffer(51).save("qubit_pulse_amplitude")
        r3.buffer(51).save_all("I")
        r3.buffer(51).average().save("I_avg")
        r4.buffer(51).save_all("Q")
        r4.buffer(51).average().save("Q_avg")

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
                        "1": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 3750000000.0,
                                },
                            },
                        },
                        "2": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 4154600000.0,
                                },
                            },
                        },
                        "3": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -11,
                            "band": 3,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 7520800000.0,
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
                    },
                    "analog_inputs": {
                        "1": {
                            "band": 3,
                            "shareable": False,
                            "gain_db": 0,
                            "sampling_rate": 1000000000.0,
                            "downconverter_frequency": 7520800000.0,
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
            "operations": {'qubit_drive': 'qubit.qubit_constant_pi_pulse_1000'},
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
            "intermediate_frequency": 207000000.0,
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
            "intermediate_frequency": -49800000.0,
        },
    },
    "pulses": {
        "rr.rr_readout_pulse": {
            "length": 1280,
            "waveforms": {'Q': 'rr.rr_readout_pulse.waveform.Q', 'I': 'rr.rr_readout_pulse.waveform.I'},
            "integration_weights": {'minus_sin': 'rr.rr_readout_pulse.minus_sin', 'sin': 'rr.rr_readout_pulse.sin', 'cos': 'rr.rr_readout_pulse.cos'},
            "operation": "measurement",
        },
        "qubit.qubit_constant_pi_pulse_1000": {
            "length": 1000,
            "waveforms": {'Q': 'qubit.qubit_constant_pi_pulse_1000.waveform.Q', 'I': 'qubit.qubit_constant_pi_pulse_1000.waveform.I'},
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "qubit.qubit_constant_pi_pulse_1000.waveform.I": {
            "type": "constant",
            "sample": 0.025906735751295342,
        },
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.12] * 640 + [0.0] * 640,
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "rr.rr_readout_pulse.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit.qubit_constant_pi_pulse_1000.waveform.Q": {
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
            "cosine": [(0.010986328125, 64), (0.0826416015625, 64), (0.332550048828125, 64), (0.62481689453125, 64), (0.908721923828125, 64), (0.98956298828125, 64), (0.72650146484375, 64), (0.12237548828125, 64), (-0.22149658203125, 64), (-0.3553466796875, 64), (-0.22137451171875, 64), (-0.112945556640625, 64), (-0.169525146484375, 64), (-0.332794189453125, 64), (-0.46319580078125, 64), (-0.4693603515625, 64), (-0.31402587890625, 64), (-0.0560302734375, 64), (0.093597412109375, 64), (0.081298828125, 64)],
            "sine": [(-0.037506103515625, 64), (-0.21380615234375, 64), (-0.41119384765625, 64), (-0.41357421875, 64), (-0.205230712890625, 64), (0.14410400390625, 64), (0.550201416015625, 64), (0.624725341796875, 64), (0.52032470703125, 64), (0.18597412109375, 64), (0.025421142578125, 64), (0.0521240234375, 64), (0.16900634765625, 64), (0.16180419921875, 64), (0.035491943359375, 64), (-0.216522216796875, 64), (-0.39691162109375, 64), (-0.436431884765625, 64), (-0.325042724609375, 64), (-0.133331298828125, 64)],
        },
        "rr.rr_readout_pulse.sin": {
            "cosine": [(0.037506103515625, 64), (0.21380615234375, 64), (0.41119384765625, 64), (0.41357421875, 64), (0.205230712890625, 64), (-0.14410400390625, 64), (-0.550201416015625, 64), (-0.624725341796875, 64), (-0.52032470703125, 64), (-0.18597412109375, 64), (-0.025421142578125, 64), (-0.0521240234375, 64), (-0.16900634765625, 64), (-0.16180419921875, 64), (-0.035491943359375, 64), (0.216522216796875, 64), (0.39691162109375, 64), (0.436431884765625, 64), (0.325042724609375, 64), (0.133331298828125, 64)],
            "sine": [(0.010986328125, 64), (0.0826416015625, 64), (0.332550048828125, 64), (0.62481689453125, 64), (0.908721923828125, 64), (0.98956298828125, 64), (0.72650146484375, 64), (0.12237548828125, 64), (-0.22149658203125, 64), (-0.3553466796875, 64), (-0.22137451171875, 64), (-0.112945556640625, 64), (-0.169525146484375, 64), (-0.332794189453125, 64), (-0.46319580078125, 64), (-0.4693603515625, 64), (-0.31402587890625, 64), (-0.0560302734375, 64), (0.093597412109375, 64), (0.081298828125, 64)],
        },
        "rr.rr_readout_pulse.minus_sin": {
            "cosine": [(-0.037506103515625, 64), (-0.21380615234375, 64), (-0.41119384765625, 64), (-0.41357421875, 64), (-0.205230712890625, 64), (0.14410400390625, 64), (0.550201416015625, 64), (0.624725341796875, 64), (0.52032470703125, 64), (0.18597412109375, 64), (0.025421142578125, 64), (0.0521240234375, 64), (0.16900634765625, 64), (0.16180419921875, 64), (0.035491943359375, 64), (-0.216522216796875, 64), (-0.39691162109375, 64), (-0.436431884765625, 64), (-0.325042724609375, 64), (-0.133331298828125, 64)],
            "sine": [(-0.010986328125, 64), (-0.0826416015625, 64), (-0.332550048828125, 64), (-0.62481689453125, 64), (-0.908721923828125, 64), (-0.98956298828125, 64), (-0.72650146484375, 64), (-0.12237548828125, 64), (0.22149658203125, 64), (0.3553466796875, 64), (0.22137451171875, 64), (0.112945556640625, 64), (0.169525146484375, 64), (0.332794189453125, 64), (0.46319580078125, 64), (0.4693603515625, 64), (0.31402587890625, 64), (0.0560302734375, 64), (-0.093597412109375, 64), (-0.081298828125, 64)],
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
                        "1": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 3750000000.0,
                                },
                            },
                        },
                        "2": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 4154600000.0,
                                },
                            },
                        },
                        "3": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -11,
                            "band": 3,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 7520800000.0,
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
                    },
                    "analog_inputs": {
                        "1": {
                            "band": 3,
                            "shareable": False,
                            "gain_db": 0,
                            "sampling_rate": 1000000000.0,
                            "downconverter_frequency": 7520800000.0,
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
            "operations": {'qubit_drive': 'qubit.qubit_constant_pi_pulse_1000'},
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
            "intermediate_frequency": 207000000.0,
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
            "intermediate_frequency": -49800000.0,
        },
    },
    "pulses": {
        "rr.rr_readout_pulse": {
            "length": 1280,
            "waveforms": {'Q': 'rr.rr_readout_pulse.waveform.Q', 'I': 'rr.rr_readout_pulse.waveform.I'},
            "integration_weights": {'minus_sin': 'rr.rr_readout_pulse.minus_sin', 'sin': 'rr.rr_readout_pulse.sin', 'cos': 'rr.rr_readout_pulse.cos'},
            "operation": "measurement",
        },
        "qubit.qubit_constant_pi_pulse_1000": {
            "length": 1000,
            "waveforms": {'Q': 'qubit.qubit_constant_pi_pulse_1000.waveform.Q', 'I': 'qubit.qubit_constant_pi_pulse_1000.waveform.I'},
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "qubit.qubit_constant_pi_pulse_1000.waveform.I": {
            "type": "constant",
            "sample": 0.025906735751295342,
        },
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.12] * 640 + [0.0] * 640,
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "rr.rr_readout_pulse.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit.qubit_constant_pi_pulse_1000.waveform.Q": {
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
            "cosine": [(0.010986328125, 64), (0.0826416015625, 64), (0.332550048828125, 64), (0.62481689453125, 64), (0.908721923828125, 64), (0.98956298828125, 64), (0.72650146484375, 64), (0.12237548828125, 64), (-0.22149658203125, 64), (-0.3553466796875, 64), (-0.22137451171875, 64), (-0.112945556640625, 64), (-0.169525146484375, 64), (-0.332794189453125, 64), (-0.46319580078125, 64), (-0.4693603515625, 64), (-0.31402587890625, 64), (-0.0560302734375, 64), (0.093597412109375, 64), (0.081298828125, 64)],
            "sine": [(-0.037506103515625, 64), (-0.21380615234375, 64), (-0.41119384765625, 64), (-0.41357421875, 64), (-0.205230712890625, 64), (0.14410400390625, 64), (0.550201416015625, 64), (0.624725341796875, 64), (0.52032470703125, 64), (0.18597412109375, 64), (0.025421142578125, 64), (0.0521240234375, 64), (0.16900634765625, 64), (0.16180419921875, 64), (0.035491943359375, 64), (-0.216522216796875, 64), (-0.39691162109375, 64), (-0.436431884765625, 64), (-0.325042724609375, 64), (-0.133331298828125, 64)],
        },
        "rr.rr_readout_pulse.sin": {
            "cosine": [(0.037506103515625, 64), (0.21380615234375, 64), (0.41119384765625, 64), (0.41357421875, 64), (0.205230712890625, 64), (-0.14410400390625, 64), (-0.550201416015625, 64), (-0.624725341796875, 64), (-0.52032470703125, 64), (-0.18597412109375, 64), (-0.025421142578125, 64), (-0.0521240234375, 64), (-0.16900634765625, 64), (-0.16180419921875, 64), (-0.035491943359375, 64), (0.216522216796875, 64), (0.39691162109375, 64), (0.436431884765625, 64), (0.325042724609375, 64), (0.133331298828125, 64)],
            "sine": [(0.010986328125, 64), (0.0826416015625, 64), (0.332550048828125, 64), (0.62481689453125, 64), (0.908721923828125, 64), (0.98956298828125, 64), (0.72650146484375, 64), (0.12237548828125, 64), (-0.22149658203125, 64), (-0.3553466796875, 64), (-0.22137451171875, 64), (-0.112945556640625, 64), (-0.169525146484375, 64), (-0.332794189453125, 64), (-0.46319580078125, 64), (-0.4693603515625, 64), (-0.31402587890625, 64), (-0.0560302734375, 64), (0.093597412109375, 64), (0.081298828125, 64)],
        },
        "rr.rr_readout_pulse.minus_sin": {
            "cosine": [(-0.037506103515625, 64), (-0.21380615234375, 64), (-0.41119384765625, 64), (-0.41357421875, 64), (-0.205230712890625, 64), (0.14410400390625, 64), (0.550201416015625, 64), (0.624725341796875, 64), (0.52032470703125, 64), (0.18597412109375, 64), (0.025421142578125, 64), (0.0521240234375, 64), (0.16900634765625, 64), (0.16180419921875, 64), (0.035491943359375, 64), (-0.216522216796875, 64), (-0.39691162109375, 64), (-0.436431884765625, 64), (-0.325042724609375, 64), (-0.133331298828125, 64)],
            "sine": [(-0.010986328125, 64), (-0.0826416015625, 64), (-0.332550048828125, 64), (-0.62481689453125, 64), (-0.908721923828125, 64), (-0.98956298828125, 64), (-0.72650146484375, 64), (-0.12237548828125, 64), (0.22149658203125, 64), (0.3553466796875, 64), (0.22137451171875, 64), (0.112945556640625, 64), (0.169525146484375, 64), (0.332794189453125, 64), (0.46319580078125, 64), (0.4693603515625, 64), (0.31402587890625, 64), (0.0560302734375, 64), (-0.093597412109375, 64), (-0.081298828125, 64)],
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
