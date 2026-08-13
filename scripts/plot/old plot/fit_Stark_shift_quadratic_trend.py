# ===========================
# Single-file Lorentzian Fit
# + Linear Fit vs drive_amp²
# ===========================

import numpy as np
import matplotlib.pyplot as plt
import h5py
from lmfit import Model, Parameters
from pathlib import Path

# ---------------------------
# File path
# ---------------------------
file_path = Path(
    r"C:\Users\qcrew\Desktop\Juncheng\victoria\data\2026-07-21\13-50-13_snail_stark_shift_sweep.hdf5"
)

# ---------------------------
# Recursive dataset finder
# ---------------------------
def find_dataset(name, group):

    for key in group.keys():

        item = group[key]

        if isinstance(item, h5py.Dataset) and key == name:
            return item[()]

        elif isinstance(item, h5py.Group):

            result = find_dataset(name, item)

            if result is not None:
                return result

    return None

# ---------------------------
# Load data
# ---------------------------
with h5py.File(file_path, "r") as f:

    print("Keys:", list(f.keys()))

    I = find_dataset("I", f)
    Q = find_dataset("Q", f)

    qubit_freq = find_dataset("qubit_frequency", f)
    drive_amp = find_dataset("drive_amp", f)

# ---------------------------
# Convert arrays
# ---------------------------
I = np.array(I)

qubit_freq = np.array(qubit_freq)
drive_amp = np.array(drive_amp)

print("I shape:", I.shape)
print("qubit_frequency shape:", qubit_freq.shape)
print("drive_amp shape:", drive_amp.shape)

# ---------------------------
# Handle averaging dimensions
# ---------------------------
# Expected final shape:
# (N_drive_amp, N_freq)

while I.ndim > 2:
    I = np.mean(I, axis=0)

print("Reduced I shape:", I.shape)

if I.ndim != 2:
    raise ValueError(f"Unexpected I shape: {I.shape}")

# ---------------------------
# Lorentzian fit
# ---------------------------
def lorentzian_fit(y, x):

    def lorentzian(x, amp=1, x0=0, gamma=1, ofs=0):
        return amp * gamma**2 / ((x - x0)**2 + gamma**2) + ofs

    model = Model(lorentzian)

    params = Parameters()

    peak_idx = np.argmax(y)

    params.add("amp", value=np.max(y) - np.min(y))
    params.add("x0", value=x[peak_idx])
    params.add("gamma", value=(x[-1] - x[0]) / 20, min=1e-6)
    params.add("ofs", value=np.min(y))

    result = model.fit(y, params, x=x)

    return result

# ---------------------------
# Linear fit
# ---------------------------
def linear_fit(x, y):

    coeffs = np.polyfit(x, y, 1)

    slope = coeffs[0]
    intercept = coeffs[1]

    fit_y = slope * x + intercept

    return slope, intercept, fit_y

# ---------------------------
# Analyze all drive amplitudes
# ---------------------------
peak_positions = []
peak_widths = []

for i, amp in enumerate(drive_amp):

    y = I[i]

    try:

        fit = lorentzian_fit(y, qubit_freq)

        peak_freq = fit.params["x0"].value
        gamma = fit.params["gamma"].value

        peak_positions.append(peak_freq)
        peak_widths.append(gamma)

        print(
            f"drive_amp = {amp:.3f} | "
            f"peak = {peak_freq/1e6:.3f} MHz | "
            f"gamma = {gamma/1e6:.3f} MHz"
        )

    except Exception as e:

        print(f"Fit failed at drive_amp={amp}: {e}")

        peak_positions.append(np.nan)
        peak_widths.append(np.nan)

# ---------------------------
# Convert arrays
# ---------------------------
peak_positions = np.array(peak_positions)
peak_widths = np.array(peak_widths)

drive_amp_sq = drive_amp**2

# ---------------------------
# Remove NaNs
# ---------------------------
mask = np.isfinite(drive_amp_sq) & np.isfinite(peak_positions)

x = drive_amp_sq[mask]
y = peak_positions[mask]

# ---------------------------
# Linear fit
# ---------------------------
x_fit = x # leave out the last three points
y_fit = y # leave out the last three points

slope, intercept, fit_y = linear_fit(x_fit, y_fit)

print("\n===== Linear Fit =====")
print(f"Slope     = {slope:.6e} Hz / amp²")
print(f"Intercept = {intercept:.6e} Hz")

# ---------------------------
# Sort for plotting
# ---------------------------
sort_all = np.argsort(x)

x_sorted = x[sort_all]
y_sorted = y[sort_all]

sort_fit = np.argsort(x_fit)

x_fit_sorted = x_fit[sort_fit]
fit_sorted = fit_y[sort_fit]

# ---------------------------
# Plot peak positions
# ---------------------------
plt.figure(figsize=(7,5))

# all data points
plt.plot(
    x_sorted,
    y_sorted / 1e6,
    'o',
    label='Lorentzian peak'
)

# fit only on subset
plt.plot(
    x_fit_sorted,
    fit_sorted / 1e6,
    '-',
    label='Linear fit (excluding last 3 points)'
)

plt.xlabel("drive_amp²")
plt.ylabel("Peak frequency (MHz)")
plt.title("Peak position vs drive_amp²")

plt.grid()
plt.legend()

plt.tight_layout()
plt.show()

# ---------------------------
# Optional: plot linewidth
# ---------------------------
plt.figure(figsize=(7,5))

plt.plot(
    drive_amp_sq,
    peak_widths / 1e6,
    'o-'
)

plt.xlabel("drive_amp²")
plt.ylabel("Lorentzian width γ (MHz)")
plt.title("Linewidth vs drive_amp²")

plt.grid()
plt.tight_layout()
plt.show()