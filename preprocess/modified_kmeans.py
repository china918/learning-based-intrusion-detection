#!/usr/bin/env python3
# this is a example for modified k-means preprocess.
import numpy as np
# define distance measure between 2 points
def new_dist(a, b):
	return np.linalg.norm(a - b)
# an example of dataset
dataset = np.array([ [ 2, 10, 9 ], [ 2, 5, 8 ], [ 5, 3, 9 ], [ 5, 0, 9 ], [ 1, 8, 10 ], \
 [ 3, 9, 10 ], [ 2, 9, 9 ], [ 8, 7, 5 ], [ 1, 5, 10 ], [ 3, 6, 9 ], [ 5, 2, 0 ], \
 [ 2, 8, 6 ], [ 0, 10, 2 ], [ 3, 0, 0 ], [ 7, 4, 4 ] ])
# select first centroid
seed = 0
# select distance threshold
threshold = 5
# initialize centroid set
centroid = [dataset[0]]
# initialize cluster sets
clusters = [[]]
# construct centroid set
for i in range(len(dataset)):
	dists = [new_dist(dataset[i], pp) for pp in centroid]
	# it's possible there is multiple minima, we choose the first one
	idx = dists.index(min(dists))
	# if falls in some cluster
	if min(dists) <= threshold:
		clusters[idx].append(dataset[i])
	# if not in any exist cluster, construct a new cluster
	else:
		centroid.append(dataset[i])
		clusters.append([ dataset[i] ])
# print
print(centroid)
print(clusters)
