
from collections import Counter

def confusion_matrix(data):
	# Implement the function here
	tp=0
	tn=0
	fp=0
	fn=0
	for i in data:
		if i[0]==1 and i[1]==1:
			tp+=1
		elif i[0]==1 and i[1]==0:
			fn+=1
		elif i[0]==0 and i[1]==1:
			fp+=1
		else:
			tn+=1
	return [[tp,fn],[fp,tn]]			
	pass
