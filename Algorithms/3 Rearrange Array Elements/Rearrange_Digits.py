""" rearrange_digits method:
    Rearrange Array Elements in a way to form two numbers such that their sum is the maximum possible

    Args:
      input_list(list): Input array of individual digits
      
    Returns:
      1- numbers(list): a list of the 2 maximum sums
"""
def rearrange_digits(input_list):
    # edge case, if the given list is null or empty we return it
    if input_list is None:
        return [-1, -1]
    
    # if the given list has 2 elements or less, we return the same list
    if len(input_list) < 3:
        return input_list
    
    # STEP 1: sort the array using a helper function
    input_list = sort(input_list)

    # STEP 2: create a list of 2 lists (to store the 2 numbers) and initialize them to '0'
    answer = [['0'], ['0']]

    # STEP 3: loop through the sorted list,
    # add the first element to the first number, and add the second element to the second number
    # keep doing the same until you exhaust the list

    # loop through the sorted list
    for i in range(len(input_list)):
        # if the index is even, add the number to the first inner list as a string
        if i%2 == 0:
            answer[0].append(str(input_list[i]))
        # if the index is odd, add the number to the second inner list as a string
        else:
            answer[1].append(str(input_list[i]))
    
    # STEP 4: join the inner lists into strings and convert them into integers
    for i in range(len(answer)):
        answer[i] = int( ''.join(answer[i]) )
    
    # return the answer
    return answer

# helper function to sort a list. Just an implementation of merge sort
def sort(input_list):
    # base case, if the given list has 1 element, we return it
    if len(input_list) <= 1:
        return input_list
    
    # recursive case, if the list has more 1 element,
    # break it into 2 lists; left and right, and sort them...
    
    # so we create pointers: left, right, mid to help divide the list from the middle
    left, right = 0, len(input_list)
    mid = left + (right-left)//2
    
    # call the recursive function to sort the left half and the right half
    left = sort(input_list[left:mid])
    right = sort(input_list[mid:right])
    
    # sort the 2 lists and merge them back
    i = 0 # left list index
    j = 0 # right list index
    result = [] # list to store the result
    # loop through the elements of the lists and append the larger element to the result list
    while i < len(left) or j < len(right):
        # check if we reached the end of the left list
        if i == len(left):
            # append the right element to the result list and go next
            result.append(right[j])
            j+=1
            continue

        # check if we reached the end of the right list
        if j == len(right):
            # append the left element to the result list and go next
            result.append(left[i])
            i+=1
            continue

        # if the element of the left list is larger than the element of the right list
        if left[i] >= right[j]:
            # append the element of the left list to the result list
            result.append(left[i])
            # increment the index
            i+=1
        # otherwise, do the same to the right list
        else:
            result.append(right[j])
            j+=1
    
    # return the sorted array
    return result
