import plotly.graph_objects as go

from dashboard import generate_lattice_visualization, generate_resonance_wave


def test_lattice_visualization():
    fig = generate_lattice_visualization(grid_size=2)
    assert isinstance(fig, go.Figure)
    assert "Scatter3d" in str(type(fig.data[0]))
    assert "Meta-Material Lattice Topology" in fig.layout.title.text


def test_resonance_wave():
    fig = generate_resonance_wave()
    assert isinstance(fig, go.Figure)
    assert "Surface" in str(type(fig.data[0]))
    assert "φ-Spiral Resonance" in fig.layout.title.text
