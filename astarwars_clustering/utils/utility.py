import numpy as np

def pad_vector(vec, n):
    for i in range(n):
        vec.append(0)

def pad_matrix_elem(matrix, lastvec):
    maxlen=len(lastvec)
    matrixlen=len(matrix)
    for i in range(matrixlen):
        elem_topad=maxlen-len(matrix[i])
        pad_vector(matrix[i], elem_topad)

#cluster di cataloghi e di prodotti
def count_occurrences(vec,n):
	occ=0
	for el in vec:
		if el==n:
			occ=occ+1
	return occ

