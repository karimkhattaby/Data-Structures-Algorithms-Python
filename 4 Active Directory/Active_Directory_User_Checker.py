# method that checks if a user belongs to a group or any of its children groups in the hierarchy
""" is_user_in_group method
    Returns True if a user belongs to a group or its sub-groups, and False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
"""
def is_user_in_group(user, group):
    # if the user is a member of the specified group, return True
    users = group.get_users()
    if user in users:
        return True
    
    # if the user is not a member of the specified group,
    # check each of the sub groups in the heirarchy
    groups = group.get_groups()
    
    # loop through all the sub groups
    while len(groups) > 0:
        # extract the current group from the groups list
        current_group = groups.pop()
        
        # if the user is a member of the current group, return True
        users = current_group.get_users()
        if user in users:
            return True
        
        # if the user is not a member of the current group,
        # add its sub groups to the groups list to check them as well
        groups.extend(current_group.get_groups())

    # if we made it this far,
    # it means we traveresed the groups hierarchy
    # without finding the user belonging to any of the groups.
    # So we return False
    return False
