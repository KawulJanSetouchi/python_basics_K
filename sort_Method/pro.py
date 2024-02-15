import open3d as o3d
import numpy as np

pcd = o3d.io.read_point_cloud("C:/Users/kawuli/Desktop/new_project3D/デモ用データ/20_堰堤メッシュ.ply")

o3d.visualization.draw_geometries([pcd])
