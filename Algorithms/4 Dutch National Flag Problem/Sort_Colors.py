""" sort_012 method:
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
      input_list(list): Input array to be sorted.
      
    Returns:
      input_list(list): The same input after sorting.
"""
def sort_012(input_list):
    # edge case, null value
    if input_list is None:
        return None
    
    #edge case, list is empty or has 1 value, return the same list
    if len(input_list) < 2:
        return input_list
    
    # creating 3 pointers to point to where zeroes, ones and twos should be
    zeros, ones, twos = 0, 0, len(input_list)-1
    
    # loop until the numbers are sorted in their correct place
    while ones <= twos:
        # if the number at a ones index is a zero
        if input_list[ones] == 0:
            # swap it with the current zero index
            input_list[zeros], input_list[ones] = input_list[ones], input_list[zeros]
            # increment the pointers
            zeros += 1
            ones += 1
        
        # otherwise, if the number at a ones index is a one
        elif input_list[ones] == 1:
            # simply increment the ones pointer
            ones += 1
        
        # otherwise, we know it's a two
        else:
            # swap it with the current two index
            input_list[ones], input_list[twos] = input_list[twos], input_list[ones]
            # decrement the twos pointer
            twos -= 1
    
    # after the loop, the list will be sorted so we return it
    return input_list
