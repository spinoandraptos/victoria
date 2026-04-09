""" """
from config.experiment_config import FOLDER, N, FREQ, I, Q, MAG, PHASE, RRB, SINGLE_SHOT
from qcore import Experiment, qua, Sweep
from qm import qua as qm_qua
from qcore.libs.qua_macros import QuaVariable

class Wigner2D(Experiment):
    """Wigner_function"""

    ############################# DEFINE PRIMARY DATASETS ##############################
    # these Datasets form the "raw" experimental data and will be streamed by the OPX
    # they must be specified at experiment runtime
    primary_datasets = ["I", "Q", "single_shot"]

    ############################## DEFINE PRIMARY SWEEPS ###############################
    # these Sweeps are uniquely associated with the Experiment subclass
    # these Sweeps must be specified at experiment runtime
    # primary_sweeps = ["cavity_drive_I"]
    primary_sweeps = ["cavity_drive_Q"]

    ############################ DEFINE THE PULSE SEQUENCE #############################
    # ensure that you import 'qua' from 'qcore' and not from 'qm' library
    # attributes accessed via 'self' must be defined in 'if __name__ == "__main__"' code
    def sequence(self):
        #phase = qm_qua.declare(qm_qua.fixed)
        #qm_qua.assign(phase, 0.25)  # formerly with a 4*

        # factor = qm_qua.declare(qm_qua.fixed)
        # qm_qua.assign(factor, self.detuning * 1e-9)  # formerly with a 4*

        qua.reset_frame(self.cavityB)
      
        qua.reset_frame(self.qubitB)
       
        qua.align()

       
        new_phase = qm_qua.declare(qm_qua.fixed)
       
        qm_qua.assign(new_phase, 0.25)
        
        # qua.update_frequency(self.qubitB, self.qubitB.int_freq) 
      
        # self.cavityB.play(self.cavityB_grape_8)
        # self.qubitB.play(self.qubitB_grape_8)

       
  

        

        # WIGNER
        # self.cavityB.play(self.cavityB_pulse_short, ampx=(self.cavity_drive_I, -self.cavity_drive_Q, self.cavity_drive_Q, self.cavity_drive_I), phase=new_phase)  # displacement in I direction
        self.cavityB.play(self.cavityB_pulse_short, ampx=self.cavity_drive_Q, phase = new_phase)
        qua.align()

        # qua.update_frequency(self.qubitB, self.qubitB.int_freq)#-5e6) 
        self.qubitB.play(self.qubit_op)  # play pi/2 pulse around X
        qua.wait(self.time_delay, self.qubitB)  # conditional phase gate on even, odd Fock state
        self.qubitB.play(self.qubit_op, phase = self.wigner_phase)  # play pi/2 pulse around X
        qua.align()  # align measurement

        # qua.update_frequency(self.qubitB_EF, self.qubitB_EF.int_freq-10e6) 
        self.qubitB_EF.play(self.qubit_EF_pi)  # play pi/2 pulse around X
        qua.align()

        # Measure cavity state
        self.resonator.measure(self.readout_pulse, (self.I, self.Q), ampx=self.ro_ampx, demod_type= 'dual')  # measure transmitted signal
        if self.plot_single_shot:  # assign state to G or E
            qm_qua.assign(self.single_shot,qm_qua.Cast.to_fixed(self.I > self.readout_pulse.threshold),)
        qua.align()
        qua.wait(self.wait_time)


