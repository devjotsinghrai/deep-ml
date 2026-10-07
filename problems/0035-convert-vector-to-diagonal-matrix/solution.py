import numpy as np

def make_diagonal(x):
	# Your code here
	diag=np.zeros((len(x),len(x)))
	for i in range(0,len(diag)):
		for j in range(0,len(diag[0])):
			if i==j:
				diag[i][j]=x[i]
				break
	return diag			

	pass