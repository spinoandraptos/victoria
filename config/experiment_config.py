""" """

from qcore import Dataset, Sweep, Stage
from pathlib import Path

################################# PROJECT FOLDER PATH ##################################
# to obtain Resources (Instruments, Modes, Pulses) from and save data file to
# MODES_CONFIG = Path(__file__).resolve().parent / "config/modes.yml"

FOLDER = "C:/Users/qcrew/Documents/eunice/"
MODES_CONFIG = FOLDER + "config/modes.yml"


######################## CONFIGURE STAGED RESOURCES IF NEEDED ##########################
print("YAY")
with Stage(MODES_CONFIG, remote=True) as stage:
    # QUBIT, RR, CAVITY, SNAIL, CAVITY_M, QUBIT_EF= stage.get("qubit", "rr", "cavity", "snail", "cavity_m", "qubit_ef")
    QUBIT, RR, CAVITY, SNAIL, CAVITY_M= stage.get("qubit", "rr", "cavity", "snail", "cavity_m")
(READOUT_PULSE,) = RR.get_operations("rr_readout_pulse")

################## DEFINE REUSABLE SWEEP (INDEPENDENT) VARIABLES #######################


# averaging sweep "N"
N = Sweep(
    name="N",
    num=1000,
    dtype=int,
    save=False,
)

# linspace Frequency sweep
FREQ = Sweep(
    name="freq",
    dtype=int,
    units="Hz",
)

LENGTH = Sweep(
    name="len",
    dtype=int,
    units="ns",
)

# DC_CURR = Sweep(
#     name="curr",
#     dtype=int,
#     units="mA",
# )

################## DEFINE REUSABLE DATASET (DEPENDENT) VARIABLES #######################

I = Dataset(
    name="I",
    save=True,
    plot=True,
    # fitfn="exp_decay",
)

Q = Dataset(
    name="Q",
    save=True,
    plot=True,
)

ADC = Dataset(
    name="adc",
    stream=RR.ports["out1"][1],  # out for old
    save=False,
    plot=True,
    plot_args={
        "plot_type": "line",
        "plot_err": False,
        "xlabel": "Time (ns)",
    },
)

ADC_FFT = Dataset(
    name="adc_fft",
    save=True,
    plot=True,
    datafn="fft",
    datafn_args={"length": READOUT_PULSE.total_length},
    plot_args={"plot_type": "line", "plot_err": False},
)

MAG = Dataset(
    name="Magnitude",
    save=True,
    plot=True,
    datafn="mag",
    # fitfn="exp_decay_sine",
)

PHASE = Dataset(
    name="Phase",
    save=False,
    plot=True,
    datafn="phase",
    datafn_args={"delay": 2.792e-7, "freq": RR.int_freq, "unwrap": True},
    # fitfn="atan",
)

SINGLE_SHOT = Dataset(
    name="single_shot",
    save=True,
    plot=True,
    # fitfn="exp_decay",
)
