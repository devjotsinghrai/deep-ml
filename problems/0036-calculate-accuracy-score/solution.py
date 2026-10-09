import numpy as np

def accuracy_score(y_true, y_pred):
	# Your code here
	new=np.equal(y_pred,y_true)
	c=0
	for i in new:
		if i==True:
			c+=1
	return c/len(y_pred)		
	pass