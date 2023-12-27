import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import DBSCAN
from scipy.spatial import ConvexHull, convex_hull_plot_2d

X, y = make_blobs(n_samples=100, centers=3, n_features=2, random_state=0, cluster_std=0.3)
plt.scatter(X[:,0], X[:,1], c=y)


# Fitting Clustering
c_alg = DBSCAN()
c_alg.fit(X)
labels = c_alg.labels_

for i in range(0, max(labels)+1):
    ind = np.where(labels == i)

    segment = X[ind, :][0]
    hull = ConvexHull(segment)

    plt.plot(segment[:, 0], segment[:, 1], 'o')
    for simplex in hull.simplices:
        plt.plot(segment[simplex, 0], segment[simplex, 1], 'k-')


plt.show()



