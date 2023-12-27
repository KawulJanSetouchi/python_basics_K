import geopandas as gpd

# ポリゴンのリストを作成します。
# #data = gpd.read_file('/Users/kawuli/Desktop/Forest_Data/Forest_Data/樹種界区_PairwiseDissolveAll.shp')
polygons = gpd.read_file("/Users/kawuli/Desktop/Forest_Data/Forest_Data/mergepolygon.shp")


# 各ポリゴンの名前とIDを取得します。
polygon_names = polygons["林相名"]
polygon_ids = polygons["林相ID"]

# 各ポリゴンについて、名前とIDが一致する最も近い隣接するポリゴンを検索します。
for i in range(len(polygons)):
    # 現在のポリゴンの名前とIDを取得します。
    curr_name = polygon_names[i]
    curr_id = polygon_ids[i]

    # 現在のポリゴンと最も近い隣接するポリゴンを検索します。
    closest_neighbor = polygons[polygons["林相名"] == curr_name]
    closest_neighbor = closest_neighbor[closest_neighbor["林相ID"] != curr_id]
    closest_neighbor = closest_neighbor.iloc[0]

    # 隣接するポリゴンが見つかった場合、両方のポリゴンを結合します。
    if closest_neighbor is not None:
        polygons = polygons.append(polygons.loc[i] | polygons.loc[closest_neighbor.index])
        polygons = polygons.drop(i)
        polygons = polygons.drop(closest_neighbor.index)

# 結合されたポリゴンのリストを作成します。
combined_polygons = polygons
print(polygons)