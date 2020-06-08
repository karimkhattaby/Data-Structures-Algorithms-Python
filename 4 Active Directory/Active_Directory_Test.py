from Active_Directory_Group import Group
from Active_Directory_User_Checker import is_user_in_group

# test case provided by the problem statement
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# checking a user that exists in the groups in all levels of the hierarchy
print("\nChecking TEST_CASE_1: user belongs to all groups and sub groups, when present in the end of the heirarchy\n")
print("Does '" + parent.get_name() + "' group have '" + sub_child_user + "' user ? " + str(is_user_in_group(sub_child_user, parent)))
# prints "Does 'parent' group have 'sub_child_user' user ? True"
print("Does '" + child.get_name() + "' group have '" + sub_child_user + "' user ? " + str(is_user_in_group(sub_child_user, child)))
# prints "Does 'child' group have 'sub_child_user' user ? True"
print("Does '" + sub_child.get_name() + "' group have '" + sub_child_user + "' user ? " + str(is_user_in_group(sub_child_user, sub_child)))
# prints "Does 'subchild' group have 'sub_child_user' user ? True"

# test case when user doesn't exist in any of the groups
user_doesnt_exist = "user_doesnt_exist"
print("\nChecking TEST_CASE_2: user doesn't exist in any of the groups\n")
print("Does '" + parent.get_name() + "' group have '" + user_doesnt_exist + "' user ? " + str(is_user_in_group(user_doesnt_exist, parent)))
# prints "Does 'parent' group have 'user_doesnt_exist' user ? False"
print("Does '" + child.get_name() + "' group have '" + user_doesnt_exist + "' user ? " + str(is_user_in_group(user_doesnt_exist, child)))
# prints "Does 'child' group have 'user_doesnt_exist' user ? False"
print("Does '" + sub_child.get_name() + "' group have '" + user_doesnt_exist + "' user ? " + str(is_user_in_group(user_doesnt_exist, sub_child)))
# prints "Does 'subchild' group have 'user_doesnt_exist' user ? False"

# test case when a group has no users or sub groups
empty_group = Group("empty_group")
print("\nChecking TEST_CASE_3: group is empty\n")
print("Does '" + empty_group.get_name() + "' group have '" + sub_child_user + "' user ? " + str(is_user_in_group(sub_child_user, empty_group)))
# prints "Does 'empty_group' group have 'sub_child_user' user ? False"

''' EXPECTED OUTPUT
Checking TEST_CASE_1: user belongs to all groups and sub groups, when present in the end of the heirarchy

Does 'parent' group have 'sub_child_user' user ? True
Does 'child' group have 'sub_child_user' user ? True
Does 'subchild' group have 'sub_child_user' user ? True

Checking TEST_CASE_2: user doesn't exist in any of the groups

Does 'parent' group have 'user_doesnt_exist' user ? False
Does 'child' group have 'user_doesnt_exist' user ? False
Does 'subchild' group have 'user_doesnt_exist' user ? False

Checking TEST_CASE_3: group is empty

Does 'empty_group' group have 'sub_child_user' user ? False
'''