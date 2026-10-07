import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	T=np.array(T)
	A=np.array(A)
	S=np.array(S)
	if np.linalg.det(A)!=0 and np.linalg.det(S)!=0:
		T_inv=np.linalg.inv(T)	
		N=np.dot(T_inv,A)
		transformed_matrix=np.dot(N,S)
		return transformed_matrix
	return -1	