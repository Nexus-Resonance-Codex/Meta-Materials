"""
NEXUS RESONANCE CODEX - Phase 3: Quantum Resonance Integration (QRI)
Module: rydberg_sim.py
Standard: God-tier / TTT-7 Stable (Digital Root 7)
"""

import math
from scipy.constants import hbar, eV

class RydbergSimulator:
    """
    Simulates the coupling between the THz Metamaterial Lattice
    and the Rydberg Quantum State (n=50).
    
    Goal: Calculate Delta_R (Resonance Shift) and LQG (Lattice-Quantum Gain).
    """
    
    def __init__(self, n_state: int = 50):
        self.n = n_state
        self.phi = 1.61803398875
        
    def execute_simulation(self, frequency_thz: float, t2_ms: float, p_ex: float) -> dict:
        """
        Executes the Rydberg-Lattice coupling simulation.
        """
        # Convert units
        f_hz = frequency_thz * 1e12
        t2_s = t2_ms * 1e-3
        
        # Calculate Rydberg Energy (E = -13.6 eV / n^2)
        e_rydberg_ev = -13.6 / (self.n ** 2)
        e_rydberg_j = e_rydberg_ev * eV
        
        # Rydberg Resonance Shift (Delta_R)
        # Delta_R = (E / hbar) - f_res
        omega_rydberg = abs(e_rydberg_j / hbar)
        delta_r = omega_rydberg - (2 * math.pi * f_hz)
        
        # Lattice-Quantum Gain (LQG)
        # LQG = (P_ex * T2) / (hbar * Delta_R) scaled for TTT-7
        lqg = abs((p_ex * t2_s) / (hbar * delta_r)) * 1e34 # Scaling for visibility
        
        return {
            "n_state": self.n,
            "rydberg_energy_ev": round(e_rydberg_ev, 6),
            "delta_r_hz": round(delta_r, 2),
            "lqg_index": round(lqg, 7),
            "ttt7_status": "STABLE" if self._check_ttt7(lqg) else "CHAOTIC"
        }
        
    def _check_ttt7(self, value: float) -> bool:
        """
        Final Phase 3 TTT-7 Stability Check.
        """
        scaled_val = int(abs(value) * 1e7)
        if scaled_val == 0: return True
        dr = scaled_val % 9
        return (dr if dr != 0 else 9) in {1, 2, 4, 5, 7, 8}

if __name__ == "__main__":
    # Parameters from QRI Step 1-3
    sim = RydbergSimulator()
    results = sim.execute_simulation(
        frequency_thz=5.0, 
        t2_ms=1.2090419, 
        p_ex=0.4653555
    )
    
    print("--- NRC PHASE 3: RYDBERG TARGET SIMULATION (FINAL) ---")
    for key, val in results.items():
        print(f"{key.upper()}: {val}")
    print("------------------------------------------------------")
