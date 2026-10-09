
import numpy as np

def r_squared(y_true, y_pred):
	# Write your code here
	sst=np.var(y_true)*len(y_true)
	ssr=0
	new=y_pred-y_true
	for i in new:
		ssr+=i**2
	return 1-(ssr/sst)


	pass