if __name__ == "__main__":
    """ """

    #################################### MODE MAP ######################################
    # key: name of the Mode as defined by the Experiment subclass
    # value: name of the Mode as defined by the user in modes.yml
    modes = {
       # "qC": "qC",
        # "cavityA": "cavA",
        "cavityB": "cavB",
        # "drive":"drive",
        "qubitB": "qB",
        # "qubitA": "qA",
        "resonator": "rrB",
        "qubitB_EF":"qB_EF",
    }

    ################################### PULSE MAP ######################################
    # key: name of the Pulse as defined by the Experiment subclass
    # value: name of the Pulse as defined by the user in modes.yml
    pulses = {
        # "cavityA_pulse": "cavA_ramp_pulse",
        # "cavityB_pulse": "cavB_gaussian_pulse",
        # "cavityB_pulse": "cavB_ramp_pulse",
        "cavityB_pulse_short": "cav_constant_40",
        "qubit_op": "qB_short_gaussian_pi2_pulse",
        # "qubit_pulse": "qB_gaussian_very_sel_pi_pulse",
        # "qubit_pulse_short": "qB_short_gaussian_pi_pulse",
        # "qubitB_SNAP_pulse": "qB_gaussian_very_sel_pi_pulse",
        "readout_pulse": "rr_readout_pulse",
        # "drive_pulse": "very_good_pulse_4000",
        "qubit_EF_pi": "qubit_gaussian_pi2_16",
        # "cavity_SNAP1_1p14":"cavB_ramp_pulse_SNAP1_1p14",
        # "cavity_SNAP1_m0p58": "cavB_ramp_pulse_SNAP1_m0p58",
        # "qubit_SNAP1_2pi": "qB_gaussian_very_sel_2pi_pulse",
        # "qubitA_grape": "qA_grape_fock1",
        # "cavityA_grape": "cavA_grape_fock1",
        # "qubitB_grape": "qB_grape_two_photon",
        # "cavityB_grape": "cavB_grape_two_photon",
        "qubitB_grape": "qB_grape_fock1",
        "cavityB_grape": "cavB_grape_fock1",

        "qubitB_grape_0": "qB_grape_fock2",
        "cavityB_grape_0": "cavB_grape_fock2",

        "qubitB_grape_1": "qB_grape_cat1.5",
        "cavityB_grape_1": "cavB_grape_cat1.5",

        "qubitB_grape_2": "qB_grape_cat2.0",
        "cavityB_grape_2": "cavB_grape_cat2.0",

        "qubitB_grape_3": "qB_grape_0plus1",
        "cavityB_grape_3": "cavB_grape_0plus1",

        "qubitB_grape_4": "qB_grape_cat_sqrt2",
        "cavityB_grape_4": "cavB_grape_cat_sqrt2",

        "qubitB_grape_5": "qB_grape_cat_sqrt3",
        "cavityB_grape_5": "cavB_grape_cat_sqrt3",

        "qubitB_grape_6": "qB_grape_fock2_old",
        "cavityB_grape_6": "cavB_grape_fock2_old",

        "qubitB_grape_7": "qB_grape_cat2_old",
        "cavityB_grape_7": "cavB_grape_cat2_old",

        "qubitB_grape_8": "qB_grape_cat1p5_old",
        "cavityB_grape_8": "cavB_grape_cat1p5_old",
    }

    ############################## CONTROL PARAMETERS ##################################
    parameters = {
        # "ramp_phase": -0.053/2,
        # "detuning": 111.8556e6, 
        # "phase": QuaVariable(value=0.0, dtype=qm_qua.fixed, tag="phase", buffer=True, stream=True),
        "wigner_phase":0.0,
        "wait_time": 6e6,
        "ro_ampx": 1,
        "time_delay": 212,#176, 
        # "test_wait": 120,#236,
        "plot_single_shot": True,
        "qubit_drive_ampx": 1.0,
        # "drive_length":3668, 
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this Experiment run
    N.num = 5000

    QD_AMPX_I = Sweep(name="cavity_drive_I", start=-1.8, stop=1.8, num = 101)
    QD_AMPX_Q = Sweep(name="cavity_drive_Q", start=-1.8, stop=1.8, num = 101)
    # QD_AMPX_I = Sweep(name="cavity_drive_I", start=-1.8, stop=1.8, step=0.2)
    # QD_AMPX_Q = Sweep(name="cavity_drive_Q", start=-1.8, stop=1.8, step=0.2)

    # DEL = Sweep(name="drive_time", start=1000, stop=15000, step=1000, dtype=int)

    # LENGTH = Sweep (name="drive_length", dtype=int, units = "ns")
    # LENGTH.start = 1000
    # LENGTH.stop = 11000
    # LENGTH.step = 500
         
    PARITY = Sweep(name="wigner_phase", start=0.0, stop=0.5, step=0.5)

    # sweeps = [N, LENGTH, QD_AMPX_Q, QD_AMPX_I]

    # sweeps = [N, QD_AMPX_Q, QD_AMPX_I]
    sweeps = [N, QD_AMPX_Q]
    # sweeps = [N, PARITY, QD_AMPX_I]

    ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass
    # I.fitfn = "gaussian"
    # SINGLE_SHOT.fitfn = "gaussian"
    PHASE.datafn_args = {"delay": 2.792e-7, "freq": RRB.int_freq}
    Q.plot, I.plot = False, True
    # I.plot, Q.plot, MAG.plot = False, False, False
    # SINGLE_SHOT.plot_args["plot_type"] = "image"
    # I.plot_args["plot_type"] = "image"
    # SINGLE_SHOT.plot = False
    datasets = [I, Q, SINGLE_SHOT]

    ######################## INITIALIZE AND RUN EXPERIMENT #############################
    expt = Wigner2D(FOLDER, modes, pulses, sweeps, datasets, **parameters)
    # expt.run()
    expt.run(simulate=False)
