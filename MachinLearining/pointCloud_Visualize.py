import open3d

# メッシュの読み込み
mesh =open3d.io.read_point_cloud("C:/Users/kawuli/Desktop/new_project3D/study_Point_cloudData/DemoCropPointCloud/BunnyMesh.ply")
# 頂点法線の計算
#mesh.compute_vertex_normals()

mesh.estimate_normals()

# # 視覚化
open3d.visualization.draw_geometries([mesh])

print(open3d.__version__)