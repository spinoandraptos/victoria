# Auto-generated standalone QUA execution script
import time
import numpy as np
import matplotlib.pyplot as plt
from qm import QuantumMachinesManager
from qm.qua import *


# Single QUA script generated at 2026-08-26 15:54:14.606096
# QUA library version: 1.3.1


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
        r1 = declare_output_stream()
        save(v1, r1)
        with for_each_((v2),(a1)):
            r2 = declare_output_stream()
            save(v2, r2)
            with for_(v3,-1.4,(v3<1.428),(v3+0.05600000000000005)):
                r3 = declare_output_stream()
                save(v3, r3)
                play('qubit_pi_pulse'*amp(v2), 'qubit')
                align('qubit', 'qubit_EF')
                play('qubitEF_pi_pulse'*amp(v3), 'qubit_EF')
                align('qubit_EF', 'qubit')
                play('qubit_pi_pulse'*amp(1.0), 'qubit')
                align('qubit', 'rr')
                measure('readout_pulse'*amp(1), 'rr', dual_demod.full("cos", "sin", v4), dual_demod.full("minus_sin", "cos", v5))
                wait(50000, 'rr')
                r4 = declare_output_stream()
                save(v4, r4)
                r5 = declare_output_stream()
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
                            "full_scale_power_dbm": 13,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 6643800000.0,
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
        "qubit": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {'qubit_pi_pulse': 'qubit.qubit_gaussian_pi_pulse_24'},
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
            "time_of_flight": 396,
            "intermediate_frequency": -50000000.0,
        },
        "qubit_EF": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {'qubitEF_pi_pulse': 'qubit_EF.qubitEF_gaussian_pi_pulse_24'},
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
            "intermediate_frequency": -108000000.0,
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
        "qubit_EF.qubitEF_gaussian_pi_pulse_24": {
            "length": 24,
            "waveforms": {'Q': 'qubit_EF.qubitEF_gaussian_pi_pulse_24.waveform.Q', 'I': 'qubit_EF.qubitEF_gaussian_pi_pulse_24.waveform.I'},
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "qubit.qubit_gaussian_pi_pulse_24.waveform.I": {
            "type": "arbitrary",
            "samples": [0.012344534086442333, 0.017217332753200303, 0.02329815240582664, 0.03058732727282485, 0.038960634138683135, 0.048147633192009064, 0.057728238870661884, 0.0671531072895081, 0.07578938039649646, 0.08298795050331668, 0.08816295963183805] + [0.09087024979899834] * 2 + [0.08816295963183805, 0.0829879505033167, 0.07578938039649646, 0.06715310728950812, 0.057728238870661884, 0.048147633192009084, 0.03896063413868314, 0.03058732727282485, 0.02329815240582665, 0.017217332753200313, 0.012344534086442333],
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
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
        "qubit_EF.qubitEF_gaussian_pi_pulse_24.waveform.I": {
            "type": "arbitrary",
            "samples": [0.008229689390961555, 0.01147822183546687, 0.015532101603884426, 0.020391551515216568, 0.025973756092455426, 0.032098422128006045, 0.03848549258044126, 0.044768738193005406, 0.05052625359766431, 0.05532530033554446, 0.05877530642122537] + [0.06058016653266556] * 2 + [0.05877530642122537, 0.05532530033554447, 0.05052625359766431, 0.04476873819300541, 0.03848549258044126, 0.03209842212800606, 0.02597375609245543, 0.020391551515216568, 0.015532101603884433, 0.011478221835466876, 0.008229689390961555],
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "qubit.qubit_gaussian_pi_pulse_24.waveform.Q": {
            "type": "arbitrary",
            "samples": [0.000407053918504005, 0.0005183636847246871, 0.0006346356776960828, 0.0007454866178310714, 0.0008378507768401625, 0.0008973620440938497, 0.0009103961120063479, 0.0008664789629881553, 0.0007605990824958342, 0.0005948869530722942, 0.00037918994825970816, 0.0001302780119282111, -0.00013027801192821067, -0.00037918994825970816, -0.0005948869530722939, -0.0007605990824958342, -0.0008664789629881553, -0.0009103961120063479, -0.0008973620440938498, -0.0008378507768401625, -0.0007454866178310714, -0.0006346356776960828, -0.0005183636847246874, -0.000407053918504005],
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "qubit_EF.qubitEF_gaussian_pi_pulse_24.waveform.Q": {
            "type": "arbitrary",
            "samples": [0.00027136927900266996, 0.00034557578981645815, 0.00042309045179738855, 0.0004969910785540476, 0.0005585671845601085, 0.0005982413627292332, 0.0006069307413375654, 0.0005776526419921036, 0.0005070660549972228, 0.0003965913020481962, 0.0002527932988398055, 8.685200795214074e-05, -8.685200795214045e-05, -0.0002527932988398055, -0.000396591302048196, -0.0005070660549972228, -0.0005776526419921036, -0.0006069307413375654, -0.0005982413627292333, -0.0005585671845601083, -0.0004969910785540476, -0.0004230904517973886, -0.00034557578981645826, -0.00027136927900266996],
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
                            "full_scale_power_dbm": 13,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 6643800000.0,
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
        "qubit": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {'qubit_pi_pulse': 'qubit.qubit_gaussian_pi_pulse_24'},
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
            "time_of_flight": 396,
            "intermediate_frequency": -50000000.0,
        },
        "qubit_EF": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {'qubitEF_pi_pulse': 'qubit_EF.qubitEF_gaussian_pi_pulse_24'},
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
            "intermediate_frequency": -108000000.0,
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
        "qubit_EF.qubitEF_gaussian_pi_pulse_24": {
            "length": 24,
            "waveforms": {'Q': 'qubit_EF.qubitEF_gaussian_pi_pulse_24.waveform.Q', 'I': 'qubit_EF.qubitEF_gaussian_pi_pulse_24.waveform.I'},
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "qubit.qubit_gaussian_pi_pulse_24.waveform.I": {
            "type": "arbitrary",
            "samples": [0.012344534086442333, 0.017217332753200303, 0.02329815240582664, 0.03058732727282485, 0.038960634138683135, 0.048147633192009064, 0.057728238870661884, 0.0671531072895081, 0.07578938039649646, 0.08298795050331668, 0.08816295963183805] + [0.09087024979899834] * 2 + [0.08816295963183805, 0.0829879505033167, 0.07578938039649646, 0.06715310728950812, 0.057728238870661884, 0.048147633192009084, 0.03896063413868314, 0.03058732727282485, 0.02329815240582665, 0.017217332753200313, 0.012344534086442333],
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
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
        "qubit_EF.qubitEF_gaussian_pi_pulse_24.waveform.I": {
            "type": "arbitrary",
            "samples": [0.008229689390961555, 0.01147822183546687, 0.015532101603884426, 0.020391551515216568, 0.025973756092455426, 0.032098422128006045, 0.03848549258044126, 0.044768738193005406, 0.05052625359766431, 0.05532530033554446, 0.05877530642122537] + [0.06058016653266556] * 2 + [0.05877530642122537, 0.05532530033554447, 0.05052625359766431, 0.04476873819300541, 0.03848549258044126, 0.03209842212800606, 0.02597375609245543, 0.020391551515216568, 0.015532101603884433, 0.011478221835466876, 0.008229689390961555],
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "qubit.qubit_gaussian_pi_pulse_24.waveform.Q": {
            "type": "arbitrary",
            "samples": [0.000407053918504005, 0.0005183636847246871, 0.0006346356776960828, 0.0007454866178310714, 0.0008378507768401625, 0.0008973620440938497, 0.0009103961120063479, 0.0008664789629881553, 0.0007605990824958342, 0.0005948869530722942, 0.00037918994825970816, 0.0001302780119282111, -0.00013027801192821067, -0.00037918994825970816, -0.0005948869530722939, -0.0007605990824958342, -0.0008664789629881553, -0.0009103961120063479, -0.0008973620440938498, -0.0008378507768401625, -0.0007454866178310714, -0.0006346356776960828, -0.0005183636847246874, -0.000407053918504005],
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "qubit_EF.qubitEF_gaussian_pi_pulse_24.waveform.Q": {
            "type": "arbitrary",
            "samples": [0.00027136927900266996, 0.00034557578981645815, 0.00042309045179738855, 0.0004969910785540476, 0.0005585671845601085, 0.0005982413627292332, 0.0006069307413375654, 0.0005776526419921036, 0.0005070660549972228, 0.0003965913020481962, 0.0002527932988398055, 8.685200795214074e-05, -8.685200795214045e-05, -0.0002527932988398055, -0.000396591302048196, -0.0005070660549972228, -0.0005776526419921036, -0.0006069307413375654, -0.0005982413627292333, -0.0005585671845601083, -0.0004969910785540476, -0.0004230904517973886, -0.00034557578981645826, -0.00027136927900266996],
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
