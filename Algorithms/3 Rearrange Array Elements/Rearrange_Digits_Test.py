from Rearrange_Digits import rearrange_digits

# helper function to perform testing
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    print(output, solution)
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# test cases
print("\n----------------------")
print("Checking Edge Cases...")
print("----------------------\n")
print("TEST_CASE_1: null value, returns [-1, -1]")
test_function([None, [-1, -1]])
print("\nTEST_CASE_2: empty list, returns an empty list")
test_function([[], []])

print("\n-----------------------")
print("Checking Other Cases...")
print("-----------------------\n")
print("TEST_CASE_3: a list of 2 elements, returns the same list")
test_function([[1, 2], [1, 2]])
print("\nTEST_CASE_4: Array = [1, 2, 3, 4, 5], returns [542, 31]")
test_function([[1, 2, 3, 4, 5], [542, 31]])
print("\nTEST_CASE_5: Array = [4, 6, 2, 5, 9, 8], returns [964, 852]")
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

'''EXPECTED OUTPUT
----------------------
Checking Edge Cases...
----------------------

TEST_CASE_1: null value, returns [-1, -1]
([-1, -1], [-1, -1])
Pass

TEST_CASE_2: empty list, returns an empty list
([], [])
Pass

-----------------------
Checking Other Cases...
-----------------------

TEST_CASE_3: a list of 2 elements, returns the same list
([1, 2], [1, 2])
Pass

TEST_CASE_4: Array = [1, 2, 3, 4, 5], returns [542, 31]
([531, 42], [542, 31])
Pass

TEST_CASE_5: Array = [4, 6, 2, 5, 9, 8], returns [964, 852]
([964, 852], [964, 852])
Pass
'''