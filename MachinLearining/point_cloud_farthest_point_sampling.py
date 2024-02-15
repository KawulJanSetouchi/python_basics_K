import open3d as o3d

# Geometry point_cloud_farthest_point_sampling
if __name__ == "__main__":
    # Load bunny data.

    pcd = o3d.io.read_point_cloud("C:/Users/kawuli/Desktop/new_project3D/study_Point_cloudData/DemoCropPointCloud/BunnyMesh.ply")
    pcd.paint_uniform_color([0.5, 1, 0.5])

    # Get 1000 samples from original point cloud and paint to green.
    pcd_down = pcd.farthest_point_down_sample(1000)
    pcd_down.paint_uniform_color([0, 1, 0])
    o3d.visualization.draw_geometries([pcd, pcd_down])