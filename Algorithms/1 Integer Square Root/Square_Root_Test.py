from Square_Root import sqrt

print("\n----------------------")
print("Checking Edge Cases...")
print("----------------------\n")
print("TEST_CASE_1: square root of 0 is 0")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print("\nTEST_CASE_2: square root of 1 is 1")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print("\nTEST_CASE_3: square root of a null value is -1")
print("Pass" if  (-1 == sqrt(None)) else "Fail")
print("\nTEST_CASE_4: square root of a negative value is -1")
print("Pass" if  (-1 == sqrt(-5000)) else "Fail")

print("\n---------------------------")
print("Checking Perfect Squares...")
print("---------------------------\n")
print("Checking TEST_CASE_5: square root of 9 is equal to 3")
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print("\nChecking TEST_CASE_6: square root of 16 is equal to 4")
print ("Pass" if  (4 == sqrt(16)) else "Fail")

print("\n-------------------------------")
print("Checking Non-Perfect Squares...")
print("-------------------------------\n")
print("Checking TEST_CASE_7: the floor of the square root of 27 is equal to 5")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

''' EXPECTED OUTPUT
----------------------
Checking Edge Cases...
----------------------

TEST_CASE_1: square root of 0 is 0
Pass

TEST_CASE_2: square root of 1 is 1
Pass

TEST_CASE_3: square root of a null value is -1
Pass

TEST_CASE_4: square root of a negative value is -1
Pass

---------------------------
Checking Perfect Squares...
---------------------------

Checking TEST_CASE_5: square root of 9 is equal to 3
Pass

Checking TEST_CASE_6: square root of 16 is equal to 4
Pass

-------------------------------
Checking Non-Perfect Squares...
-------------------------------

Checking TEST_CASE_7: the floor of the square root of 27 is equal to 5
Pass
'''