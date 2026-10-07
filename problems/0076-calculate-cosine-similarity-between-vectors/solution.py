import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	v1=np.array(v1)
	v2=np.array(v2)
	m=0
	for i in v1:
		m+=i**2
	m=np.sqrt(m)
	n=0
	for j in v2:
		n+=j**2
	n=np.sqrt(n)	
	p=np.dot(v1,v2)
	q=m*n
	return p/q	
	pass