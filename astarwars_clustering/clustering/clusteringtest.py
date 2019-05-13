import pandas as pd
import numpy as np
from astarwars_clustering.utils import utility
from astarwars_clustering.clustering import structural_clustering

FILEPATH = '/home/vincenzo/PycharmProjects/AGIW_First_Project/dataset/bookdepository.csv'
df = pd.read_csv(FILEPATH,nrows=1000)
print("No. of rows and columns")
print("-----------------------")
print(df.shape)


clusters=structural_clustering.structural_clustering(df['src'])
labels=clusters.labels_
print (np.unique(labels))

nclusters=len(clusters.cluster_centers_)
selectedelements=utility.count_occurrences(labels, 0)
truepositive=0
allpositives=len(df[df['label']=='product'])
for index, row in df.iterrows():
	if row['label']=='product' and row['predicted_labels']==0:
		truepositive+=1

fmt_string='{} is {}'
print(fmt_string.format('Recall', truepositive/allpositives))
print(fmt_string.format('Precision', truepositive/selectedelements))