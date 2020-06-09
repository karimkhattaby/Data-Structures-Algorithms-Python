""" get_min_max method:
    Given an unsorted input array, find the minimum and maximum values.

    Args:
      input_list(list): Input array to be checked.
      
    Returns:
      min,max (tuple): the minimum and maximum values.
"""
def get_min_max(ints):
    # edge case, null value or empty list
    if ints is None or ints == []:
       return (None, None)

    # edge case, single value list
    if len(ints) < 2:
        return (ints[0], ints[0])
    
    # assign first value as the min and max
    min_value = ints[0]
    max_value = ints[0]

    # loop through the list
    for i in range(len(ints)):
        # if the current value is greater than the max
        if ints[i] > max_value:
            # update the max value
            max_value = ints[i]
        # if the current value is less than the min
        if ints[i] < min_value:
            # update the min value
            min_value = ints[i]
    
    # return the min and max values
    return (min_value, max_value)
