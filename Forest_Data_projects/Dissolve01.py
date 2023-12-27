#pip install geopandas shapely

import geopandas as gpd
from shapely.ops import unary_union

# ポリゴンシェイプファイルの読み込み
input_shapefile = 'path/to/input/polygons.shp'
output_shapefile = 'path/to/output/polygons_dissolved.shp'

# GeoDataFrameとしてデータを読み込む
gdf = gpd.read_file(input_shapefile)

# 面積が600平方メートル未満のポリゴンを抽出
small_polygons = gdf[gdf.area < 600]

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
gdf.to_file(output_shapefile)
