import matplotlib.pyplot as plt
from shapely.geometry import MultiLineString
from shapely.ops import bezier_curve
import shapely  # .shpファイルを読み込むためのライブラリ


def read_shapefile(shapefile_path):
    # shapefile.Readerを使用して.shpファイルを読み込む
    shape = shapely.Reader(shapefile_path)

    # ジオメトリを取得し、MultiLineStringとして扱う
    lines = []
    for sr in shape.shapeRecords():
        line = sr.shape.__geo_interface__['coordinates']
        lines.append(line)

    return MultiLineString(lines)


def convert_to_bezier(line_geometry):
    # shapelyのbezier_curve関数を使用して、ジオメトリをベジェ曲線に変換する
    return bezier_curve(line_geometry)


def plot_bezier(bezier_curve_geometry):
    # プロットするための設定
    fig, ax = plt.subplots()

    # ベジェ曲線をプロットする
    for curve in bezier_curve_geometry:
        x, y = curve.xy
        ax.plot(x, y, '-o', label='Bezier Curve')

    # グラフの表示
    ax.legend()
    plt.show()


if __name__ == "__main__":
    # .shpファイルからジオメトリを読み取る
    shapefile_path = "path/to/your_shapefile.shp"  # 自分の.shpファイルのパスに置き換える
    geometry = read_shapefile(shapefile_path)

    # ジオメトリをベジェ曲線に変換する
    bezier_curve_geometry = convert_to_bezier(geometry)

    # ベジェ曲線をプロットする
    plot_bezier(bezier_curve_geometry)
