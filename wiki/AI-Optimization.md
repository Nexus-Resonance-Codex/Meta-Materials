# AI & Multi-Physics Optimization

The `ai_optimizer.py` module introduces advanced thermal coupling and machine learning parameter discovery.

### Thermal Coupling
Metamaterials expand under thermal load. The `MultiPhysicsCoupler` automatically dynamically adjusts the lattice constant $a$ based on the thermal expansion coefficient of the selected substrate material (e.g., Graphene-Enhanced, YBCO), applying a logarithmic thermal penalty to the TTT-7 stability.

### AI Lattice Discovery
The `AIOptimizer` uses `scipy`'s L-BFGS-B optimization algorithm. Instead of manually guessing lattice dimensions, the AI will compute the *exact* optimal dimension that maximizes stability.

```python
from ai_optimizer import AIOptimizer

# Discover the perfect lattice dimension at 400 Kelvin for Metamaterial-X
optimizer = AIOptimizer("Metamaterial-X", temperature_k=400.0, frequency=10.0)
result = optimizer.optimize_lattice(initial_guess=1.0)

print(result['optimal_lattice_constant'])
```
