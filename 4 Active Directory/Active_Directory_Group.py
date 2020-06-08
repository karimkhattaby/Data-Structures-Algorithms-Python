# Active Directory Group Class Definition
class Group(object):
    def __init__(self, _name):
        # group name
        self.name = _name
        # list to store child groups
        self.groups = []
        # list to store users that belong to this group
        self.users = []

    # method that adds a child group to the current group
    def add_group(self, group):
        self.groups.append(group)

    # method that adds a user to the current group
    def add_user(self, user):
        self.users.append(user)

    # method that returns the list of child groups of the current group
    def get_groups(self):
        return self.groups

    # method that returns the list of users that belong to the current group
    def get_users(self):
        return self.users

    # method that returns the name of the current group
    def get_name(self):
        return self.name
