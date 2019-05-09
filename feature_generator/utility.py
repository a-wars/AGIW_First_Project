import numpy as np
from pymongo import MongoClient

def pad_vector(vec, n):
    return np.pad(vec, (0, n), 'constant')

def pad_matrix_elem(matrix, lastvec):
    maxlen=len(lastvec)
    matrixlen=len(matrix)
    for i in range(matrixlen):
        elem_topad=maxlen-len(matrix[i])
        matrix[i]=pad_vector(matrix[i], elem_topad)

def get_db():
    client=MongoClient('172.17.0.2',27017)
    db = client.ProductFinderCrawlerData
    return db


def get_collection(collection_name):
	try:
		db=get_db()
		return db[collection_name]
	except:
		return None
