from astarwars_clustering.clustering import features
from astarwars_clustering.utils import utility
from sklearn.cluster import MeanShift, estimate_bandwidth, DBSCAN
import numpy as np
import pandas as pd
import time as time


# clustering algorithm
# It takes as input a Pandas Series containing html source code and a hyperparameter for mean shift clustering algorithm called bandwith


def meanshiftclustering(bandwidth, featurematrix):
    start = time.time()
    clustering = MeanShift(bandwidth=bandwidth).fit(featurematrix)
    end = time.time()
    hours, rem = divmod(end - start, 3600)
    minutes, seconds = divmod(rem, 60)
    print("Elapsed time to calculate MeanShift clustering:{:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds))
    return clustering


def dbscanclustering(featurematrix):
    start = time.time()
    clustering =DBSCAN(min_samples=20, eps=0.1).fit(featurematrix)
    end = time.time()
    hours, rem = divmod(end - start, 3600)
    minutes, seconds = divmod(rem, 60)
    print("Elapsed time to calculate DBSCAN clustering:{:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds))
    return clustering


def createFeatureMatrix(listOfHtmls):
    start = time.time()

    matrix = []
    vectorizer = features.TagFrequency()
    last_vec = None
    for _, doc in listOfHtmls.iteritems():
        feature_vec = vectorizer(doc)
        matrix.append(feature_vec)
        last_vec = feature_vec
    utility.pad_matrix_elem(matrix, last_vec)

    end = time.time()
    hours, rem = divmod(end - start, 3600)
    minutes, seconds = divmod(rem, 60)
    print("Elapsed time to calculate features:{:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds))
    return matrix


def calculatePrecision(truepositive, selectedelements):
    return truepositive / selectedelements


def calculateRecall(truepositive,allpositive):
	return truepositive/allpositive

def calculateF1Score(recall,precision):
	return 2*((recall*precision)/(recall+precision))

