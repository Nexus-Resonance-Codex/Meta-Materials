"""
NRC Visualizer Dashboard
========================
High-performance, interactive web dashboard using FastAPI and Streamlit/Plotly
for visualizing 3D meta-material lattices, stress-strain fields, and resonance waves.
"""

import numpy as np
import plotly.graph_objects as go
import streamlit as st

from universal_engine import AcousticMetamaterial, ElectromagneticMetamaterial


def generate_lattice_visualization(grid_size: int = 3):
    """
    Generates a 3D Plotly visualization of a standard metamaterial lattice structure.
    """
    x, y, z = np.mgrid[0:grid_size, 0:grid_size, 0:grid_size]

    fig = go.Figure(
        data=go.Scatter3d(
            x=x.flatten(),
            y=y.flatten(),
            z=z.flatten(),
            mode="markers+lines",
            marker=dict(size=12, color=z.flatten(), colorscale="Viridis", opacity=0.8),
            line=dict(color="rgba(200,200,200,0.5)", width=2),
        )
    )

    fig.update_layout(
        title="Meta-Material Lattice Topology (TTT-7 Manifold)",
        scene=dict(
            xaxis_title="X (Lattice Const)",
            yaxis_title="Y (Lattice Const)",
            zaxis_title="Z (Layer)",
        ),
        margin=dict(l=0, r=0, b=0, t=40),
    )
    return fig


def generate_resonance_wave():
    """
    Simulates a 3D surface plot representing bulk resonance reinforcement.
    """
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    x, y = np.meshgrid(x, y)

    # phi-spiral resonance mathematical simulation
    r = np.sqrt(x**2 + y**2)
    phi = 1.618
    z = np.sin(r * phi) / (r + 1)

    fig = go.Figure(data=[go.Surface(z=z, x=x, y=y, colorscale="Plasma")])
    fig.update_layout(
        title="φ-Spiral Resonance (Phi-Infinity) Wave Propagation",
        autosize=False,
        width=700,
        height=500,
        margin=dict(l=65, r=50, b=65, t=90),
    )
    return fig


def main():
    st.set_page_config(page_title="NRC Visualizer Dashboard", layout="wide")
    st.title("🪐 Nexus Resonance Codex (NRC) Dashboard")
    st.markdown(
        "Real-time simulation of Meta-Material Physics and TTT-7 Stability Manifolds."
    )

    st.sidebar.header("Simulation Parameters")
    material_type = st.sidebar.selectbox(
        "Material Class", ["Electromagnetic", "Acoustic", "Optical", "Mechanical"]
    )
    lattice_const = st.sidebar.slider("Lattice Constant (a)", 0.1, 5.0, 1.0)
    frequency = st.sidebar.number_input("Frequency (GHz/THz)", value=10.0)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("3D Lattice Structure")
        fig_lattice = generate_lattice_visualization(
            grid_size=int(lattice_const * 3) + 1
        )
        st.plotly_chart(fig_lattice, use_container_width=True)

    with col2:
        st.subheader("Resonance Manifold Wave")
        fig_wave = generate_resonance_wave()
        st.plotly_chart(fig_wave, use_container_width=True)

    st.subheader("Live Analytics (TTT-7 / BRR)")

    if material_type == "Electromagnetic":
        em = ElectromagneticMetamaterial(frequency, "Custom", lattice_const, 2.0, 1.5)
        tau = em.calculate_ttt7_stability()
        tau_re = em.apply_bulk_reinforcement(tau)

        st.metric(label="Base TTT-7 Stability (τ)", value=f"{tau:.4f}")
        st.metric(label="Reinforced Stability (BRR)", value=f"{tau_re:.4f}")
        if tau_re > 0.5:
            st.success("STATUS: OPTIMAL STABILITY (Phase 3 Active)")
        else:
            st.warning("STATUS: DECAY DETECTED (Increase lattice constant)")

    elif material_type == "Acoustic":
        ac = AcousticMetamaterial(frequency, "Air-Cavity", lattice_const, -1.2e5, -1.1)
        tensor = ac.calculate_acoustic_tensor()

        st.metric(label="Effective Density", value=f"{tensor['effective_density']:.4f}")
        st.info(f"Acoustic State: {tensor['status']}")


if __name__ == "__main__":
    main()
