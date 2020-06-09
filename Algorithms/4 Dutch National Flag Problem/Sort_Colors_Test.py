from Sort_Colors import sort_012

# helper function to perform testing
def test_function(test_case):
    sorted_array = sort_012(test_case)
    print("returns: "+ str(sorted_array))
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

# test cases
print("\n----------------------")
print("Checking Edge Cases...")
print("----------------------\n")
print("TEST_CASE_1: null value")
print(sort_012(None))
print("\nTEST_CASE_2: empty list")
test_function([])

print("\n-----------------------")
print("Checking Other Cases...")
print("-----------------------\n")
print("TEST_CASE_3: single value array [1]")
test_function([1])
print("\nTEST_CASE_4: Array: [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]")
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
print("\nTEST_CASE_5: Array: [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]")
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
print("\nTEST_CASE_6: Array: [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]")
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

''' EXPECTED OUTPUT
----------------------
Checking Edge Cases...
----------------------

TEST_CASE_1: null value
None

TEST_CASE_2: empty list
returns: []
Pass

-----------------------
Checking Other Cases...
-----------------------

TEST_CASE_3: single value array [1]
returns: [1]
Pass

TEST_CASE_4: Array: [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
returns: [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
Pass

TEST_CASE_5: Array: [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
returns: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
Pass

TEST_CASE_6: Array: [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
returns: [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
Pass
'''