""" rotated_array_search method:
    Finds the index of a value by searching a rotated sorted array.

    Args:
      1- input_list(list): Input array to be searched
      2- number(int): the target number we're searching for
      
    Returns:
      index(int): the index of the value
      OR -1 if no index was found
"""
def rotated_array_search(input_list, number):
    # edge case, null list or value to search for
    if input_list is None or number is None:
        return -1
    # edge case, empty list
    if len(input_list) < 1:
        return -1
    # edge case, list with 1 element
    if len(input_list) == 1:
        return 0 if number==input_list[0] else -1

    # we do binary search using 2 pointers
    # left (starts from 0) and right (starts from last index)
    left, right = 0, len(input_list)-1

    # we find the index from which rotation gets reset
    rotation_index = find_rotation_index(input_list)

    # if the target is between the rotation index and the right
    # then we need to search in that range
    if input_list[rotation_index] <= number <= input_list[right]:
        left = rotation_index
    # otherwise we need to search in the other part of the array
    else:
        right = rotation_index

    ### we do binary search over the chosen interval...
    # we loop until the left pointer crosses the right one
    while left <= right:
        # we calculate the middle index between the 2 pointers
        mid = left + (right-left)//2

        # if the number in the middle is our target, return the index
        if number == input_list[mid]:
            return mid
        
        # if the number is less than the middle, move left
        if number < input_list[mid]:
            right = mid - 1
        # if the number is higher than the middle, move right
        else:
            left = mid + 1
        
    # if we reached this point, it means we didn't find our target, so we return -1
    return -1

#helper function to find the rotation index
def find_rotation_index(input_list):
    # we do binary search using 2 pointers
    # left (starts from 0) and right (starts from last index)
    left, right = 0, len(input_list)-1

    # we keep looping until the left pointer crosses the right one
    while left < right:
        # calculate the middle index between the 2 pointers
        mid = left + (right-left)//2

        # if the middle element is larger than the right element
        if input_list[mid] > input_list[right]:
            # it means the rotation index will be on our right
            left = mid + 1
        # else
        else:
            # the rotation index will be on our left
            right = mid
    
    # when right exceeds left, the rotation index is left
    return left
