import geopandas as gpd

# Load your GeoDataFrame (replace 'your_data.shp' with your file path)
gdf = gpd.read_file('/Users/kawuli/Desktop/Forest_Data/Forest_Data/mergepolygon.shp')

# Check for neighboring polygons with the same attribute (e.g., 'name')
neighboring = gdf.groupby('林相名').geometry.unary_union

# Create a new GeoDataFrame with dissolved polygons
dissolved = gpd.GeoDataFrame(geometry=gpd.GeoSeries(neighboring))


output_shapefile = '/Users/kawuli/Desktop/Forest_Data/Forest_Data/樹種界区_PairwiseDissol_Dissolve_D.shp'
# 新しいGeoDataFrameをシェイプファイルとして保存
dissolved.to_file(output_shapefile)


# Plot the dissolved polygons or save them to a new file
dissolved.plot()
