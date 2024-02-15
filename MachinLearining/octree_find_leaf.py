
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

    octree = o3d.geometry.Octree(max_depth=4)
    octree.convert_from_point_cloud(pcd, size_expand=0.01)
    print('Displaying input octree ...')
    o3d.visualization.draw([octree])
    print('Finding leaf node containing the first point of pointcloud ...')
    print(octree.locate_leaf_node(pcd.points[0]))