import laspy
import open3d as o3d
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import  rasterio
import  alphashape as ash
import geopandas as gpd
import shapely as sh

from rasterio.transform import  from_origin
from rasterio.enums import Resampling
from rasterio.features import shapes
from shapely.geometry import Polygon

#print(laspy.__version__)
#Data load ...
las = laspy.read("C:/Users/kawuli\Desktop/new_project3D/study_Point_cloudData/01ke9821_org.las")

# Explore the classification field
# print(np.unique(las.classification))
# print([dimension.name for dimension in las.point_format.dimensions])

# explore CRS info
#crs=las.vlrs[2].string
#print(las.vlrs[2].string)

# Create  a mask to filter points
pst_mask=las.classification ==1
# Apply the mask and get the coordinate if the filtered dataset
xyz_t=np.vstack((las.x[pst_mask],las.y[pst_mask],las.z[pst_mask]))
# transform to the open3D .o3d .geometry.pointCloud and visualize
pcd_o3d =o3d.geometry.PointCloud()
pcd_o3d.points=o3d.utility.Vector3dVector(xyz_t.transpose())

# translate the point cloud , and keep the translation to reapply at the end
pcd_center =pcd_o3d.get_center()
pcd_o3d.translate(-pcd_center)

# Visualize the results
#o3d.visualization.draw_geometries([pcd_o3d])

# Isolating Group points
pts_mask =las.classification==1
xyz_t=np.vstack((las.x[pts_mask], las.y[pts_mask], las.z[pts_mask]))
ground_pts =o3d.geometry.PointCloud()
ground_pts.points =o3d.utility.Vector3dVector(xyz_t.transpose())
ground_pts.translate(-pcd_center)
# visualize
#o3d.visualization.draw_geometries([ground_pts])

# Identifying the average distance between building points
nn_distance =np.mean(pcd_o3d.compute_nearest_neighbor_distance())
#print("average point distance(m): ", nn_distance)

#Defintion clusters
epsilon =2
min_cluster_points=100

labels =np.array(pcd_o3d.cluster_dbscan(eps=epsilon, min_points=min_cluster_points))
max_label =labels.max()
#print(f"point cloud has {max_label +1} clusters")

# we use a discrete color palette to randomize the visualization
colors =plt.get_cmap("tab20")(labels /(max_label if max_label > 0 else 1))
colors[labels <0]=0
pcd_o3d.colors =o3d.utility.Vector3dVector(colors[:,:3])

# Point cloud Visualization
#o3d.visualization.draw_geometries([pcd_o3d])

#selecting a segment to be considered
sel=3
segment =pcd_o3d.select_by_index(np.where(labels==sel)[0])
#o3d.visualization.draw_geometries([segment])

#Extract only the X and Y coordinates of our point cloud
points_2D=np.asarray(segment.points)[:,0:2]
building_vector=ash.alphashape(points_2D, alpha=0.2)
#print(building_vector)
plt.show()

# store in Geodataframe the 2D polygon
building_gdf =gpd.GeoDataFrame(geometry=[building_vector], crs='EPSG:26910')
building_gdf.head(1)




