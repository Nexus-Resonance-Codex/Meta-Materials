---
name: Verify TTT-7 Stability Manifold
description: Interrogate the NRC mathematical engine to generate proofs for the TTT-7 stability equations.
model: gpt-4
temperature: 0.2
---

You are an expert computational physicist analyzing the Nexus Resonance Codex (NRC).

Below is the foundational Python code governing the Trageser Tensor Theorem (TTT-7) Stability Manifold.

```python
def calculate_ttt7_stability(lattice_constant, permittivity, permeability):
    numerator = (lattice_constant**2) * permittivity * permeability
    tau = numerator / (1 + (numerator**2))
    return tau
```

Your task is to mathematically prove and explain why the maximum possible stability $\tau$ is exactly $0.5$ using differential calculus.

1. Write out the equation $f(x) = \frac{x}{1+x^2}$ where $x = a^2 \epsilon \mu$.
2. Take the derivative with respect to $x$.
3. Set the derivative to 0 to find the critical points.
4. Conclude with a rigorous explanation of how this mathematical bound physically anchors the metamaterial lattice in the high-frequency Terahertz regime.

Please output the mathematical proof in clean, readable LaTeX format.
