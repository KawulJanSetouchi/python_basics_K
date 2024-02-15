import open3d as o3d
import numpy as np

if __name__ == "__main__":


    mesh = o3d.io.read_triangle_mesh("C:/Users/kawuli/Desktop/new_project3D/study_Point_cloudData/DemoCropPointCloud/BunnyMesh.ply")
    mesh.compute_vertex_normals()

    # Fit to unit cube.
    mesh.scale(1 / np.max(mesh.get_max_bound() - mesh.get_min_bound()),
               center=mesh.get_center())
    print('Displaying input mesh ...')
    o3d.visualization.draw([mesh])

    voxel_grid = o3d.geometry.VoxelGrid.create_from_triangle_mesh(
        mesh, voxel_size=0.05)
    print('Displaying voxel grid ...')
    o3d.visualization.draw([voxel_grid])