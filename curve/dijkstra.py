
#  Pythonの導入

# L = [1, 'suzuki', 3.14, True]
# print(L[1])
# L[2] =3.1415
# print(L[2])
#
# s =[]
# print(len(s))
#
# L.append('Eiji')
# print(L)
#
# v = [i for i in range(1,20) if i % 2==0]
# print(v)

# 関数
# def prod_expo(x,y):
#     prod =x * y
#     expo =x ** y
#     return prod, expo
# print(prod_expo(2,3))

# for文・while文
# year ='B4'
# if year =='B4':
#     print('ALim','Samat','Gulnur','aynur')
# elif year == 'M1':
#     print("aytaji", 'ziba', 'aykiz', 'Yusufjan')
# elif year == 'M2':
#     print('Maysam', 'kasim','ali','sali')
# else:
#     print("Try again ... ")
#

    # for文・while文・if文：演習

# method = 0
# if method ==0:
#     for i in range(1,10):
#         for j in range(1,10):
#             print(i*j, end=' ')
# elif method ==1:
#     result =[]
#     while (len(result) <= 9):
#         prod =1
#         for i in range(1,10):
#             prod *=1
#         result.append(prod)
#     print(result)
# else:
#     print(' Its wrong ! Try again pls... ')


#  NumPy（ndarray）
#import numpy as np
#
# # ndarrayの生成
#
# a =np.full(10,5)
# b = np.zeros(10).astype(int)
# print(a)
# print(b)
#
# list1 = [9,2,5,4,7,1,3,6]
# c =np.array(list1)
# print(c)
#
# # 2次元配列
#
# list2 =[[1,3,4],[5,7,2],[9,3,6]]
# d = np.array(list2)
# print(d)
#
# print('GHHGHFHGFGGDJHFJDFDGDGF')
# print(d[:,2])
#
# print(np.argmin(c))
# print(c[np.where(c>=5)])
#
# print(c[np.where((c>=5) & (c<=8))])

# NumPy（CSVファイルの読み込み）
import numpy as np

a = np.loadtxt('/Users/kawuli/Desktop/Big-Folder/data/Tesla.csv', delimiter=',',skiprows=1, dtype=str)
print(a)

# using loadtxt()
# arr = np.loadtxt("/Users/kawuli/Desktop/Big-Folder/data/Tesla.csv",
#                  delimiter=",", dtype=str)
# print(arr)

# 始点・終点・計算法の指定
s=80
t = 1148

method =1
