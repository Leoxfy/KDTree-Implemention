from sklearn.neighbors import KDTree

import numpy as np
rng = np.random.RandomState(0)
X = rng.random_sample((10, 3))  # 10 points in 3 dimensions
tree = KDTree(X, leaf_size=2)              # doctest: +SKIP
dist, ind = tree.query(X[:1], k=3)                # doctest: +SKIP
print(ind)  # indices of 3 closest neighbors
print(dist)  # distances to 3 closest neighbors
