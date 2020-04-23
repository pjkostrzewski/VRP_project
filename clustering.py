# k-means clustering
import numpy
from numpy import unique
from numpy import where
from sklearn.datasets import make_classification
from sklearn.cluster import KMeans
from matplotlib import pyplot
# define dataset
# X, _ = make_classification(n_samples=50, n_features=2, n_informative=2, n_redundant=0, n_clusters_per_class=1, random_state=4)
data = [
    [49, 49], [52, 64], [20, 26], [40, 30], [21, 47], [17, 63], [31, 62], [52, 33], [51, 21], [42, 41],
    [31, 32], [5, 25], [12, 42], [36, 16], [52, 41], [27, 23], [17, 33], [13, 13], [57, 58], [62, 42], [42, 57],
    [16, 57], [8, 52], [7, 38], [27, 68], [30, 48], [43, 67], [58, 48], [58, 27], [37, 69], [38, 46], [46, 10], [61, 33],
    [62, 63], [63, 69], [32, 22], [45, 35], [59, 15], [5, 6], [10, 17], [21, 10], [5, 64], [30, 15], [39, 10], [32, 39],
    [25, 32], [25, 55], [48, 28], [56, 37], [30, 40]]
# with open("eil51/eil51_points_only.txt") as f:
#     data = [x.split()[1:] for x in f.readlines()]
# print(data)
X=numpy.array([numpy.array(xi) for xi in data])
print(type(X))
print(X)
# define the model
model = KMeans(n_clusters=2)
# fit the model
model.fit(X)
# assign a cluster to each example
yhat = model.predict(X)
# retrieve unique clusters
clusters = unique(yhat)
# create scatter plot for samples from each cluster
for cluster in clusters:
	# get row indexes for samples with this cluster
	row_ix = where(yhat == cluster)
	# create scatter of these samples
	pyplot.scatter(X[row_ix, 0], X[row_ix, 1])
pyplot.scatter(37, 52)
# show the plot
pyplot.show()