# Auto-generated standalone QUA execution script
import time
import numpy as np
import matplotlib.pyplot as plt
from qm import QuantumMachinesManager
from qm.qua import *


# Single QUA script generated at 2026-08-26 13:29:23.435370
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
        with for_(v2,-1.5,(v2<1.53),(v2+0.06000000000000005)):
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
                                    "frequency": 4461000000.0,
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
                                    "frequency": 7650600000.0,
                                },
                            },
                        },
                        "4": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 7,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 6605000000.0,
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
                                    "frequency": 5746600000.0,
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
                            "downconverter_frequency": 7650600000.0,
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
            "operations": {'qubit_gf2_drive': 'qubit_GF2.qubitGF2_gaussian_pi_pulse_60'},
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
            "intermediate_frequency": -37000000.0,
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
            "time_of_flight": 396,
            "intermediate_frequency": -50000000.0,
        },
    },
    "pulses": {
        "rr.rr_readout_pulse": {
            "length": 1280,
            "waveforms": {'Q': 'rr.rr_readout_pulse.waveform.Q', 'I': 'rr.rr_readout_pulse.waveform.I'},
            "integration_weights": {'minus_sin': 'rr.rr_readout_pulse.minus_sin', 'sin': 'rr.rr_readout_pulse.sin', 'cos': 'rr.rr_readout_pulse.cos'},
            "operation": "measurement",
        },
        "qubit_GF2.qubitGF2_gaussian_pi_pulse_60": {
            "length": 60,
            "waveforms": {'Q': 'qubit_GF2.qubitGF2_gaussian_pi_pulse_60.waveform.Q', 'I': 'qubit_GF2.qubitGF2_gaussian_pi_pulse_60.waveform.I'},
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "rr.rr_readout_pulse.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.00765625] * 640 + [0.0] * 640,
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "qubit_GF2.qubitGF2_gaussian_pi_pulse_60.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit_GF2.qubitGF2_gaussian_pi_pulse_60.waveform.I": {
            "type": "arbitrary",
            "samples": [0.027067056647322542, 0.030926468305403826, 0.03517413623658342, 0.03982175280952551, 0.04487672136135559, 0.0503414459947229, 0.05621265122175424, 0.06248075506304599, 0.06912932032323425, 0.07613460905630519, 0.08346526459338478, 0.09108214385512572, 0.09893831997172102, 0.10697927149399829, 0.11514326975756815, 0.12336197036969676, 0.13156120848811403, 0.13966199076265484, 0.14758166976538709, 0.15523527972439413, 0.1625370057007208, 0.16940175231132715, 0.17574677299603322, 0.18149331691903844, 0.18656824810906125, 0.19090559054402875, 0.19444795367722997, 0.19714779540791705, 0.19896848366786285] + [0.19988512349540505] * 2 + [0.19896848366786285, 0.19714779540791705, 0.19444795367722997, 0.19090559054402875, 0.18656824810906125, 0.18149331691903844, 0.17574677299603325, 0.16940175231132718, 0.16253700570072083, 0.1552352797243942, 0.14758166976538709, 0.13966199076265484, 0.13156120848811403, 0.12336197036969683, 0.1151432697575682, 0.10697927149399832, 0.09893831997172106, 0.09108214385512575, 0.08346526459338478, 0.07613460905630519, 0.06912932032323425, 0.06248075506304599, 0.056212651221754284, 0.05034144599472293, 0.04487672136135561, 0.039821752809525525, 0.03517413623658342, 0.030926468305403826, 0.027067056647322542],
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
                                    "frequency": 4461000000.0,
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
                                    "frequency": 7650600000.0,
                                },
                            },
                        },
                        "4": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 7,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 6605000000.0,
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
                                    "frequency": 5746600000.0,
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
                            "downconverter_frequency": 7650600000.0,
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
            "operations": {'qubit_gf2_drive': 'qubit_GF2.qubitGF2_gaussian_pi_pulse_60'},
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
            "intermediate_frequency": -37000000.0,
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
            "time_of_flight": 396,
            "intermediate_frequency": -50000000.0,
        },
    },
    "pulses": {
        "rr.rr_readout_pulse": {
            "length": 1280,
            "waveforms": {'Q': 'rr.rr_readout_pulse.waveform.Q', 'I': 'rr.rr_readout_pulse.waveform.I'},
            "integration_weights": {'minus_sin': 'rr.rr_readout_pulse.minus_sin', 'sin': 'rr.rr_readout_pulse.sin', 'cos': 'rr.rr_readout_pulse.cos'},
            "operation": "measurement",
        },
        "qubit_GF2.qubitGF2_gaussian_pi_pulse_60": {
            "length": 60,
            "waveforms": {'Q': 'qubit_GF2.qubitGF2_gaussian_pi_pulse_60.waveform.Q', 'I': 'qubit_GF2.qubitGF2_gaussian_pi_pulse_60.waveform.I'},
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "rr.rr_readout_pulse.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.00765625] * 640 + [0.0] * 640,
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "qubit_GF2.qubitGF2_gaussian_pi_pulse_60.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit_GF2.qubitGF2_gaussian_pi_pulse_60.waveform.I": {
            "type": "arbitrary",
            "samples": [0.027067056647322542, 0.030926468305403826, 0.03517413623658342, 0.03982175280952551, 0.04487672136135559, 0.0503414459947229, 0.05621265122175424, 0.06248075506304599, 0.06912932032323425, 0.07613460905630519, 0.08346526459338478, 0.09108214385512572, 0.09893831997172102, 0.10697927149399829, 0.11514326975756815, 0.12336197036969676, 0.13156120848811403, 0.13966199076265484, 0.14758166976538709, 0.15523527972439413, 0.1625370057007208, 0.16940175231132715, 0.17574677299603322, 0.18149331691903844, 0.18656824810906125, 0.19090559054402875, 0.19444795367722997, 0.19714779540791705, 0.19896848366786285] + [0.19988512349540505] * 2 + [0.19896848366786285, 0.19714779540791705, 0.19444795367722997, 0.19090559054402875, 0.18656824810906125, 0.18149331691903844, 0.17574677299603325, 0.16940175231132718, 0.16253700570072083, 0.1552352797243942, 0.14758166976538709, 0.13966199076265484, 0.13156120848811403, 0.12336197036969683, 0.1151432697575682, 0.10697927149399832, 0.09893831997172106, 0.09108214385512575, 0.08346526459338478, 0.07613460905630519, 0.06912932032323425, 0.06248075506304599, 0.056212651221754284, 0.05034144599472293, 0.04487672136135561, 0.039821752809525525, 0.03517413623658342, 0.030926468305403826, 0.027067056647322542],
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
