# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 19:08:11 2020

@author: lveys
"""

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

# worst case complexity O(n), proportional to the number of elements within the group (and subgroups)
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if group.groups == []:                     # check presence of group(s). If not, return False
        return False
    for g in group.groups:                     # A group can have subgroups with users
        if user in g.users:                    # First, check presence of user in users of parent group
            return True                        # if user found, return True
        # for each subgroup, check presence of user with recursive search
        if is_user_in_group(user, g):          # if user found, return True
            return True
    
    # if group and subgroups explored without finding 'user', return False
    return False

# Test 1 : create a Group with subgroups Parent>Child>subchild. Find 'sub_child_user' in Parent

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

#print(is_user_in_group("sub_child_user", parent))
if is_user_in_group("sub_child_user", parent) == True:
    print('test 1 passed')


# Test 2 : create a Group with subgroups Parent>Child>subchild. Find 'child_user' in Parent

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

child_user = "child_user"
child.add_user(child_user)

child.add_group(sub_child)
parent.add_group(child)

#print(is_user_in_group("child_user", parent))
if is_user_in_group("child_user", parent) == True:
    print('test 2 passed')
    
# Test 3 : create a Group with subgroups Parent>Child>subchild. Check if 'user' in Parent

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

child.add_group(sub_child)
parent.add_group(child)

#print(is_user_in_group("user", parent))
if is_user_in_group("user", parent) == False:
    print('test 3 passed')

# Test 4 : create a Group Parent. Check if 'user' in Parent

parent = Group("parent")

#print(is_user_in_group("user", parent))
if is_user_in_group("user", parent) == False:
    print('test 4 passed')
    
# Test 5 : create an empty Group. Check if 'user' in Parent

parent = Group("")

#print(is_user_in_group("user", parent))
if is_user_in_group("user", parent) == False:
    print('test 5 passed')