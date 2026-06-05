""" """

from config.experiment_config import FOLDER, N, FREQ, I, Q, MAG, PHASE, RR

from qcore import Experiment, qua, Sweep


class ECD_CAL_1D_gf2_real_imag_fock1(Experiment):
    """Char_1D_singledisplacement"""

    ############################# DEFINE PRIMARY DATASETS ##############################
    # these Datasets form the "raw" experimental data and will be streamed by the OPX
    # they must be specified at experiment runtime

    primary_datasets = ["I", "Q"]

    ############################## DEFINE PRIMARY SWEEPS ###############################
    # these Sweeps are uniquely associated with the Experiment subclass
    # these Sweeps must be specified at experiment runtime

    primary_sweeps = ["cavity_amp"]

    ############################ DEFINE THE PULSE SEQUENCE #############################
    # ensure that you import 'qua' from 'qcore' and not from 'qm' library
    # attributes accessed via 'self' must be defined in 'if __name__ == "__main__"' code

    def sequence(self):
        """QUA sequence that defines this Experiment subclass"""

        # bring qubit into superposition
        qua.reset_phase(self.cavity)
        qua.reset_frame(self.cavity)
        ###################### fock 1  #####################
        
        self.qubit_gf2.play(self.qubit_gf2_drive)
        qua.align()
       
        
        self.drive.play(self.stark_drive) # fixed freq #, ampx=2.0 max , duration=self.length_drive
        qua.align()  # wait for qubit pulse to end
        ######################  charactristic function  1D measurement #####################

        self.qubit.play(self.qubit_pi2)

        # start ECD gate
        qua.align()  # wait for qubit pulse to end
        # First positive displacement
        self.cavity.play(self.cav_disp, ampx=self.cavity_amp, phase=self.tomo_phase)

        qua.wait(int(self.delay), self.cavity)
        # First negative displacement
        self.cavity.play(self.cav_disp, ampx=-self.cavity_amp, phase=self.tomo_phase)

        qua.align()
        self.qubit.play(self.qubit_pi, phase=0.0)  # play pi to flip qubit around X
        qua.align()  # wait for qubit pulse to end

        # Second negative displacement
        self.cavity.play(self.cav_disp, ampx=-self.cavity_amp, phase=self.tomo_phase)

        qua.wait(int(self.delay), self.cavity)
        # Second positive displacement
        self.cavity.play(self.cav_disp, ampx=self.cavity_amp, phase=self.tomo_phase)
        qua.align()

        self.qubit.play(
            self.qubit_pi2,
            phase=self.q_phase,#self.correction_phase + self.q_phase,
        )  # play pi/2 pulse around X or SY, to measure either the real or imaginary part of the characteristic function
        # qubit.play(qubit_pi2_pulse, phase=measure_real)  # 0 else 0.25  # play
        qua.align(self.qubit_gf2, self.qubit)
        self.qubit_gf2.play(self.qubit_gf2_drive)
        qua.align(self.qubit_gf2, self.resonator)
        # qua.align()
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
        "qubit_gf2": "qubit_GF2",
        "drive": "drive"
    }

    ################################### PULSE MAP ######################################
    # key: name of the Pulse as defined by the Experiment subclass
    # value: name of the Pulse as defined by the user in modes.yml

    pulses = {
        "stark_drive": "drive_constant_fock1",
        "cav_disp": "cav_constant_180",  # "cav_gaussian_40",
        "qubit_pi2": "qubit_gaussian_pi2_24",
        "qubit_pi": "qubit_gaussian_pi_24",
        "readout_pulse": "rr_readout_pulse",
        "qubit_gf2_drive": "qubitGF2_gaussian_pi_24",
    }

    ############################## CONTROL PARAMETERS ##################################

    parameters = {
        "wait_time": 1_200_000,
        "ro_ampx": 1,
        "fetch_interval": 5,
        "tomo_phase": 0,
        "delay": 160, #45,
        "correction_phase": 0,
        "measure_real": True,
    }

    ######################## SWEEP (INDEPENDENT) VARIABLES #############################
    # must include an outermost averaging Sweep named "N"
    # must include all primary sweeps defined by the Experiment subclass

    # set number of repetitions for this Experiment run
    N.num = 10000

    # set the qubit frequency sweep for this Experiment run
    CAV_AMPX = Sweep(name="cavity_amp", start=-1.95, stop=1.95, step=0.1)
    # Q_phase = Sweep(name="q_phase", start=-1.95, stop=1.95, step=0.1)
    Q_phase = Sweep(
        name="q_phase",
        points=[0, 0.25]#0.25,0.5,0.75] #[0.01,0.05, 0.08,0.1, 0.2, 0.3, 0.4]
        # points=[0.2, 0.4, 0.6, 0.8, 1.0]
        # points=[0.01, 0.02, 0.03, 0.04, 0.05, 0.1]#0.25,0.5,0.75]
    ) 

    sweeps = [N, Q_phase, CAV_AMPX]

    ######################## DATASET (DEPENDENT) VARIABLES #############################
    # must include all primary datasets defined by the Experiment subclass
    # MAG.fitfn = "gaussian"

    PHASE.datafn_args = {"delay": 2.792e-7, "freq": RR.int_freq}
    # PHASE.plot = False

    I.fitfn = "gaussian"
    Q.fitfn = "gaussian"
    MAG.fitfn = "gaussian"
    PHASE.fitfn = "gaussian"
    datasets = [I, Q, MAG, PHASE]

    ######################## INITIALIZE AND RUN EXPERIMENT #############################

    expt = ECD_CAL_1D_gf2_real_imag_fock1(FOLDER, modes, pulses, sweeps, datasets, **parameters)
    expt.run()
    # expt.run(simulate=True)
