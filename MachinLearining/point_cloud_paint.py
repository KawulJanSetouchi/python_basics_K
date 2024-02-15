import open3d as o3d


#point_cloud_paint
if __name__ == "__main__":
    print("Load a ply point cloud, print it, and render it")
    pcd = o3d.io.read_point_cloud(
        "C:/Users/kawuli/Desktop/new_project3D/study_Point_cloudData/DemoCropPointCloud/fragment.ply")

    # Flip it, otherwise the pointcloud will be upside down.
    pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
    print(pcd)
    o3d.visualization.draw([pcd])
    print("Paint pointcloud")
    pcd.paint_uniform_color([1, 0.706, 0])
    o3d.visualization.draw([pcd])