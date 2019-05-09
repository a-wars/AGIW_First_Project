from feature_generator import features
from feature_generator import utility
from sklearn.cluster import MeanShift
import numpy as np
import pandas as pd

#cluster di cataloghi e di prodotti
def count_occurrences(vec,n):
	occ=0
	for el in vec:
		if el==n:
			occ=occ+1
	return occ


matrix=[]
vectorizer=features.TagFrequency()

df=pd.read_csv('/home/vincenzo/PycharmProjects/AGIW_First_Project/dataset/bookrepository.csv',nrows=1000)
fmt_string = 'There are {} row with {} label'
print(fmt_string.format(len(df[df['label'].isnull()]),'no'))
print(fmt_string.format(len(df[df['label']=='product']), 'product'))

X=df['src']
last_vec=None

for doc in X:
	feature_vec=vectorizer(doc)
	matrix.append(feature_vec)
	last_vec=feature_vec


print('lunghezza matrice:'+str(len(matrix))+'\n')
utility.pad_matrix_elem(matrix, last_vec)

numpymatrix=np.array(matrix)
clustering = MeanShift(bandwidth=0.1).fit(numpymatrix)
labels=clustering.labels_
print(labels)

df['predicted_labels'] = labels

nclusters=len(clustering.cluster_centers_)
selectedelements=count_occurrences(labels,0)
truepositive=0
allpositives=len(df[df['label']=='product'])
for index, row in df.iterrows():
	if row['label']=='product' and row['predicted_labels']==0:
		truepositive+=1

fmt_string='{} is {}'
print(fmt_string.format('Recall', truepositive/allpositives))
print(fmt_string.format('Precision', truepositive/selectedelements))