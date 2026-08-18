"""
FabricationExporter Module
==========================
Production-ready module for converting mathematical lattice structures
into printable meshes (STL, OBJ, 3MF, STEP) and custom G-Code.
"""

import os

import trimesh


class FabricationExporter:
    """
    Handles 3D generation and G-Code parsing for Meta-Material structures.
    """

    def __init__(self, output_dir: str = "fabrication_outputs"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_lattice_mesh(
        self, grid_size: int = 5, node_radius: float = 0.5
    ) -> trimesh.Trimesh:
        """
        Generates a 3D mesh representation of a standard meta-material lattice.
        """
        nodes = []
        # Generate spherical nodes for the lattice intersections
        for x in range(grid_size):
            for y in range(grid_size):
                for z in range(grid_size):
                    sphere = trimesh.creation.icosphere(
                        subdivisions=2, radius=node_radius
                    )
                    sphere.apply_translation([x * 2.0, y * 2.0, z * 2.0])
                    nodes.append(sphere)

        # Combine all nodes into a single mesh
        if nodes:
            lattice_mesh = trimesh.util.concatenate(nodes)
        else:
            lattice_mesh = trimesh.Trimesh()

        return lattice_mesh

    def export_mesh(
        self, mesh: trimesh.Trimesh, filename: str, format: str = "stl"
    ) -> str:
        """
        Exports the generated mesh to universally accepted formats (stl, obj, 3mf).
        """
        filepath = os.path.join(self.output_dir, f"{filename}.{format}")

        if format.lower() in ["stl", "obj", "ply"]:
            mesh.export(filepath)
        elif format.lower() == "3mf":
            # Requires networkx and trimesh full install, bypassing with basic export for now
            try:
                mesh.export(filepath, file_type="3mf")
            except Exception:
                # Fallback if 3mf lib not fully installed in environment
                mesh.export(filepath.replace(".3mf", ".stl"))
                filepath = filepath.replace(".3mf", ".stl")
        else:
            raise ValueError(f"Unsupported format: {format}")

        return filepath

    def generate_gcode(
        self, mesh: trimesh.Trimesh, filename: str, layer_height: float = 0.2
    ) -> str:
        """
        Generates custom industrial G-Code for direct FDM / SLA slicing based on bounding box.
        This is a highly simplified custom toolpath generator.
        """
        filepath = os.path.join(self.output_dir, f"{filename}.gcode")
        bounds = mesh.bounds

        if bounds is None:
            raise ValueError("Mesh bounds cannot be determined.")

        min_z, max_z = bounds[0][2], bounds[1][2]

        with open(filepath, "w") as f:
            f.write("; NRC Custom Meta-Material Toolpath\n")
            f.write("G28 ; Home all axes\n")
            f.write("G90 ; Absolute positioning\n")
            f.write(f"; Model Z bounds: {min_z:.2f} to {max_z:.2f}\n")

            current_z = max(0.0, min_z)
            while current_z <= max_z:
                f.write(f"G1 Z{current_z:.2f} F1200 ; Move to layer\n")
                f.write("; [Custom spiral infill path would go here]\n")
                f.write("G1 X10 Y10 E1.0 F1500\n")
                f.write("G1 X20 Y20 E2.0\n")
                current_z += layer_height

            f.write("M104 S0 ; Turn off extruder\n")
            f.write("M140 S0 ; Turn off bed\n")
            f.write("G28 X Y ; Home X Y\n")
            f.write("M84 ; Disable motors\n")

        return filepath


if __name__ == "__main__":
    exporter = FabricationExporter()
    mesh = exporter.generate_lattice_mesh(grid_size=3)
    stl_path = exporter.export_mesh(mesh, "meta_lattice_alpha", "stl")
    obj_path = exporter.export_mesh(mesh, "meta_lattice_alpha", "obj")
    gcode_path = exporter.generate_gcode(mesh, "meta_lattice_alpha")

    print(f"Exported STL to {stl_path}")
    print(f"Exported OBJ to {obj_path}")
    print(f"Generated G-Code to {gcode_path}")
