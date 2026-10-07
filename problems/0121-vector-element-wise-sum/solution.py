def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	# Return the element-wise sum of vectors 'a' and 'b'.
	# If vectors have different lengths, return -1.
	import numpy as np
	a=np.array(a)
	b=np.array(b)
	if len(a)==len(b):
		return  a+b
	return -1	
	pass