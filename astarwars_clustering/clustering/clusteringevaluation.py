import pandas as pd
import sklearn
from astarwars_clustering.utils import utility


#predictedlabel rappresenta l'etichetta del clustering su cui vogliamo calcolare precision e recall
def calculate_precision_and_recall(df, clustering, selectedlabel, predictedlabel):

	labels=clustering.labels_
	df['predicted_labels'] = labels
	selectedelements=utility.count_occurrences(labels,predictedlabel)
	print('Predicted products:{}',selectedelements)

	truepositive = 0
	allpositives = len(df[df['label'] == selectedlabel])

	for index, row in df.iterrows():
		if row['label'] == selectedlabel and row['predicted_labels'] == predictedlabel:
			truepositive += 1

	fmt_string='{} is {}'
	recall = truepositive/allpositives
	precision = truepositive/selectedelements

	print(fmt_string.format('Recall', recall))
	print(fmt_string.format('Precision', precision))

	return precision, recall
