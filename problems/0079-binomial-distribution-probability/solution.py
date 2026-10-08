import math
def fact(n):
    if n<=1:
        return 1
    else:
        return fact(n-1)*n            
def binomial_probability(n: int, k: int, p: float) -> float:
    """
    Calculate the probability of exactly k successes in n Bernoulli trials.
    
    Args:
        n: Total number of trials
        k: Number of successes
        p: Probability of success on each trial
    
    Returns:
        Probability of k successes
    """
    # Your code here
    num=fact(n)
    denom=fact(n-k)*fact(k)
    q=1-p
    val=num/denom*math.pow(p,k)*math.pow(q,n-k)
    return val

    pass