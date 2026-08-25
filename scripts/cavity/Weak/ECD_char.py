""" """

from config.experiment_config import FOLDER, N, FREQ, I, Q, MAG, PHASE, RR

from qcore import Experiment, qua, Sweep
from ECD_functions import V_cat, Char_2D_singledisplacement, ECD


class ECD_coherent(Experiment):
    """Char_2D_singledisplacement"""

    ############################# DEFINE PRIMARY DATASETS ##############################
    # these Datasets form the "raw" experimental data and will be streamed by the OPX
    # they must be specified at experiment runtime

    primary_datasets = ["I", "Q"]

    ############################## DEFINE PRIMARY SWEEPS ###############################
    # these Sweeps are uniquely associated with the Experiment subclass
    # these Sweeps must be specified at experiment runtime

    primary_sweeps = ["ampx_x"]

    ############################ DEFINE THE PULSE SEQUENCE #############################
    # ensure that you import 'qua' from 'qcore' and not from 'qm' library
    # attributes accessed via 'self' must be defined in 'if __name__ == "__main__"' code

    def sequence(self):
        """QUA sequence that defines this Experiment subclass"""

        # bring qubit into superposition
        # qua.reset_phase(self.qubit)
        # qua.reset_frame(self.cavity, self.qubit)
        qua.reset_phase(self.cavity)
        qua.reset_frame(self.cavity)
        ###################### state prep  #####################
        self.cavity.play(self.cav_disp_state, ampx=1.75, phase=0.0)  # 0.1 , ampx=1, phase=0.0
        
        
        # self.qubit.play(self.qubit_pi2)
        # qua.align()
        # ECD(self.cavity, self.qubit, self.cav_disp, self.qubit_pi, ampx=amp_big,delay=self.delay,tomo_phase=0)

        # ECD(
        # self.cavity,
        # self.qubit,
        # self.cav_disp_state,
        # self.qubit_pi,
        # self.v_cat_amp_scale,
        # self.delay,
        # self.tomo_phase, )
        # qua.align()
        # self.qubit.play(self.qubit_pi)  # remove this if creating even cat
        # qua.align()
        # V_cat(
        #     self.cavity,
        #     self.qubit,
        #     self.cav_disp,
        #     self.qubit_pi,
        #     self.qubit_pi2,
        #     ampx=self.v_cat_amp_scale,
        #     delay=self.delay,
        #     # qubit_phase=0.25,
        # )
        qua.align()
        # self.qubit.play(self.qubit_pi)  # remove this if creating even cat
        # qua.align()

        ######################  charactristic function  1D measurement #####################

        Char_2D_singledisplacement(
            self.cavity,
            self.qubit,
            self.cav_disp,
            self.qubit_pi,
            self.qubit_pi2,
            self.ampx_x,
            self.ampx_y,
            delay=self.delay,
            measure_real=self.measure_real,
            tomo_phase=self.tomo_phase,  # -0.2,
        )
        qua.align()
        
        # self.qubit_gf2.play(self.qubit_gf2_drive)
        # qua.align(self.qubit_gf2, self.resonator)
        self.resonator.measure(self.readout_pulse, (self.I, self.Q), demod_type="dual")
        qua.wait(self.wait_time, self.resonator)


if __name__ == "__main__":
    """ """

    #################################### MODE MAP ######################################
    # key: name of the Mode as defined by the Experiment subclass
    # value: name of the Mode as defined by the user in modes.yml

    modes = {
        "cavity": "cavity",
        "qubit": "qubit",
        "resonator": "rr",
        # "qubit_gf2": "qubit_GF2",
    }

    ################################### PULSE MAP ######################################
    # key: name of the Pulse as defined by the Experiment subclass
    # value: name of the Pulse as defined by the user in modes.yml

    pulses = {
        "cav_disp_state": "cav_constant_40",
        "cav_disp": "cav_constant_40",
        "qubit_pi2": "qubit_gaussian_pi2_pulse_24",
        "qubit_pi": "qubit_gaussian_pi_pulse_24",
        # "qubit_gf2_drive": "qubitGF2_gaussian_pi_24",
        "readout_pulse": "rr_readout_pulse",
    }

    ############################## CONTROL PARAMETERS ##################################

    parameters = {
        "wait_time": 600_000,
        "ro_ampx": 1,
        "fetch_interval": 5,
        "tomo_phase": 0,
        "delay": 160,
        "correction_phase": 0,
        "measure_real": True,
        "v_cat_amp_scale": 1,
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this Experiment run
    N.num = 10000

    # set the qubit frequency sweep for this Experiment run
    CAV_AMPX = Sweep(name="ampx_x", start=-1.5, stop=1.5, step=0.1)
    CAV_AMPX2 = Sweep(name="ampx_y", start=-1.5, stop=1.5, step=0.1)

    sweeps = [N, CAV_AMPX, CAV_AMPX2]

    ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass
    # MAG.fitfn = "gaussian"

    PHASE.datafn_args = {"delay": 2.792e-7, "freq": RR.int_freq}
    # PHASE.plot = False
    Q.plot = False
    PHASE.plot = False
    MAG.plot = False

    datasets = [I, Q, MAG, PHASE]
    MAG.plot_args["plot_type"] = "image"
    I.plot_args["plot_type"] = "image"

    ######################## INITIALIZE AND RUN EXPERIMENT #############################

    expt = ECD_coherent(FOLDER, modes, pulses, sweeps, datasets, **parameters)
    # expt.run(simulate=True)
    expt.run()
