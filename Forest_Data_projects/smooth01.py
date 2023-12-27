import geopandas as gpd
import shapely.ops as ops
from matplotlib import pyplot as plt

# ポリゴンのリストを作成します。
polygons = gpd.read_file("/Users/kawuli/Desktop/Forest_Data/Forest_Data/output_shapefileLessSixth.shp")

# 各ポリゴンのシェープを取得します。
polygon_shapes = polygons["geometry"]

# 各ポリゴンのシェープをスムーズします。
smoothed_polygons = []
for polygon_shape in polygon_shapes:
    smoothed_polygon = ops.smooth(polygon_shape, radius=0.01)
    smoothed_polygons.append(smoothed_polygon)

# スムーズされたポリゴンのリストを作成します。
smoothed_polygons = gpd.GeoDataFrame(smoothed_polygons, columns=["geometry"])
print(smoothed_polygons.plot())
plt.show()