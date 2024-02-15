import open3d as o3d
import numpy as np

#point_cloud_hidden_point_removal

if __name__ == "__main__":

    # Convert mesh to a point cloud and estimate dimensions.

    pcd = o3d.io.read_triangle_mesh(
        "C:/Users/kawuli/Desktop/new_project3D/study_Point_cloudData/DemoCropPointCloud/ArmadilloMesh.ply").sample_points_poisson_disk(5000)
    diameter = np.linalg.norm(
        np.asarray(pcd.get_max_bound()) - np.asarray(pcd.get_min_bound()))
    print("Displaying input point cloud ...")
    o3d.visualization.draw([pcd], point_size=5)

    # Define parameters used for hidden_point_removal.
    camera = [0, 0, diameter]
    radius = diameter * 100

    # Get all points that are visible from given view point.
    _, pt_map = pcd.hidden_point_removal(camera, radius)

    print("Displaying point cloud after hidden point removal ...")
    pcd = pcd.select_by_index(pt_map)
    o3d.visualization.draw([pcd], point_size=5)