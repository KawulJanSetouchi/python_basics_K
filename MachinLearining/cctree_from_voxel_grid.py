
import open3d as o3d
import numpy as np

if __name__ == "__main__":
    N = 2000
    #armadillo_data = o3d.data.ArmadilloMesh()
    pcd = o3d.io.read_triangle_mesh(
        "C:/Users/kawuli/Desktop/new_project3D/study_Point_cloudData/DemoCropPointCloud/ArmadilloMesh.ply").sample_points_poisson_disk(N)
    # Fit to unit cube.
    pcd.scale(1 / np.max(pcd.get_max_bound() - pcd.get_min_bound()),
              center=pcd.get_center())
    pcd.colors = o3d.utility.Vector3dVector(np.random.uniform(0, 1,
                                                              size=(N, 3)))
    print('Displaying input voxel grid ...')
    voxel_grid = o3d.geometry.VoxelGrid.create_from_point_cloud(pcd,
                                                                voxel_size=0.05)
    o3d.visualization.draw([voxel_grid])

    octree = o3d.geometry.Octree(max_depth=4)
    octree.create_from_voxel_grid(voxel_grid)
    print('Displaying octree ..')
    o3d.visualization.draw([octree])