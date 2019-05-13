import pandas as pd
import numpy as np
from astarwars_clustering.utils import utility
from astarwars_clustering.clustering import structural_clustering

FILEPATH = '/home/vincenzo/PycharmProjects/AGIW_First_Project/datasets/blackwells.csv'
df = pd.read_csv(FILEPATH,nrows=4000)
print("No. of rows and columns")
print("-----------------------")
print(df.shape)

featureMat=structural_clustering.createFeatureMatrix(df['src'])
clusters=structural_clustering.structural_clustering(bandwidth=0.07,featurematrix=featureMat)
labels=clusters.labels_
print (np.unique(labels))

nclusters=len(clusters.cluster_centers_)
df['predicted_labels']=labels
selectedelementsproducts=utility.count_occurrences(labels, 0)
selectedelementcatalog=utility.count_occurrences(labels,1)
truepositivecatalog=0
truepositiveproduct=0
allpositivesproduct=len(df[df['label'] == 'product'])
allpositivecatalog=len(df[df['label'] == 'list'])
for index, row in df.iterrows():
	if row['label'] == 'product' and row['predicted_labels'] == 0:
		truepositiveproduct += 1
	if row['label'] == 'list' and row['predicted_labels'] == 1:
		truepositivecatalog += 1


fmt_string='{} is {}'
print(fmt_string.format('Recall', truepositiveproduct / allpositivesproduct))
print(fmt_string.format('Precision', truepositiveproduct / selectedelementsproducts))

print(fmt_string.format('Recall', truepositivecatalog / allpositivecatalog))
print(fmt_string.format('Precision', truepositivecatalog / selectedelementcatalog))