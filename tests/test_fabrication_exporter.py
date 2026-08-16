import os
import pytest
from fabrication_exporter import FabricationExporter


@pytest.fixture
def exporter():
    exp = FabricationExporter(output_dir="test_outputs")
    yield exp
    # Cleanup
    if os.path.exists("test_outputs"):
        for f in os.listdir("test_outputs"):
            os.remove(os.path.join("test_outputs", f))
        os.rmdir("test_outputs")


def test_generate_lattice_mesh(exporter):
    mesh = exporter.generate_lattice_mesh(grid_size=2)
    assert mesh is not None
    assert len(mesh.faces) > 0


def test_export_formats(exporter):
    mesh = exporter.generate_lattice_mesh(grid_size=1)
    stl_path = exporter.export_mesh(mesh, "test_mesh", "stl")
    obj_path = exporter.export_mesh(mesh, "test_mesh", "obj")

    assert os.path.exists(stl_path)
    assert os.path.exists(obj_path)


def test_generate_gcode(exporter):
    mesh = exporter.generate_lattice_mesh(grid_size=1)
    gcode_path = exporter.generate_gcode(mesh, "test_gcode")

    assert os.path.exists(gcode_path)
    with open(gcode_path, "r") as f:
        content = f.read()
        assert "G28" in content
        assert "NRC Custom Meta-Material Toolpath" in content
