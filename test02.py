#'/Users/kawuli/Desktop/Forest_Data/Forest_Data/樹種界区_PairwiseDissol_Dissolve_D.shp'

import geodatasets
import geopandas as gpd
from shapely import unary_union

# Load your GeoDataFrame (replace 'your_data.shp' with your file path)
gdf = gpd.read_file('/Users/kawuli/Desktop/Forest_Data/Forest_Data/樹種界区_PairwiseDissol_Dissolve_D.shp')
output_shapefile = '/Users/kawuli/Desktop/Forest_Data/Forest_Data/樹種界区_PairwiseDissol_D.shp'



t = gdf.geometry.explore()
print(t)

#print(gdf.head())
select_column =gdf['MIN_Shape_']
#print(select_column)

select_row=gdf[gdf['MIN_Shape_']<600]
#print(select_row)


small_polygons =gdf[gdf['MIN_Shape_']<600]
# 面積が600平方メートル未満のポリゴンを含む隣接する最大のポリゴンを見つけ、統合する
for index, small_polygon in small_polygons.iterrows():
    # 面積が600平方メートル未満のポリゴンと隣接する最大のポリゴンを抽出
    neighbors = gdf[~gdf.geometry.touches(small_polygon.geometry)]
    max_neighbor = neighbors.iloc[neighbors.area.idxmax()]

    # 隣接する最大のポリゴンと面積が600平方メートル未満のポリゴンを統合
    dissolved_geometry = unary_union([small_polygon.geometry, max_neighbor.geometry])

    # 統合されたポリゴンで元のGeoDataFrameを更新
    gdf = gdf.drop([index, max_neighbor.name])
    gdf = gdf.append({'geometry': dissolved_geometry}, ignore_index=True)

# 新しいGeoDataFrameをシェイプファイルとして保存
new_data=gdf.to_file(output_shapefile)