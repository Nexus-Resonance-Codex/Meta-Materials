# 3D Print & Fabrication Exporter

The `fabrication_exporter.py` module takes mathematical lattice properties and outputs them to standard 3D meshes for rapid prototyping.

### Features
* **Mesh Generation**: Generates icosphere nodes at lattice intersection points using `trimesh`.
* **Standard Exports**: Fully supports exporting to `.stl`, `.obj`, and `.3mf`.
* **G-Code Generation**: Generates highly specialized, bare-metal `.gcode` for direct execution on industrial SLA/SLS/FDM hardware.

### Quick Export Guide
```python
from fabrication_exporter import FabricationExporter

exporter = FabricationExporter(output_dir="outputs")
mesh = exporter.generate_lattice_mesh(grid_size=5)

# Export to STL for standard slicing
exporter.export_mesh(mesh, "my_lattice", "stl")

# Export directly to custom FDM G-Code
exporter.generate_gcode(mesh, "my_lattice")
```
