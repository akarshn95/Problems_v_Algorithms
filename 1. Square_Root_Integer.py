def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number==0 or number==1:
        return number
    
    start=1
    end=number

    while start<=end:
        mid=(start+end)//2
        if mid*mid==number:
            return mid
        elif mid*mid<number:
            start=mid+1
            sqrt=mid
        else:
            end=mid-1
    
    return sqrt


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (100 == sqrt(10000)) else "Fail")
