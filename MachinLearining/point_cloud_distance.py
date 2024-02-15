import open3d as o3d
import numpy as np

# Geometry point_cloud_distance
if __name__ == "__main__":

    pcd = o3d.io.read_point_cloud("C:/Users/kawuli/Desktop/new_project3D/study_Point_cloudData/fragment.ply")
    vol = o3d.visualization.read_selection_polygon_volume(
        "C:/Users/kawuli/Desktop/new_project3D/study_Point_cloudData/cropped.json")
    chair = vol.crop_point_cloud(pcd)

    chair.paint_uniform_color([0, 0, 1])
    pcd.paint_uniform_color([1, 0, 0])
    print("Displaying the two point clouds used for calculating distance ...")
    o3d.visualization.draw([pcd, chair])

    dists = pcd.compute_point_cloud_distance(chair)
    dists = np.asarray(dists)
    print("Printing average distance between the two point clouds ...")
    print(dists)
