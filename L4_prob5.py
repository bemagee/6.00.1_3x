#!/c/python27/python

def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
    - lo, when x < lo
    - hi, when x > hi
    - x, otherwise
    '''
    return max(min(hi,x),lo)

lo=10
x=15
hi=20
low = clip(lo,x,hi)
print low
