import pytest
from nri_simulator import NRISimulator

def test_refractive_index():
    sim = NRISimulator()
    # Negative Refractive Index Check
    n_neg = sim.calculate_refractive_index(-2.0, -1.5)
    assert n_neg < 0
    assert round(n_neg, 6) == -1.732051

    # Positive Refractive Index Check
    n_pos = sim.calculate_refractive_index(2.0, 1.5)
    assert n_pos > 0

def test_perfect_absorption():
    sim = NRISimulator()
    efficiency = sim.simulate_perfect_absorption(10.0, 0.3)
    assert 0.0 < efficiency < 1.0
