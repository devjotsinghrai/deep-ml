import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	l=new_shape[0]*new_shape[1]
	if len(a[0])*len(a)==l:
		a=np.array(a)
		a.shape=new_shape
		return a
	return []	
	#return reshaped_matrix