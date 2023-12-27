import geopandas as gpd

# Shapefileを読み込む
data = gpd.read_file('/Users/kawuli/Desktop/Forest_Data/Forest_Data/樹種界区_PairwiseDissolveAll.shp')

name =data['林相名' ]
print(name)

same_id =data['林相名' ]
print(same_id)

# 同じ名前またはIDで最も近い隣接ポリゴンにディゾルブする関数
def dissolve_to_nearest_neighbor(df):
    # 同じ名前またはIDでポリゴンを結合
    joined = gpd.sjoin(df, df, how='inner', op='intersects')

    # 同じ名前またはIDを持つ結合されたフィーチャのみを保持
    same_id = joined[joined['林相名_left'] == joined['林相名_right']]

    # 最も近い隣接ポリゴンにディゾルブ
    dissolved = same_id.dissolve(by='林相名_left')

    return dissolved


# 同じ名前またはIDで最も近い隣接ポリゴンにディゾルブ
dissolved_data = dissolve_to_nearest_neighbor(data)

# ディゾルブされたshapefileを保存
dissolved_data.to_file('ディゾルブされたshapefile.shp')
