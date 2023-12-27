import fiona
import numpy as np
import scipy.spatial as sp

def convex_hull_shp(shp_file):
    # shp ファイルを読み込みます。
    with fiona.open(shp_file, "r") as shp:
        features = shp.read()

    # 点集合を抽出します。
    points = []
    for feature in features:
        points.append(feature["geometry"]["coordinates"])

    # 凸包を計算します。
    hull = sp.ConvexHull(points)

    # 凸包の頂点を表示します。
    print(hull.vertices)


if __name__ == "__main__":
    shp_file = "point_shp.shp"
    convex_hull_shp(shp_file)
