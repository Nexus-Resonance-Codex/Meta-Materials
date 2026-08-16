import pytest
from metamaterial_synth import MetamaterialSynth
from nri_simulator import NRISimulator
from absorption_optimizer import AbsorptionOptimizer

def test_absorption_optimization():
    synth = MetamaterialSynth(30.0, "Copper", 1.5, 3.0, 2.2)
    sim = NRISimulator()
    pao = AbsorptionOptimizer(synth, sim)

    tau = synth.calculate_ttt7_stability()
    q_factor = pao.calculate_q_factor(30.0, tau)

    assert q_factor > 0

    final_efficiency = pao.push_to_perfect_absorption(0.272702, q_factor)
    assert final_efficiency >= 0.90
