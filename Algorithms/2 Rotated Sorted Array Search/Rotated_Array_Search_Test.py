from Rotated_Array_Search import rotated_array_search

# Linear Search helper function that will find the target using linear search.
# It's used to test the binary search method
def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

# helper function that will perform the test cases and check if the results match
def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

# test cases
print("\n----------------------")
print("Checking Edge Cases...")
print("----------------------\n")
print("TEST_CASE_1: empty list, returns -1")
test_function([[], 6])
print("\nTEST_CASE_2: single element list, target matches the element, returns 0")
test_function([[6], 6])
print("\nTEST_CASE_3: single element list, target does not match the element, returns -1")
test_function([[1], 6])

print("\n-------------------------")
print("Checking Rotated Array...")
print("-------------------------\n")
print("TEST_CASE_4: Array = [6, 7, 8, 9, 10, 1, 2, 3, 4], Number = 6 (exists), returns 0")
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
print("\nTEST_CASE_5: Array = [6, 7, 8, 9, 10, 1, 2, 3, 4], Number = 1 (exists), returns 5")
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
print("\nTEST_CASE_6: Array = [6, 7, 8, 1, 2, 3, 4], Number = 8 (exists), returns 2")
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
print("\nTEST_CASE_7: Array = [6, 7, 8, 1, 2, 3, 4], Number = 1 (exists), returns 3")
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
print("\nTEST_CASE_8: Array = [6, 7, 8, 1, 2, 3, 4], Number = 10 (doesn't exist), returns -1")
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

print("\n-----------------------------")
print("Checking Non-rotated Array...")
print("-----------------------------\n")
print("TEST_CASE_9: Array = [6, 7, 8, 9, 10, 1, 2, 3, 4], Number = 0 (exists), returns 0")
test_function([[0, 1, 2, 4, 5, 6, 7], 0])
print("\nTEST_CASE_10: Array = [6, 7, 8, 9, 10, 1, 2, 3, 4], Number = 10 (doesn't exists), returns -1")
test_function([[0, 1, 2, 4, 5, 6, 7], 10])

''' EXPECTED OUTPUT
----------------------
Checking Edge Cases...
----------------------

TEST_CASE_1: empty list, returns -1
Pass

TEST_CASE_2: single element list, target matches the element, returns 0
Pass

TEST_CASE_3: single element list, target does not match the element, returns -1
Pass

-------------------------
Checking Rotated Array...
-------------------------

TEST_CASE_4: Array = [6, 7, 8, 9, 10, 1, 2, 3, 4], Number = 6 (exists), returns 0
Pass

TEST_CASE_5: Array = [6, 7, 8, 9, 10, 1, 2, 3, 4], Number = 1 (exists), returns 5
Pass

TEST_CASE_6: Array = [6, 7, 8, 1, 2, 3, 4], Number = 8 (exists), returns 2
Pass

TEST_CASE_7: Array = [6, 7, 8, 1, 2, 3, 4], Number = 1 (exists), returns 3
Pass

TEST_CASE_8: Array = [6, 7, 8, 1, 2, 3, 4], Number = 10 (doesn't exist), returns -1
Pass

-----------------------------
Checking Non-rotated Array...
-----------------------------

TEST_CASE_9: Array = [6, 7, 8, 9, 10, 1, 2, 3, 4], Number = 0 (exists), returns 0
Pass

TEST_CASE_10: Array = [6, 7, 8, 9, 10, 1, 2, 3, 4], Number = 10 (doesn't exists), returns -1
Pass
'''