import pytest
from metamaterial_synth import MetamaterialSynth

def test_ttt7_stability():
    # Alpha Baseline
    alpha = MetamaterialSynth(10.0, "Gold", 1.0, 2.0, 1.5)
    tau = alpha.calculate_ttt7_stability()
    assert 0.0 < tau < 1.0
    assert round(tau, 6) == 0.300000

def test_bulk_reinforcement():
    gamma = MetamaterialSynth(30.0, "Copper", 1.5, 3.0, 2.2)
    tau_base = gamma.calculate_ttt7_stability()
    tau_reinforced = gamma.apply_bulk_reinforcement(tau_base)
    assert tau_reinforced > tau_base

def test_phi_spiral_resonance():
    alpha = MetamaterialSynth(10.0, "Gold", 1.0, 2.0, 1.5)
    phi = 1.61803398875
    res = alpha.calculate_phi_spiral_resonance(phi, 1)
    assert res > phi
