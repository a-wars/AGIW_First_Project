from astarwars_clustering.clustering import features
from astarwars_clustering.utils import utility
from sklearn.cluster import MeanShift,estimate_bandwidth
import numpy as np
import pandas as pd

#clustering algorithm
#It takes as input a Pandas Series containing html source code and a hyperparameter for mean shift clustering algorithm called bandwith
def structural_clustering(bandwidth,featurematrix):
	
	clustering = MeanShift(bandwidth=bandwidth).fit(featurematrix)

	return clustering


def createFeatureMatrix(listOfHtmls):
	matrix = []
	vectorizer = features.TagFrequency()
	last_vec = None
	for _, doc in listOfHtmls.iteritems():
		feature_vec = vectorizer(doc)
		matrix.append(feature_vec)
		last_vec = feature_vec
	utility.pad_matrix_elem(matrix, last_vec)
	return matrix
