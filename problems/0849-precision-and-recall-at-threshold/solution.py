import numpy as np

def precision_recall_at_threshold(y_true, y_scores, threshold):
    """
    Compute precision and recall at a given decision threshold.

    Args:
        y_true: list/array of true binary labels (0 or 1)
        y_scores: list/array of predicted scores in [0, 1]
        threshold: float, classification threshold (predict positive if score >= threshold)

    Returns:
        [precision, recall] as a list of two floats rounded to 4 decimals.
    """
    # Your code here
    for i in  range(len(y_scores)):
        if y_scores[i]>=threshold:
            y_scores[i]=1
        else:
            y_scores[i]=0
    tp=0
    fp=0
    fn=0        
    for i in range(len(y_true)):
        if y_scores[i]==1 and y_true[i]==1:
            tp+=1
        elif y_scores[i]==0 and y_true[i]==1:
            fn+=1
        elif y_scores[i]==1 and y_true[i]==0:
            fp+=1
    if tp==0:
        return [0,0]        
    precison=tp/(tp+fp)
    recall=tp/(tp+fn)  
    return [precison,recall]              


    pass
