import numpy as np
import random
import matplotlib.pyplot as plt

from scipy.spatial import ConvexHull

points = np.random.rand(100,2)

hull = ConvexHull(points)

plt.plot(points[:,0], points[:,1], 'o',color='c')

for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'r')

plt.plot(points[hull.vertices,0], points[hull.vertices,1], 'r', lw=-1)
plt.plot(points[hull.vertices[0],0], points[hull.vertices[0],1], 'r-')
plt.show()
