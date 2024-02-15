import open3d as o3d
import time
# point_cloud_iss_keypoint_detector
if __name__ == "__main__":
    # Compute ISS Keypoints on armadillo pointcloud.)
    mesh = o3d.io.read_triangle_mesh("C:/Users/kawuli/Desktop/new_project3D/study_Point_cloudData/DemoCropPointCloud/ArmadilloMesh.ply")
    pcd = o3d.geometry.PointCloud()
    pcd.points = mesh.vertices

    tic = time.time()
    keypoints = o3d.geometry.keypoint.compute_iss_keypoints(pcd)
    toc = 1000 * (time.time() - tic)
    print("ISS Computation took {:.0f} [ms]".format(toc))

    mesh.compute_vertex_normals()
    mesh.paint_uniform_color([0.5, 0.5, 0.5])
    keypoints.paint_uniform_color([1.0, 0.0, 0.0])
    o3d.visualization.draw([keypoints, mesh], point_size=5)