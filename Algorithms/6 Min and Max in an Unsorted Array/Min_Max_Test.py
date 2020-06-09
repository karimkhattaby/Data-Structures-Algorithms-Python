from Min_Max import get_min_max

# test cases
print("\n----------------------")
print("Checking Edge Cases...")
print("----------------------\n")
print("TEST_CASE_1: null value, returns null min and max")
print("Pass" if ((None, None) == get_min_max(None)) else "Fail")
print("\nTEST_CASE_2: empty list, returns null min and max")
print("Pass" if ((None, None) == get_min_max([])) else "Fail")
print("\nTEST_CASE_3: single element list, returns the same element as min and max")
print("Pass" if ((1, 1) == get_min_max([1])) else "Fail")

print("\n----------------------")
print("Checking Other Cases...")
print("----------------------\n")
print("TEST_CASE_4: list that has the same value across all elements, returns the same value")
print("Pass" if ((1, 1) == get_min_max([1, 1, 1, 1, 1, 1, 1])) else "Fail")
print("\nTEST_CASE_5: Test Case given by the problem statement")
## Example Test Case of Ten Integers
import random
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print("Array: {}".format(l)+str(", Returns (0, 9) ?"))
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")