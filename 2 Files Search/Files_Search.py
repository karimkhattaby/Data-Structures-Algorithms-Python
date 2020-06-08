import os # used to navigate directories

""" find_files method:
    Finds all files beneath path with file name suffix.

    Note that a path may contain further subdirectories,
    and those subdirectories may also contain further subdirectories.
    - There is no limit to the depth which the subdirectories can go.

    Args:
      suffix(str): suffix of the file name to be found.
      path(str): path of the file system.

    Returns:
       paths(list): a list of paths found matching the suffix.
       OR
       Error(str): a custom error message.
"""
def find_files(suffix, path=""): # O(n)
    # edge case, if path or suffix are invalid
    if path is None or suffix is None:
        return "Incorrect path or suffix."
    
    # edge case, if no path was given, assume current directory as starting point
    if path == "":
        path = "."
    
    # list to store files matching the suffix
    files_list = []
    
    # create a list to store directories and files to be checked
    try: #if the path doesn't exist, the code will raise an error
        dir_list = os.listdir(path)
    except OSError: #in that case we catch it and return an error string
        return "Path doesn't exist."

    # we loop through all available entries in the directories list
    while len(dir_list) > 0:
        # remove the last entry in the directories list and assign it to entry
        entry = dir_list.pop()
        
        # create the current path to be checked, from the given path and the current entry
        current_path = os.path.join(path, entry) # example: current_path = "./testdir/subdir1"
        
        ''' check if the current path is a file or a directory '''
        # if the current path is a file, and it matches our suffix
        if os.path.isfile(current_path) and current_path.endswith(suffix):
            # add it to our files list
            files_list.append(current_path)
        
        # if the current path is a directory
        elif os.path.isdir(current_path) :
            # get the directories inside the current path and append them to the directories list
            sub_dirs = os.listdir(current_path)
            for sub_dir in sub_dirs:
                #the appended sub directories need to have the entry appended with a '/'
                dir_list.append(entry+'/'+sub_dir)
        
        # else, if the current path is a file which doesn't match our suffix, we do nothing and go next

    # at the end of our function and after the loop, we return the list of files which we found
    return files_list if len(files_list)>0 else "No files found matching the given suffix."
    # if no files were found, we return a descriptive error message
