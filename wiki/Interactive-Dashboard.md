# Interactive Web Dashboard

To visualize the mathematics and structures natively, the NRC includes a high-performance interactive dashboard built on **FastAPI**, **Streamlit**, and **Plotly**.

### Running the Dashboard
Ensure you have installed the required dependencies from `requirements.txt`. Then execute:
```bash
streamlit run src/dashboard.py
```

### Dashboard Features
1. **Lattice Topology**: Renders an interactive 3D scatter plot of the meta-material nodes.
2. **Resonance Wave Mapping**: Renders a 3D surface plot simulating the $\varphi$-spiral wave propagation through the substrate.
3. **Live Analytics**: A sidebar allows you to tweak frequency, lattice constants, and material classes, instantly re-calculating TTT-7 stability metrics and Acoustic effective densities in real time.
