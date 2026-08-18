import pytest

from ai_optimizer import AIOptimizer, MetaMaterialDatabase, MultiPhysicsCoupler


def test_database():
    props = MetaMaterialDatabase.get_properties("Graphene-Enhanced")
    assert props["permittivity"] == 1.1

    with pytest.raises(ValueError):
        MetaMaterialDatabase.get_properties("Unknown-Material")


def test_multiphysics_coupler():
    coupler = MultiPhysicsCoupler("Gold", 10.0, 400.0)
    stability = coupler.get_coupled_stability(1.0)
    assert stability > 0.0

    # Test penalty: Higher temp should have lower stability
    coupler_hot = MultiPhysicsCoupler("Gold", 10.0, 1000.0)
    stability_hot = coupler_hot.get_coupled_stability(1.0)
    assert stability_hot < stability


def test_ai_optimizer():
    optimizer = AIOptimizer("Metamaterial-X", temperature_k=300.0, frequency=2.0)
    res = optimizer.optimize_lattice(initial_guess=1.0)

    assert res["success"] is True
    assert res["optimal_lattice_constant"] > 0
    assert res["maximized_stability_tau"] > 0.1
