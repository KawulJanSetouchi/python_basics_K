import fiona
import numpy as np
import scipy.spatial as sp

# SHP ファイルを読み込みます。
with fiona.open("points.shp", "r") as shp:
    features = shp.read()

# 同じ名前、同じ ID の点集合を取得します。
points = []
for feature in features:
    if feature["properties"]["name"] == "point" and feature["properties"]["id"] == 1:
        points.append((feature["geometry"]["coordinates"][0], feature["geometry"]["coordinates"][1]))

# 凸包を計算します。
hull = sp.ConvexHull(points)

# 凸包の頂点を表示します。
print(hull.vertices)
