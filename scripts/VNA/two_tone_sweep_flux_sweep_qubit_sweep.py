import pyvisa
import numpy as np
import time
import pickle
from datetime import datetime

def dc_ramp(yoko, stop, start=None, step=20e-6) -> None:
    """ """
    if start is None:  # start from the current level set right now
        start = float(yoko.query(":source:level?"))

    if start > stop:  # ramp down
        points = np.arange(stop, start, step)[::-1]  # include endpoint
    else:  # ramp up
        points = np.arange(start, stop, step)
    points = np.concatenate([points, [stop]])  # ensures that last point is included
    for point in points:
        yoko.write(f":source:level:auto {point}")
        time.sleep(0.1)


def dc_output(yoko, value: bool) -> None:
    """ """
    yoko.write(f"output {int(bool(value))}")
    time.sleep(0.1)


def vna_single_sweep(vna, center_freq, freq_span, power, sweep_reps):
    vna.write(f"SENS1:FREQ:CENTER {center_freq}")
    vna.write(f"SENS1:FREQ:SPAN {freq_span}")
    start_freq = float(vna.query("SENS1:FREQ:START?")[:-1])
    # Query the stop frequency
    stop_freq = float(vna.query("SENS1:FREQ:STOP?")[:-1])
    # # Query the number of points
    num_points = int(vna.query("SENS1:SWE:POIN?")[:-1])
    freq = np.linspace(start_freq, stop_freq, num_points)
    vna.write(f"SOUR:POW {power:.1f}")

    real_list = []
    imag_list = []
    for i2 in range(sweep_reps):
        print(f"({i2}/{sweep_reps})")
        time.sleep(5)
        vna.write("CALC1:DATA? SDATA")
        raw_data = vna.read()
        float_list = [float(x) for x in raw_data.split(",")]
        # Separate the values into two lists based on index
        column1 = np.array(float_list[0::2])  # Values at even indices (0, 2, 4, ...)
        column2 = np.array(float_list[1::2])  # Values at odd indices (1, 3, 5, ...)
        real_list.append(column1)
        imag_list.append(column2)
    return freq, real_list, imag_list


rm = pyvisa.ResourceManager()

vna = rm.open_resource("TCPIP0::192.168.111.169::inst0::INSTR")
print(vna.query("*IDN?"))

yoko = rm.open_resource("USB0::0x0B21::0x0039::90X823743::INSTR")
print(yoko.query("*IDN?"))
vna.write(f"SENS1:SWE:POIN {5001}")
vna.write(f"SENS1:BAND:RES 1000Hz")

pump = rm.open_resource("TCPIP0::192.168.111.122::inst0::INSTR")
"""Sets power in dBm"""
pump.write(f":POW {0}")
# Synchronize (wait until all previous commands have been executed completely)
pump.query("*OPC?")

dc_bias_list = np.arange(start=-1, stop=1, step=0.1) * 1e-6  # in amps
dc_bias_list = np.arange(start=11, stop=11.05, step=0.1) * 1e-6  # in amps
pump_power_list = np.arange(start=-10, stop=5, step=0.1)  # in amps
# pump_power_list = np.arange(start=0, stop=0.05, step=0.1)  # in amps
center_freq = 6e9
freq_span = 10e6
reps = 1
power = -40

print(dc_bias_list)
# # set yoko to 0 at the start
dc_ramp(yoko, 0)
dc_output(yoko, True)
pump.write(f"OUTP ON")
pump.query("*OPC?")

for dc_bias in dc_bias_list:
    for pump_power in pump_power_list:
        print(f"{datetime.now()} Setting DC bias: {dc_bias * 1e6} uA")
        dc_ramp(yoko, dc_bias)
        pump.write(f":POW {pump_power}")
        pump.query("*OPC?")
        print(f"{datetime.now()} Running VNA sweep")
        freq, real_list, imag_list = vna_single_sweep(
            vna,
            center_freq=center_freq,
            freq_span=freq_span,
            power=power,
            sweep_reps=reps,
        )
        real = np.average(real_list, axis=1)
        imag = np.average(imag_list, axis=1)
    with open(
        f"C:\\Users\\qcrew\\Documents\\eunice\\data\\2026-02-04\\snaillm_s21_two_tone_sweep_freq_dc_bias_{dc_bias}"
        + ".pkl",
        "wb",
    ) as f:
        pickle.dump(
            {
                "freq": freq,
                "real": real_list,
                "imag": imag_list,
            },
            f,
        )

dc_ramp(yoko, 0)
dc_output(yoko, False)
pump.write(f"OUTP OFF")
pump.query("*OPC?")
