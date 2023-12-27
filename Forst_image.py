from skimage import io
import matplotlib.pyplot as plt
from tifffile import TiffFile
import numpy as np



path = "C:/Users/kawuli/Desktop/Forest_Data/03_航空写真/04ib3614.tif" # パスを格納
img = io.imread(path) # これでOK
img.shape # 形の確認


with TiffFile(path) as tif:
    img = tif.asarray()
plt.imshow(img) # 画像の表示



from tifffile import imwrite
imwrite("C:/Users/kawuli/Desktop/Forest_Data/03_航空写真/kawwww.tif", img) # 保存完了


with TiffFile(path) as tif:
    mmap = tif.asarray(out="memmap") # out="memmap"でメモリマップを返してくれる
# 形や型の確認はメモリマップでもできる
print(mmap.shape)
print(mmap.dtype)


img = np.asarray(mmap) # もちろんすぐに変換してはメモリマップの意味がない！


# メモリマップを取得
with TiffFile(path) as tif:
    mmap = tif.asarray(out="memmap")

# 1枚目を表示
img0 = np.asarray(mmap[0])
plt.imshow(img0)
