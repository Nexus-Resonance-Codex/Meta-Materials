from universal_engine import (
    AcousticMetamaterial,
    BaseMetamaterial,
    ElectromagneticMetamaterial,
    MechanicalMetamaterial,
    OpticalMetamaterial,
)


def test_base_metamaterial():
    base = BaseMetamaterial(1.0, "Test", 1.0)
    phi = base.calculate_phi_spiral_resonance(1.618, 1)
    assert phi > 1.618


def test_electromagnetic_metamaterial():
    em = ElectromagneticMetamaterial(10.0, "Gold", 1.0, 2.0, 1.5)
    tau = em.calculate_ttt7_stability()
    assert 0.0 < tau < 1.0


def test_acoustic_metamaterial():
    acoustic = AcousticMetamaterial(1.5, "Air-Cavity", 0.1, -1.2e5, -1.1)
    tensor = acoustic.calculate_acoustic_tensor()
    assert tensor["status"] == "ANOMALOUS"
    assert tensor["effective_density"] < 0


def test_mechanical_metamaterial():
    mech = MechanicalMetamaterial(0.0, "Titanium-Lattice", 0.05, 110e9, -0.4)
    compliance = mech.calculate_compliance_matrix()
    assert compliance["is_auxetic"] == "AUXETIC"
    assert compliance["s12"] > 0  # Since poisson is negative, -nu/E is positive


def test_optical_metamaterial():
    optical = OpticalMetamaterial(400.0, "Silicon-Photonics", 400e-9, 3.48)
    new_index = optical.manipulate_refractive_index(1e6)
    assert new_index < 3.48
