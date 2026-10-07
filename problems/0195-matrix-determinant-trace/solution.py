def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	import numpy as np
	"""
	Compute the determinant and trace of a square matrix.
	
	Args:
		matrix: A square matrix (n x n) represented as list of lists
	
	Returns:
		Tuple of (determinant, trace)
	"""
	# Your code here
	det=np.linalg.det(matrix)
	trace=0
	for i in range(0,len(matrix)):
		for j in range(0,len(matrix[0])):
			if i==j:
				trace+=matrix[i][j]
	return (det,trace)
	pass