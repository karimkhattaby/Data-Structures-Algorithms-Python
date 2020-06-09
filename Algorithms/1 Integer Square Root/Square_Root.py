""" sqrt method:
    Calculates the floored square root of integers.

    Args:
      number(int): number to find the floored square root for.
      
    Returns:
      square_root(int): the floored square root
"""
def sqrt(number):    
    # edge case, if the passed number is null or negative, we return -1
    # indicating that there is no square root
    if number < 0 or number is None:
        return -1
    # edge case, if the passed number is 0 or 1, we return the number
    if number < 2:
        return number
    
    # we do binary search using 2 pointers left (starts from 0) and right (starts from number)
    left, right = 0, number
    
    # we keep looping until the left pointer crosses the right one
    # which will be the case when a number isn't a perfect square
    while right >= left:
        # we calculate the middle number between the 2 pointers
        mid = left + (right-left)//2
        
        # if mid^2 is larger than our number, we need to move to the left of the current middle
        if mid**2 > number:
            right = mid - 1
        # if mid^2 is the original number, we found our result
        elif mid == number/mid:
            # so we return the middle value
            return mid
        # if mid^2 is less than our number, we need to move to the right of the current middle
        else:
            left = mid + 1
    
    # we will only exit the loop if the given number is not a perfect square
    # in that case we return the floor of the division
    return number//left
