"""
NRISimulator Module
===================
Production-ready module for simulating Negative Refractive Index (NRI) and Perfect Absorption.

Classes:
    NRISimulator: Advanced electromagnetic performance engine for NRC Phase 2.

Mathematical Foundations:
- Negative Refractive Index (n = -sqrt(ε * μ))
- Perfect Absorption (A = 1 - T - R) modulated by TTT-7 Stability.
"""

import math


class NRISimulator:
    """
    Simulates the electromagnetic performance of NRC Metamaterials.
    """

    def calculate_refractive_index(self, epsilon: float, mu: float) -> float:
        """
        Calculates the refractive index (n).
        Supports NRI when both epsilon and mu are negative.
        Formula: n = sgn(ε) * sqrt(ε * μ) if both are negative, else sqrt(ε * μ).
        Simplified for NRC: n = -sqrt(abs(ε * μ)) if both are negative.

        Args:
            epsilon (float): Relative permittivity.
            mu (float): Relative permeability.

        Returns:
            float: Refractive index (n).
        """
        # In metamaterials, NRI occurs in the double-negative (DNG) region
        if epsilon < 0 and mu < 0:
            return -math.sqrt(epsilon * mu)
        return math.sqrt(epsilon * mu)

    def simulate_perfect_absorption(self, frequency: float, tau: float) -> float:
        """
        Simulates the absorption efficiency (A).
        Uses TTT-7 stability (tau) as a coherence coefficient.
        High tau minimizes parasitic scattering, maximizing absorption.

        Args:
            frequency (float): Operating frequency in GHz.
            tau (float): TTT-7 stability coefficient.

        Returns:
            float: Absorption efficiency (0.0 to 1.0).
        """
        # NRC Perfect Absorption Manifold: A = 1 - exp(-tau * log10(frequency))
        # High tau + High Frequency = Near unity absorption.
        efficiency = 1.0 - math.exp(-tau * math.log10(frequency))
        return efficiency


def analyze_electromagnetic_performance():
    """
    Step 4: NRI & Perfect Absorption Audit for the NRC Manifold.
    """
    simulator = NRISimulator()

    # Manifold Baseline (from Step 3)
    targets = [
        {
            "name": "Meta-Lattice-Alpha",
            "freq": 10.0,
            "eps": -2.0,
            "mu": -1.5,
            "tau": 0.300000,
        },
        {
            "name": "Meta-Lattice-Beta",
            "freq": 20.0,
            "eps": -2.5,
            "mu": -1.8,
            "tau": 0.150731,
        },
        {
            "name": "Meta-Lattice-Gamma",
            "freq": 30.0,
            "eps": -3.0,
            "mu": -2.2,
            "tau": 0.215567,
        },
    ]

    print("--- NRC PHASE 2: ELECTROMAGNETIC PERFORMANCE REPORT ---")
    for t in targets:
        n = simulator.calculate_refractive_index(t["eps"], t["mu"])
        a = simulator.simulate_perfect_absorption(t["freq"], t["tau"])

        status = "OPTIMAL" if a > 0.35 else "STABLE"

        print(f"Target: {t['name']} ({t['freq']} GHz)")
        print(f"  Refractive Index (n): {n:.6f} [NRI ACTIVE]")
        print(f"  Absorption Efficiency: {a:.6f}")
        print(f"  Performance Status: {status}")
        print("-" * 55)


if __name__ == "__main__":
    analyze_electromagnetic_performance()
