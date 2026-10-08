import math

def sigmoid(z: float) -> float:
	#Your code here
	denom=1+math.exp(-z)
	result=1/denom
	return result