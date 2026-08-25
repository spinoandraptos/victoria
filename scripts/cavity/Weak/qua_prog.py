# Auto-generated standalone QUA execution script
import time
import numpy as np
import matplotlib.pyplot as plt
from qm import QuantumMachinesManager
from qm.qua import *


# Single QUA script generated at 2026-08-25 02:45:56.593983
# QUA library version: 1.3.1


from qm import CompilerOptionArguments
from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    v4 = declare(fixed, )
    v5 = declare(fixed, )
    with for_(v1,1,(v1<5001),(v1+1)):
        r1 = declare_output_stream()
        save(v1, r1)
        with for_(v2,-1.5,(v2<1.55),(v2+0.1)):
            r2 = declare_output_stream()
            save(v2, r2)
            with for_(v3,-1.5,(v3<1.55),(v3+0.1)):
                r3 = declare_output_stream()
                save(v3, r3)
                reset_if_phase('cavity')
                reset_frame('cavity')
                play('cav_disp'*amp(1.5), 'cavity')
                align()
                wait(125000, )
                align()
                align('qubit', 'cavity')
                play('qubit_pi2'*amp(1.0), 'qubit')
                align('cavity', 'qubit')
                play('cav_disp'*amp(v2, (0.0-v3), v3, v2), 'cavity')
                wait(40, 'cavity')
                play('cav_disp'*amp((0.0-v2), v3, (0.0-v3), (0.0-v2)), 'cavity')
                align('qubit', 'cavity')
                frame_rotation_2pi(0.25, 'qubit')
                play('qubit_pi'*amp(1.0), 'qubit')
                frame_rotation_2pi(-0.25, 'qubit')
                align('cavity', 'qubit')
                play('cav_disp'*amp((0.0-v2), v3, (0.0-v3), (0.0-v2)), 'cavity')
                wait(40, 'cavity')
                play('cav_disp'*amp(v2, (0.0-v3), v3, v2), 'cavity')
                align('qubit', 'cavity')
                play('qubit_pi2'*amp(1.0), 'qubit')
                align()
                measure('readout_pulse'*amp(1.0), 'rr', dual_demod.full("cos", "sin", v4), dual_demod.full("minus_sin", "cos", v5))
                wait(150000, 'rr')
                r4 = declare_output_stream()
                save(v4, r4)
                r5 = declare_output_stream()
                save(v5, r5)
    with stream_processing():
        r2.buffer(31).save("ampx_x")
        r3.buffer(31).save("ampx_y")
        r4.buffer(31, 31).save_all("I")
        r4.buffer(31, 31).average().save("I_avg")
        r5.buffer(31, 31).save_all("Q")
        r5.buffer(31, 31).average().save("Q_avg")

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
                                    "frequency": 2947000000.0,
                                },
                            },
                        },
                        "3": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -2,
                            "band": 3,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 7662850000.0,
                                },
                            },
                        },
                        "4": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 2975141510.0,
                                },
                            },
                        },
                        "6": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 8,
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 4285700000.0,
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
                            "downconverter_frequency": 7662850000.0,
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
            "operations": {'qubit_pi': 'qubit.qubit_gaussian_pi_pulse_24', 'qubit_pi2': 'qubit.qubit_gaussian_pi2_pulse_24'},
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
            "intermediate_frequency": 50000000.0,
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
            "intermediate_frequency": -50000000.0,
        },
        "cavity": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {'cav_disp': 'cavity.cav_constant_40', 'cav_disp_state': 'cavity.cav_constant_40'},
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
            "intermediate_frequency": -50000000.0,
        },
    },
    "pulses": {
        "qubit.qubit_gaussian_pi_pulse_24": {
            "length": 24,
            "waveforms": {'Q': 'qubit.qubit_gaussian_pi_pulse_24.waveform.Q', 'I': 'qubit.qubit_gaussian_pi_pulse_24.waveform.I'},
            "integration_weights": {},
            "operation": "control",
        },
        "rr.rr_readout_pulse": {
            "length": 1280,
            "waveforms": {'Q': 'rr.rr_readout_pulse.waveform.Q', 'I': 'rr.rr_readout_pulse.waveform.I'},
            "integration_weights": {'minus_sin': 'rr.rr_readout_pulse.minus_sin', 'sin': 'rr.rr_readout_pulse.sin', 'cos': 'rr.rr_readout_pulse.cos'},
            "operation": "measurement",
        },
        "qubit.qubit_gaussian_pi2_pulse_24": {
            "length": 24,
            "waveforms": {'Q': 'qubit.qubit_gaussian_pi2_pulse_24.waveform.Q', 'I': 'qubit.qubit_gaussian_pi2_pulse_24.waveform.I'},
            "integration_weights": {},
            "operation": "control",
        },
        "cavity.cav_constant_40": {
            "length": 40,
            "waveforms": {'Q': 'cavity.cav_constant_40.waveform.Q', 'I': 'cavity.cav_constant_40.waveform.I'},
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "qubit.qubit_gaussian_pi2_pulse_24.waveform.I": {
            "type": "arbitrary",
            "samples": [0.008055671621226947, 0.011235513457369303, 0.0152036734516181, 0.019960369711441134, 0.025424537903029724, 0.0314196971402987, 0.037671712221568725, 0.04382209785166572, 0.04945786990219127, 0.054155440220913335, 0.0575324955139118] + [0.05929919164171237] * 2 + [0.0575324955139118, 0.05415544022091334, 0.04945786990219127, 0.04382209785166573, 0.037671712221568725, 0.031419697140298714, 0.02542453790302973, 0.019960369711441134, 0.015203673451618107, 0.01123551345736931, 0.008055671621226947],
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "cavity.cav_constant_40.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.013500000000000002] * 640 + [0.0] * 640,
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "rr.rr_readout_pulse.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit.qubit_gaussian_pi_pulse_24.waveform.I": {
            "type": "arbitrary",
            "samples": [0.016111343242453894, 0.022471026914738606, 0.0304073469032362, 0.03992073942288227, 0.05084907580605945, 0.0628393942805974, 0.07534342444313745, 0.08764419570333144, 0.09891573980438254, 0.10831088044182667, 0.1150649910278236] + [0.11859838328342474] * 2 + [0.1150649910278236, 0.10831088044182668, 0.09891573980438254, 0.08764419570333146, 0.07534342444313745, 0.06283939428059743, 0.05084907580605946, 0.03992073942288227, 0.030407346903236213, 0.02247102691473862, 0.016111343242453894],
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "cavity.cav_constant_40.waveform.I": {
            "type": "constant",
            "sample": 0.2,
        },
        "qubit.qubit_gaussian_pi2_pulse_24.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit.qubit_gaussian_pi_pulse_24.waveform.Q": {
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
                                    "frequency": 2947000000.0,
                                },
                            },
                        },
                        "3": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -2,
                            "band": 3,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 7662850000.0,
                                },
                            },
                        },
                        "4": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 2975141510.0,
                                },
                            },
                        },
                        "6": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 8,
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 4285700000.0,
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
                            "downconverter_frequency": 7662850000.0,
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
            "operations": {'qubit_pi': 'qubit.qubit_gaussian_pi_pulse_24', 'qubit_pi2': 'qubit.qubit_gaussian_pi2_pulse_24'},
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
            "intermediate_frequency": 50000000.0,
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
            "intermediate_frequency": -50000000.0,
        },
        "cavity": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {'cav_disp': 'cavity.cav_constant_40', 'cav_disp_state': 'cavity.cav_constant_40'},
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
            "intermediate_frequency": -50000000.0,
        },
    },
    "pulses": {
        "qubit.qubit_gaussian_pi_pulse_24": {
            "length": 24,
            "waveforms": {'Q': 'qubit.qubit_gaussian_pi_pulse_24.waveform.Q', 'I': 'qubit.qubit_gaussian_pi_pulse_24.waveform.I'},
            "integration_weights": {},
            "operation": "control",
        },
        "rr.rr_readout_pulse": {
            "length": 1280,
            "waveforms": {'Q': 'rr.rr_readout_pulse.waveform.Q', 'I': 'rr.rr_readout_pulse.waveform.I'},
            "integration_weights": {'minus_sin': 'rr.rr_readout_pulse.minus_sin', 'sin': 'rr.rr_readout_pulse.sin', 'cos': 'rr.rr_readout_pulse.cos'},
            "operation": "measurement",
        },
        "qubit.qubit_gaussian_pi2_pulse_24": {
            "length": 24,
            "waveforms": {'Q': 'qubit.qubit_gaussian_pi2_pulse_24.waveform.Q', 'I': 'qubit.qubit_gaussian_pi2_pulse_24.waveform.I'},
            "integration_weights": {},
            "operation": "control",
        },
        "cavity.cav_constant_40": {
            "length": 40,
            "waveforms": {'Q': 'cavity.cav_constant_40.waveform.Q', 'I': 'cavity.cav_constant_40.waveform.I'},
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "qubit.qubit_gaussian_pi2_pulse_24.waveform.I": {
            "type": "arbitrary",
            "samples": [0.008055671621226947, 0.011235513457369303, 0.0152036734516181, 0.019960369711441134, 0.025424537903029724, 0.0314196971402987, 0.037671712221568725, 0.04382209785166572, 0.04945786990219127, 0.054155440220913335, 0.0575324955139118] + [0.05929919164171237] * 2 + [0.0575324955139118, 0.05415544022091334, 0.04945786990219127, 0.04382209785166573, 0.037671712221568725, 0.031419697140298714, 0.02542453790302973, 0.019960369711441134, 0.015203673451618107, 0.01123551345736931, 0.008055671621226947],
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "cavity.cav_constant_40.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.013500000000000002] * 640 + [0.0] * 640,
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "rr.rr_readout_pulse.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit.qubit_gaussian_pi_pulse_24.waveform.I": {
            "type": "arbitrary",
            "samples": [0.016111343242453894, 0.022471026914738606, 0.0304073469032362, 0.03992073942288227, 0.05084907580605945, 0.0628393942805974, 0.07534342444313745, 0.08764419570333144, 0.09891573980438254, 0.10831088044182667, 0.1150649910278236] + [0.11859838328342474] * 2 + [0.1150649910278236, 0.10831088044182668, 0.09891573980438254, 0.08764419570333146, 0.07534342444313745, 0.06283939428059743, 0.05084907580605946, 0.03992073942288227, 0.030407346903236213, 0.02247102691473862, 0.016111343242453894],
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "cavity.cav_constant_40.waveform.I": {
            "type": "constant",
            "sample": 0.2,
        },
        "qubit.qubit_gaussian_pi2_pulse_24.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit.qubit_gaussian_pi_pulse_24.waveform.Q": {
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
