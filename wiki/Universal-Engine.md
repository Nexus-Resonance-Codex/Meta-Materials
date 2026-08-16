# Universal Meta-Material Engine

The `universal_engine.py` is the core architectural backend of the NRC.

### Classes Available:
1. `ElectromagneticMetamaterial`: Analyzes THz lattices for NRI (Negative Refractive Index) and perfect absorption.
2. `AcousticMetamaterial`: Computes anomalous acoustic tensors (negative mass density and bulk modulus).
3. `MechanicalMetamaterial`: Computes compliance matrices for Auxetic (negative Poisson's ratio) structures.
4. `OpticalMetamaterial`: Handles non-linear Pockels effect calculations manipulating the refractive index dynamically.

### Example Usage:
```python
from universal_engine import MechanicalMetamaterial

mech = MechanicalMetamaterial(
    frequency=0.0,
    material="Titanium-Lattice",
    lattice_constant=0.05,
    youngs_modulus=110e9,
    poissons_ratio=-0.4 # Auxetic property
)

compliance = mech.calculate_compliance_matrix()
print(compliance['is_auxetic']) # Outputs: AUXETIC
```
