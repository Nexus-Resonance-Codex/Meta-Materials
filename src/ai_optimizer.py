"""
AI & Multi-Physics Optimizer
============================
Integrates Scipy-based parameter optimization to discover optimal lattice configurations
and couples thermal-mechanical-electromagnetic properties concurrently.
"""

import math

from scipy.optimize import minimize

from universal_engine import ElectromagneticMetamaterial


class MetaMaterialDatabase:
    """
    Synthetic Materials Database referencing rare-earth and advanced metamaterials.
    """

    MATERIALS = {
        "Graphene-Enhanced": {
            "permittivity": 1.1,
            "permeability": 1.05,
            "thermal_expansion": 2e-6,
        },
        "Gold": {"permittivity": -2.0, "permeability": 1.5, "thermal_expansion": 14e-6},
        "Yttrium-Barium-Copper-Oxide": {
            "permittivity": -4.0,
            "permeability": -3.0,
            "thermal_expansion": 10e-6,
        },
        "Metamaterial-X": {
            "permittivity": -3.5,
            "permeability": -2.5,
            "thermal_expansion": 1e-6,
        },
    }

    @classmethod
    def get_properties(cls, name: str) -> dict:
        if name not in cls.MATERIALS:
            raise ValueError(f"Material {name} not found in database.")
        return cls.MATERIALS[name]


class MultiPhysicsCoupler:
    """
    Simulates thermal-mechanical-electromagnetic interactions concurrently.
    """

    def __init__(self, material_name: str, base_frequency: float, temperature_k: float):
        self.material = MetaMaterialDatabase.get_properties(material_name)
        self.temperature = temperature_k
        self.frequency = base_frequency
        self.reference_temp = 293.15  # 20C

    def get_coupled_stability(self, lattice_constant: float) -> float:
        """
        Couples thermal expansion into the electromagnetic TTT-7 stability calculation.
        """
        delta_t = self.temperature - self.reference_temp
        expanded_lattice = lattice_constant * (
            1 + (self.material["thermal_expansion"] * delta_t)
        )

        # Instantiate EM model with dynamically shifted lattice constant
        em_model = ElectromagneticMetamaterial(
            frequency=self.frequency,
            material="Dynamic",
            lattice_constant=expanded_lattice,
            permittivity=self.material["permittivity"],
            permeability=self.material["permeability"],
            is_thz=True if self.frequency >= 1.0 else False,
        )

        tau = em_model.calculate_ttt7_stability()
        # Since tau can be negative if (permittivity * permeability) is negative
        # For our stability manifold, we take the absolute resonance magnitude
        tau_magnitude = abs(tau)

        # Reinforcement based on thermal stress
        reinforced_tau = em_model.apply_bulk_reinforcement(tau_magnitude, factor=1.5)

        # If lattice expands too much, stability collapses logarithmically
        thermal_penalty = math.exp(-abs(delta_t) * 1e-3)

        return reinforced_tau * thermal_penalty


class AIOptimizer:
    """
    AI/ML driven optimizer to discover the global peak TTT-7 stability manifold.
    """

    def __init__(
        self, material_name: str, temperature_k: float = 293.15, frequency: float = 10.0
    ):
        self.coupler = MultiPhysicsCoupler(material_name, frequency, temperature_k)

    def optimize_lattice(self, initial_guess: float = 1.0):
        """
        Uses L-BFGS-B optimization to find the optimal lattice constant that maximizes stability.
        """

        # Objective function: We want to MAXIMIZE stability, so we MINIMIZE negative stability.
        def objective(x):
            a = x[0]
            stability = self.coupler.get_coupled_stability(a)
            return -stability

        # Bounds: Lattice constant must be between 0.1 and 10.0 units
        bounds = [(0.1, 10.0)]

        result = minimize(objective, [initial_guess], method="L-BFGS-B", bounds=bounds)

        optimal_a = result.x[0]
        max_stability = -result.fun

        return {
            "optimal_lattice_constant": optimal_a,
            "maximized_stability_tau": max_stability,
            "success": result.success,
        }


if __name__ == "__main__":
    print("--- NRC AI-DRIVEN MULTI-PHYSICS OPTIMIZATION ---")
    optimizer = AIOptimizer("Metamaterial-X", temperature_k=350.0, frequency=5.0)
    res = optimizer.optimize_lattice(initial_guess=2.0)

    print(
        f"Discovered Optimal Lattice Constant (a): {res['optimal_lattice_constant']:.6f}"
    )
    print(
        f"Peak TTT-7 Stability under Thermal Load: {res['maximized_stability_tau']:.6f}"
    )
