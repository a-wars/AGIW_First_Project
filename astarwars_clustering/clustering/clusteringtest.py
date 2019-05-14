import pandas as pd
import numpy as np
from astarwars_clustering.clustering import clusteringevaluation
from astarwars_clustering.clustering import structural_clustering
from astarwars_clustering.utils import utility

FILEPATH = '/home/vincenzo/PycharmProjects/AGIW_First_Project/datasets/bookswagon.csv'
df = pd.read_csv(FILEPATH,nrows=500)
print("No. of rows and columns")
print("-----------------------")
print(df.shape)

featureMat = structural_clustering.createFeatureMatrix(df['src'])
msclustering = structural_clustering.meanshiftclustering(bandwidth=0.1, featurematrix=featureMat)
dbscanclustering = structural_clustering.dbscanclustering(featurematrix=featureMat)
mslabels = msclustering.labels_
msclusters = np.unique(mslabels)

dbscanlabels = dbscanclustering.labels_
dbscanclusters = np.unique(dbscanlabels)

for label in msclusters:
	print (utility.count_occurrences(mslabels,label))
print('\n')

for label in dbscanclusters:
	print (utility.count_occurrences(dbscanlabels,label))

'''
print('Metriche per MeanShift')
p1, r1 = clusteringevaluation.calculate_precision_and_recall(df,msclustering,'product',0)
p2, r2 = clusteringevaluation.calculate_precision_and_recall(df,msclustering,'list',1)
'''
print('Metriche per DBSCAN')
p4, r4 = clusteringevaluation.calculate_precision_and_recall(df, dbscanclustering, 'product', 1)
p5, r5 = clusteringevaluation.calculate_precision_and_recall(df, dbscanclustering, selectedlabel='list', predictedlabel=2)
