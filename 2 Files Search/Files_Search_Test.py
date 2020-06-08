from Files_Search import find_files

# test case to check a path that exists and has files that match our suffix
print("\nChecking TEST_CASE_1: Path given exists, suffix is present\n")
print(find_files(suffix=".c", path="./testdir"))
print('\n')
'''
should return the list of files found:
['./testdir/subdir1/a.c', './testdir/subdir5/a.c', './testdir/t1.c', './testdir/subdir3/subsubdir1/b.c']
'''

# test case to check a path that exists (current directory since no path was given to the method),
# but no files match the given suffix
print("\nChecking TEST_CASE_2: Path exists (current directory), suffix is NOT present\n")
print(find_files(suffix=".cpp"))
print('\n')
'''
should return a custom error message: NoFilesFound
"No files found matching the given suffix."
'''

# test case to check a valid suffix in a path which doesn't exist
print("\nChecking TEST_CASE_3: Path DOES NOT exist, suffix is valid\n")
print(find_files(suffix=".c", path="./testdir12312"))
print('\n')
'''
should return a custom error message: PathError
"Path doesn't exist."
'''

# test case to check a path that exists (current directory) but the given suffix is null
print("\nChecking TEST_CASE_4: Path exists (current directory), suffix is null\n")
print(find_files(suffix=None))
print('\n')
'''
should return a custom error message: NullValue
"Incorrect path or suffix."
'''


''' EXPECTED OUTPUT
Checking TEST_CASE_1: Path given exists, suffix is present

['./testdir/subdir1/a.c', './testdir/subdir5/a.c', './testdir/t1.c', './testdir/subdir3/subsubdir1/b.c']



Checking TEST_CASE_2: Path exists (current directory), suffix is NOT present

No files found matching the given suffix.



Checking TEST_CASE_3: Path DOES NOT exist, suffix is valid

Path doesn't exist.



Checking TEST_CASE_4: Path exists (current directory), suffix is null

Incorrect path or suffix.
'''