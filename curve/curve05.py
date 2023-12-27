import geopandas as gpd
import shapely
import shapely.ops as ops

# Define the original polygon
original_polygon = shapely.geometry.Polygon([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)])

# Smooth the polygon using the `ops.smooth()` function
smoothed_polygon = ops.smooth(original_polygon, radius=0.01)

# Create a GeoDataFrame from the smoothed polygon
smoothed_gdf = gpd.GeoDataFrame({'geometry': [smoothed_polygon]})

# Plot the original and smoothed polygons
original_gdf = gpd.GeoDataFrame({'geometry': [original_polygon]})

print(original_gdf.plot())
print(smoothed_gdf.plot())
