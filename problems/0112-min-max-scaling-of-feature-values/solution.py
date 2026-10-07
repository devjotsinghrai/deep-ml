def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    # Your code here
    mini=min(x)
    maxi=max(x)
    denom=maxi-mini
    new=[]
    for i in x:
        n=(i-mini)/denom
        new.append(n)
    return new
