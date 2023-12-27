import alphashape
import numpy as np
from descartes import PolygonPatch
from matplotlib import pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_blobs

X, y = make_blobs(n_samples=1000, centers=3, n_features=2, random_state=0, cluster_std=0.3)
plt.scatter(X[:, 0], X[:, 1], c=y)

# Fitting Clustering
c_alg = DBSCAN()
c_alg.fit(X)
labels = c_alg.labels_

fig, ax = plt.subplots()
for i in range(0, max(labels) + 1):
    ind = np.where(labels == i)
    points = X[ind, :][0, :, :]

    alpha_shape = alphashape.alphashape(points, 5.0)
    ax.scatter(*zip(*points))
    ax.add_patch(PolygonPatch(alpha_shape, alpha=0.5))

plt.show()
