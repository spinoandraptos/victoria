# Auto-generated standalone QUA execution script
import time
import numpy as np
import matplotlib.pyplot as plt
from qm import QuantumMachinesManager
from qm.qua import *


# Single QUA script generated at 2026-08-07 15:49:25.345968
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
            play('qubit_pi_pulse'*amp(1.0), 'qubit')
            align('qubit', 'qubit_EF')
            play('qubit_ef_drive'*amp(v2), 'qubit_EF')
            align('qubit_EF', 'qubit')
            play('qubit_pi_pulse'*amp(1.0), 'qubit')
            align('qubit', 'rr')
            measure('readout_pulse'*amp(1), 'rr', dual_demod.full("cos", "sin", v3), dual_demod.full("minus_sin", "cos", v4))
            wait(37500, 'rr')
            r3 = declare_output_stream()
            save(v3, r3)
            r4 = declare_output_stream()
            save(v4, r4)
    with stream_processing():
        r2.buffer(51).save("qubit_ef_pulse_amplitude")
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
                        "2": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 8,
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 1185200000.0,
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
                                    "frequency": 5698000000.0,
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
        "qubit": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {'qubit_pi_pulse': 'qubit.qubit_gaussian_pi_24'},
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
            "intermediate_frequency": 53800000.0,
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
            "intermediate_frequency": -40700000.0,
        },
        "qubit_EF": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {'qubit_ef_drive': 'qubit_EF.qubitEF_gaussian_pi_24'},
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
            "intermediate_frequency": -146000000.0,
        },
    },
    "pulses": {
        "qubit.qubit_gaussian_pi_24": {
            "length": 24,
            "waveforms": {'Q': 'qubit.qubit_gaussian_pi_24.waveform.Q', 'I': 'qubit.qubit_gaussian_pi_24.waveform.I'},
            "integration_weights": {},
            "operation": "control",
        },
        "rr.rr_readout_pulse": {
            "length": 640,
            "waveforms": {'Q': 'rr.rr_readout_pulse.waveform.Q', 'I': 'rr.rr_readout_pulse.waveform.I'},
            "integration_weights": {'minus_sin': 'rr.rr_readout_pulse.minus_sin', 'sin': 'rr.rr_readout_pulse.sin', 'cos': 'rr.rr_readout_pulse.cos'},
            "operation": "measurement",
        },
        "qubit_EF.qubitEF_gaussian_pi_24": {
            "length": 24,
            "waveforms": {'Q': 'qubit_EF.qubitEF_gaussian_pi_24.waveform.Q', 'I': 'qubit_EF.qubitEF_gaussian_pi_24.waveform.I'},
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "rr.rr_readout_pulse.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit_EF.qubitEF_gaussian_pi_24.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.012] * 320 + [0.0] * 320,
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "qubit_EF.qubitEF_gaussian_pi_24.waveform.I": {
            "type": "arbitrary",
            "samples": [0.01164675415117149, 0.016244115841979715, 0.021981214628845447, 0.0288583658478667, 0.0367583680525731, 0.04542606815464873, 0.05446512610347285, 0.06335724990602273, 0.07150535407545726, 0.07829702200613976, 0.08317951158637851] + [0.08573377104825886] * 2 + [0.08317951158637851, 0.07829702200613978, 0.07150535407545726, 0.06335724990602275, 0.05446512610347285, 0.045426068154648745, 0.036758368052573105, 0.0288583658478667, 0.021981214628845454, 0.016244115841979725, 0.01164675415117149],
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "qubit.qubit_gaussian_pi_24.waveform.Q": {
            "type": "arbitrary",
            "samples": [-0.0013070124363882597, -0.0016644177876905587, -0.0020377563895538574, -0.0023936884927853734, -0.0026902612538217885, -0.002881346421830137, -0.0029231976068548973, -0.002782183708380586, -0.002442213217308149, -0.001910126915785869, -0.0012175438083247025, -0.00041831063168216277, 0.00041831063168216136, 0.0012175438083247025, 0.0019101269157858678, 0.002442213217308149, 0.002782183708380586, 0.0029231976068548973, 0.0028813464218301384, 0.002690261253821789, 0.0023936884927853734, 0.002037756389553858, 0.0016644177876905595, 0.0013070124363882597],
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "qubit.qubit_gaussian_pi_24.waveform.I": {
            "type": "arbitrary",
            "samples": [0.03963715576475937, 0.05528326102981932, 0.07480820980964187, 0.09821307528099997, 0.1250989882027897, 0.1545975913851738, 0.18536002899086415, 0.21562240867763224, 0.2433526818472497, 0.26646662382428593, 0.28308309889534866] + [0.2917759569088389] * 2 + [0.28308309889534866, 0.26646662382428593, 0.2433526818472497, 0.21562240867763227, 0.18536002899086415, 0.15459759138517387, 0.12509898820278975, 0.09821307528099997, 0.0748082098096419, 0.055283261029819356, 0.03963715576475937],
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
            "cosine": [(0.024444580078125, 64), (0.1009521484375, 64), (0.054412841796875, 64), (0.0169677734375, 64), (-0.171600341796875, 64), (-0.47509765625, 64), (-0.644134521484375, 64), (-0.754241943359375, 64), (-0.6962890625, 64), (-0.684906005859375, 64)],
            "sine": [(0.029754638671875, 64), (0.150054931640625, 64), (0.427459716796875, 64), (0.669647216796875, 64), (0.863616943359375, 64), (0.82220458984375, 64), (0.764923095703125, 64), (0.5853271484375, 64), (0.434600830078125, 64), (0.337188720703125, 64)],
        },
        "rr.rr_readout_pulse.sin": {
            "cosine": [(-0.029754638671875, 64), (-0.150054931640625, 64), (-0.427459716796875, 64), (-0.669647216796875, 64), (-0.863616943359375, 64), (-0.82220458984375, 64), (-0.764923095703125, 64), (-0.5853271484375, 64), (-0.434600830078125, 64), (-0.337188720703125, 64)],
            "sine": [(0.024444580078125, 64), (0.1009521484375, 64), (0.054412841796875, 64), (0.0169677734375, 64), (-0.171600341796875, 64), (-0.47509765625, 64), (-0.644134521484375, 64), (-0.754241943359375, 64), (-0.6962890625, 64), (-0.684906005859375, 64)],
        },
        "rr.rr_readout_pulse.minus_sin": {
            "cosine": [(0.029754638671875, 64), (0.150054931640625, 64), (0.427459716796875, 64), (0.669647216796875, 64), (0.863616943359375, 64), (0.82220458984375, 64), (0.764923095703125, 64), (0.5853271484375, 64), (0.434600830078125, 64), (0.337188720703125, 64)],
            "sine": [(-0.024444580078125, 64), (-0.1009521484375, 64), (-0.054412841796875, 64), (-0.0169677734375, 64), (0.171600341796875, 64), (0.47509765625, 64), (0.644134521484375, 64), (0.754241943359375, 64), (0.6962890625, 64), (0.684906005859375, 64)],
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
                                    "frequency": 1185200000.0,
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
                                    "frequency": 5698000000.0,
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
        "qubit": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {'qubit_pi_pulse': 'qubit.qubit_gaussian_pi_24'},
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
            "intermediate_frequency": 53800000.0,
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
            "intermediate_frequency": -40700000.0,
        },
        "qubit_EF": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {'qubit_ef_drive': 'qubit_EF.qubitEF_gaussian_pi_24'},
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
            "intermediate_frequency": -146000000.0,
        },
    },
    "pulses": {
        "qubit.qubit_gaussian_pi_24": {
            "length": 24,
            "waveforms": {'Q': 'qubit.qubit_gaussian_pi_24.waveform.Q', 'I': 'qubit.qubit_gaussian_pi_24.waveform.I'},
            "integration_weights": {},
            "operation": "control",
        },
        "rr.rr_readout_pulse": {
            "length": 640,
            "waveforms": {'Q': 'rr.rr_readout_pulse.waveform.Q', 'I': 'rr.rr_readout_pulse.waveform.I'},
            "integration_weights": {'minus_sin': 'rr.rr_readout_pulse.minus_sin', 'sin': 'rr.rr_readout_pulse.sin', 'cos': 'rr.rr_readout_pulse.cos'},
            "operation": "measurement",
        },
        "qubit_EF.qubitEF_gaussian_pi_24": {
            "length": 24,
            "waveforms": {'Q': 'qubit_EF.qubitEF_gaussian_pi_24.waveform.Q', 'I': 'qubit_EF.qubitEF_gaussian_pi_24.waveform.I'},
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "rr.rr_readout_pulse.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit_EF.qubitEF_gaussian_pi_24.waveform.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "rr.rr_readout_pulse.waveform.I": {
            "type": "arbitrary",
            "samples": [0.012] * 320 + [0.0] * 320,
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "qubit_EF.qubitEF_gaussian_pi_24.waveform.I": {
            "type": "arbitrary",
            "samples": [0.01164675415117149, 0.016244115841979715, 0.021981214628845447, 0.0288583658478667, 0.0367583680525731, 0.04542606815464873, 0.05446512610347285, 0.06335724990602273, 0.07150535407545726, 0.07829702200613976, 0.08317951158637851] + [0.08573377104825886] * 2 + [0.08317951158637851, 0.07829702200613978, 0.07150535407545726, 0.06335724990602275, 0.05446512610347285, 0.045426068154648745, 0.036758368052573105, 0.0288583658478667, 0.021981214628845454, 0.016244115841979725, 0.01164675415117149],
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "qubit.qubit_gaussian_pi_24.waveform.Q": {
            "type": "arbitrary",
            "samples": [-0.0013070124363882597, -0.0016644177876905587, -0.0020377563895538574, -0.0023936884927853734, -0.0026902612538217885, -0.002881346421830137, -0.0029231976068548973, -0.002782183708380586, -0.002442213217308149, -0.001910126915785869, -0.0012175438083247025, -0.00041831063168216277, 0.00041831063168216136, 0.0012175438083247025, 0.0019101269157858678, 0.002442213217308149, 0.002782183708380586, 0.0029231976068548973, 0.0028813464218301384, 0.002690261253821789, 0.0023936884927853734, 0.002037756389553858, 0.0016644177876905595, 0.0013070124363882597],
            "is_overridable": False,
            "max_allowed_error": 1.0,
        },
        "qubit.qubit_gaussian_pi_24.waveform.I": {
            "type": "arbitrary",
            "samples": [0.03963715576475937, 0.05528326102981932, 0.07480820980964187, 0.09821307528099997, 0.1250989882027897, 0.1545975913851738, 0.18536002899086415, 0.21562240867763224, 0.2433526818472497, 0.26646662382428593, 0.28308309889534866] + [0.2917759569088389] * 2 + [0.28308309889534866, 0.26646662382428593, 0.2433526818472497, 0.21562240867763227, 0.18536002899086415, 0.15459759138517387, 0.12509898820278975, 0.09821307528099997, 0.0748082098096419, 0.055283261029819356, 0.03963715576475937],
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
            "cosine": [(0.024444580078125, 64), (0.1009521484375, 64), (0.054412841796875, 64), (0.0169677734375, 64), (-0.171600341796875, 64), (-0.47509765625, 64), (-0.644134521484375, 64), (-0.754241943359375, 64), (-0.6962890625, 64), (-0.684906005859375, 64)],
            "sine": [(0.029754638671875, 64), (0.150054931640625, 64), (0.427459716796875, 64), (0.669647216796875, 64), (0.863616943359375, 64), (0.82220458984375, 64), (0.764923095703125, 64), (0.5853271484375, 64), (0.434600830078125, 64), (0.337188720703125, 64)],
        },
        "rr.rr_readout_pulse.sin": {
            "cosine": [(-0.029754638671875, 64), (-0.150054931640625, 64), (-0.427459716796875, 64), (-0.669647216796875, 64), (-0.863616943359375, 64), (-0.82220458984375, 64), (-0.764923095703125, 64), (-0.5853271484375, 64), (-0.434600830078125, 64), (-0.337188720703125, 64)],
            "sine": [(0.024444580078125, 64), (0.1009521484375, 64), (0.054412841796875, 64), (0.0169677734375, 64), (-0.171600341796875, 64), (-0.47509765625, 64), (-0.644134521484375, 64), (-0.754241943359375, 64), (-0.6962890625, 64), (-0.684906005859375, 64)],
        },
        "rr.rr_readout_pulse.minus_sin": {
            "cosine": [(0.029754638671875, 64), (0.150054931640625, 64), (0.427459716796875, 64), (0.669647216796875, 64), (0.863616943359375, 64), (0.82220458984375, 64), (0.764923095703125, 64), (0.5853271484375, 64), (0.434600830078125, 64), (0.337188720703125, 64)],
            "sine": [(-0.024444580078125, 64), (-0.1009521484375, 64), (-0.054412841796875, 64), (-0.0169677734375, 64), (0.171600341796875, 64), (0.47509765625, 64), (0.644134521484375, 64), (0.754241943359375, 64), (0.6962890625, 64), (0.684906005859375, 64)],
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
