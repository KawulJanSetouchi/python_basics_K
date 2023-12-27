import geopandas as gpd
from shapely.ops import unary_union

# GeoPandasでデータを読み込む
data = gpd.read_file('path/to/your/shapefile.shp')

# 小班ごとに処理を行う
for small_unit_id in data['small_unit_id'].unique():  # 小班の識別子に基づいてループします
    unit_data = data[data['small_unit_id'] == small_unit_id]  # 特定の小班のデータを取得します

    # 面積が600㎡未満のポリゴンを取得します
    small_polygons = unit_data[unit_data['area'] < 600]

    # 隣接しているポリゴンを見つけて結合します
    for index, small_polygon in small_polygons.iterrows():
        adjacent_polygons = []
        for index, polygon in unit_data.iterrows():
            if polygon.geometry.touches(small_polygon.geometry) or polygon.geometry.intersects(small_polygon.geometry):
                adjacent_polygons.append(polygon.geometry)

        if adjacent_polygons:
            adjacent_polygons.append(small_polygon.geometry)
            union_result = unary_union(adjacent_polygons)

            # 結合した結果を元のデータに反映させるなどの処理を行います
