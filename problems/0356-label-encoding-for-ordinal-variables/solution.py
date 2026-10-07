def label_encode_ordinal(values: list, order: list) -> list:
    """
    Encode ordinal categorical values to integers based on specified order.
    
    Args:
        values: List of categorical values to encode
        order: List specifying the order of categories from lowest (0) to highest
    
    Returns:
        List of integers representing the encoded values
    """
    encoded=[]
    for i in  range(0,len(values)):
        for j in range(0,len(order)):
            if values[i]==order[j]:
                encoded.append(j)
                break
    value=set(values)
    order=set(order)   
    left=value.difference(order)
    for k in range(0,len(values)):
        if values[k] in left:
            encoded.insert(k,-1)           
    return encoded
    