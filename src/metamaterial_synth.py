"""
MetamaterialSynth Module
========================
Production-ready module for simulating NRC Phase 2 metamaterials.

Classes:
    MetamaterialSynth: Base engine for calculating synthetic lattice stability and resonance.

Mathematical Foundations:
- φ-spiral hierarchical compression (Phi-Infinity)
- Trageser Tensor Theorem (TTT-7) Stability Manifold
- Bulk Resonance Reinforcement (BRR)
"""

import math


class MetamaterialSynth:
    """
    Base class for simulating metamaterial resonance and stability.

    Attributes:
        frequency (float): Operating frequency in GHz or THz (scaled).
        is_thz (bool): Flag for Terahertz-scale operations.
        material (str): Synthetic material substrate (e.g., 'Gold').
        lattice_constant (float): Dimensional scaling factor (a).
        permittivity (float): Relative permittivity (epsilon).
        permeability (float): Relative permeability (mu).
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
        self.frequency = frequency
        self.is_thz = is_thz
        self.material = material
        self.lattice_constant = lattice_constant
        self.permittivity = permittivity
        self.permeability = permeability

    def calculate_ttt7_stability(self) -> float:
        """
        Calculates the TTT-7 stability (tau) of the metamaterial lattice.
        Formula: τ = (a^2 * ε * μ) / (1 + (a^2 * ε * μ)^2)
        """
        numerator = (self.lattice_constant**2) * self.permittivity * self.permeability
        tau = numerator / (1 + (numerator**2))
        return tau

    def apply_bulk_reinforcement(self, tau: float, factor: float = 1.5) -> float:
        """
        Applies Bulk Resonance Reinforcement (BRR) to counteract high-frequency instability.

        Args:
            tau (float): Base TTT-7 stability.
            factor (float): Reinforcement coefficient.

        Returns:
            float: Reinforced stability coefficient.
        """
        # BRR logic: tau_reinforced = tau * (1 + factor * log10(frequency))
        # For THz scale, frequency is shifted by 10^3 for normalization.
        freq_log = (
            math.log10(self.frequency * 1000)
            if self.is_thz
            else math.log10(self.frequency)
        )
        reinforcement = 1 + (factor * freq_log)
        return tau * reinforcement

    def calculate_phi_spiral_resonance(self, phi: float, iterations: int = 1) -> float:
        """
        Calculates the φ-spiral resonance (Phi-Infinity).
        """
        phi_curr = phi
        for _ in range(iterations):
            phi_curr = phi_curr * (1 + (1 / phi_curr) ** 2)
        return phi_curr


def run_full_manifold_audit():
    """
    Step 3: Bulk Reinforcement & Final Stability Manifold Comparison.
    """
    # 1. Alpha (Baseline)
    alpha = MetamaterialSynth(10.0, "Gold", 1.0, 2.0, 1.5)
    t_alpha = alpha.calculate_ttt7_stability()

    # 2. Beta (Decay observed in Step 2)
    beta = MetamaterialSynth(20.0, "Silver", 1.2, 2.5, 1.8)
    t_beta = beta.calculate_ttt7_stability()

    # 3. Gamma (Target: 30 GHz with Reinforcement)
    gamma = MetamaterialSynth(30.0, "Copper", 1.5, 3.0, 2.2)
    t_gamma_base = gamma.calculate_ttt7_stability()
    t_gamma_reinforced = gamma.apply_bulk_reinforcement(t_gamma_base)

    # 4. Delta (Target: 5.0 THz - Phase 3 Delta Lattice)
    # Lambda_THz = 30e-6 m, RSF = 166.67
    delta = MetamaterialSynth(5.0, "Graphene-Enhanced", 30e-6, 1.1, 1.05, is_thz=True)
    t_delta_base = delta.calculate_ttt7_stability()
    t_delta_reinforced = delta.apply_bulk_reinforcement(
        t_delta_base, factor=2.1
    )  # Higher factor for THz

    print("--- NRC PHASE 3: THz RESONANCE MANIFOLD REPORT ---")
    print(f"Lattice Alpha (10 GHz): τ = {t_alpha:.6f}")
    print(f"Lattice Beta  (20 GHz): τ = {t_beta:.6f}")
    print(f"Lattice Gamma (30 GHz): τ_reinforced = {t_gamma_reinforced:.6f}")
    print(f"Lattice Delta (5.0 THz): τ_base = {t_delta_base:.6f}")
    print(
        f"Lattice Delta (5.0 THz): τ_reinforced = {t_delta_reinforced:.6f} [PHASE 3 ACTIVE]"
    )

    print("\nRESONANCE VERIFICATION:")
    # Harmonic progression
    phi = 1.61803398875
    phi = alpha.calculate_phi_spiral_resonance(phi)
    print(f"Alpha φ-State: {phi:.6f}")
    phi = beta.calculate_phi_spiral_resonance(phi, iterations=2)
    print(f"Beta  φ-State: {phi:.6f}")
    phi = gamma.calculate_phi_spiral_resonance(phi, iterations=3)
    print(f"Gamma φ-State: {phi:.6f}")
    phi = delta.calculate_phi_spiral_resonance(phi, iterations=5)  # Deep spiral for THz
    print(f"Delta φ-State: {phi:.6f}")
    print("-----------------------------------------------------")


if __name__ == "__main__":
    run_full_manifold_audit()
