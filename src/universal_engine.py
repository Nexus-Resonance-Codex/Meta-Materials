"""
Universal Meta-Material Engine
==============================
Broadens the core engine beyond electromagnetic/THz physics to include
Acoustic, Mechanical, and Optical metamaterials.

Base Classes and Specific Modules:
- BaseMetamaterial
- ElectromagneticMetamaterial (Extends legacy MetamaterialSynth)
- AcousticMetamaterial
- MechanicalMetamaterial
- OpticalMetamaterial
"""

import math
from typing import Dict, Any


class BaseMetamaterial:
    """
    Generalized base class for any metamaterial leveraging NRC TTT-7 and phi-spiral dynamics.
    """

    def __init__(
        self,
        frequency: float,
        material: str,
        lattice_constant: float,
    ):
        self.frequency = frequency
        self.material = material
        self.lattice_constant = lattice_constant

    def calculate_phi_spiral_resonance(self, phi: float, iterations: int = 1) -> float:
        """
        Calculates the φ-spiral resonance (Phi-Infinity) universally applicable.
        """
        phi_curr = phi
        for _ in range(iterations):
            phi_curr = phi_curr * (1 + (1 / phi_curr) ** 2)
        return phi_curr


class ElectromagneticMetamaterial(BaseMetamaterial):
    """
    Electromagnetic / THz metamaterial incorporating permittivity and permeability.
    """

    def __init__(
        self,
        frequency: float,
        material: str,
        lattice_constant: float,
        permittivity: float,
        permeability: float,
        is_thz: bool = False,
    ):
        super().__init__(frequency, material, lattice_constant)
        self.permittivity = permittivity
        self.permeability = permeability
        self.is_thz = is_thz

    def calculate_ttt7_stability(self) -> float:
        """
        Formula: τ = (a^2 * ε * μ) / (1 + (a^2 * ε * μ)^2)
        """
        numerator = (self.lattice_constant**2) * self.permittivity * self.permeability
        tau = numerator / (1 + (numerator**2))
        return tau

    def apply_bulk_reinforcement(self, tau: float, factor: float = 1.5) -> float:
        freq_log = (
            math.log10(self.frequency * 1000)
            if self.is_thz
            else math.log10(self.frequency)
        )
        reinforcement = 1 + (factor * freq_log)
        return tau * reinforcement


class AcousticMetamaterial(BaseMetamaterial):
    """
    Acoustic metamaterial with negative bulk modulus and mass density.
    """

    def __init__(
        self,
        frequency: float,
        material: str,
        lattice_constant: float,
        bulk_modulus: float,
        mass_density: float,
    ):
        super().__init__(frequency, material, lattice_constant)
        self.bulk_modulus = bulk_modulus
        self.mass_density = mass_density

    def calculate_acoustic_tensor(self) -> Dict[str, float]:
        """
        Simulates the effective acoustic tensor.
        Negative values indicate anomalous wave propagation (e.g., sound blocking).
        """
        tensor_c11 = self.bulk_modulus / self.mass_density
        # Effective mass density modification based on TTT-7 phi-resonance
        eff_density = self.mass_density * (
            1 - self.calculate_phi_spiral_resonance(1.618) * 0.1
        )

        return {
            "effective_density": eff_density,
            "tensor_c11": tensor_c11,
            "status": "ANOMALOUS" if eff_density < 0 or tensor_c11 < 0 else "NORMAL",
        }


class MechanicalMetamaterial(BaseMetamaterial):
    """
    Mechanical (auxetic) metamaterial featuring negative Poisson's ratio.
    """

    def __init__(
        self,
        frequency: float,
        material: str,
        lattice_constant: float,
        youngs_modulus: float,
        poissons_ratio: float,
    ):
        super().__init__(frequency, material, lattice_constant)
        self.youngs_modulus = youngs_modulus
        self.poissons_ratio = poissons_ratio

    def calculate_compliance_matrix(self) -> Dict[str, Any]:
        """
        Calculates compliance matrix for mechanical metamaterials (auxetics).
        """
        # Simplification of a 2D orthotropic compliance matrix
        s11 = 1.0 / self.youngs_modulus
        s12 = -self.poissons_ratio / self.youngs_modulus

        auxetic_status = "AUXETIC" if self.poissons_ratio < 0 else "CONVENTIONAL"

        return {
            "s11": s11,
            "s12": s12,
            "is_auxetic": auxetic_status,
            "shear_modulus": self.youngs_modulus / (2 * (1 + self.poissons_ratio)),
        }


class OpticalMetamaterial(BaseMetamaterial):
    """
    Optical metamaterial for refractive index manipulation.
    """

    def __init__(
        self,
        frequency: float,  # in THz or PHz
        material: str,
        lattice_constant: float,
        refractive_index: float,
    ):
        super().__init__(frequency, material, lattice_constant)
        self.refractive_index = refractive_index

    def manipulate_refractive_index(self, applied_field: float) -> float:
        """
        Simulates electro-optic or non-linear manipulation of the refractive index.
        """
        # Pockels effect simulation: n(E) = n - 0.5 * r * n^3 * E
        # Using phi as a standard non-linear coefficient (r)
        r_coeff = self.calculate_phi_spiral_resonance(1.618) * 1e-12
        new_index = (
            self.refractive_index
            - 0.5 * r_coeff * (self.refractive_index**3) * applied_field
        )
        return new_index


if __name__ == "__main__":
    print("--- NRC UNIVERSAL META-MATERIAL ENGINE ---")

    acoustic = AcousticMetamaterial(1.5, "Air-Cavity", 0.1, -1.2e5, -1.1)
    print("Acoustic:", acoustic.calculate_acoustic_tensor())

    mech = MechanicalMetamaterial(0.0, "Titanium-Lattice", 0.05, 110e9, -0.4)
    print("Mechanical:", mech.calculate_compliance_matrix())

    optical = OpticalMetamaterial(400.0, "Silicon-Photonics", 400e-9, 3.48)
    print("Optical Index (Field=1e6):", optical.manipulate_refractive_index(1e6))
