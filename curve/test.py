import geopandas as gpd
import shapely.ops as ops

# ポリゴンのリストを作成します。
shapefile_path= "/Users/kawuli/Desktop/Forest_Data/Forest_Data/polygondisso.shp"
shapefile = gpd.read_file(shapefile_path)

print(shapefile.head())

polygons = shapefile["geometry"]

buffer_distance = 0.01
buffer_polygons = polygons.buffer(buffer_distance)

smoothed_buffer_polygons = []
for buffer_polygon in buffer_polygons:
    smoothed_buffer_polygon = ops.smooth(buffer_polygon, radius=0.01)
    smoothed_buffer_polygons.append(smoothed_buffer_polygon)


smoothed_polygons = []
for smoothed_buffer_polygon in smoothed_buffer_polygons:
    clipped_polygon = smoothed_buffer_polygon.clip(polygons[0])
    smoothed_polygons.append(clipped_polygon)

smoothed_shapefile = gpd.GeoDataFrame(smoothed_polygons, columns=["geometry"])

smoothed_shapefile_path = "/Users/kawuli/Desktop/Forest_Data/Forest_Data/smoothed_shapefile_without_spaces.shp"
smoothed_shapefile.to_file(smoothed_shapefile_path)
