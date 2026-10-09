
import numpy as np

def rmse(y_true, y_pred):
	# Write your code here
	r=y_true-y_pred
	r=r**2
	rmse_res=np.mean(r)
	final=np.sqrt(rmse_res)
	return round(final,3)
