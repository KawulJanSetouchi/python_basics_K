
import open3d as o3d

if __name__ == "__main__":
    print("Load a ply point cloud, print it, and render it")
    #sample_ply_data = o3d.data.PLYPointCloud()
    pcd = o3d.io.read_point_cloud("C:/Users/kawuli/Desktop/new_project3D/study_Point_cloudData/DemoCropPointCloud/fragment.ply")
    # Flip it, otherwise the pointcloud will be upside down.
    pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
    print(pcd)
    o3d.visualization.draw([pcd])
    print("Downsample the point cloud with a voxel of 0.05")
    downpcd = pcd.voxel_down_sample(voxel_size=0.05)
    o3d.visualization.draw([downpcd])