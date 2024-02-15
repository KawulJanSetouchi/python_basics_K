import open3d as o3d

# Load point cloud
pcd = o3d.io.read_point_cloud("C:/Users/kawuli/Desktop/new_project3D/デモ用データ/20_堰堤メッシュ.ply")

cloud = o3d.geometry.PointCloud()
cloud.points = o3d.cpu.pybind.utility.Vector3dVector(pcd)
# Ball pivoting algorithm
#mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(pcd)
mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_alpha_shape(pcd=cloud, alpha=10.0)
# Visualize the mesh
o3d.visualization.draw_geometries([mesh])

# Optional: Save the mesh
o3d.io.write_triangle_mesh("C:/Users/kawuli/Desktop/new_project3D/デモ用データ/surface_mesh.ply", mesh)
