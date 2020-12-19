# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 19:41:29 2020

@author: lveys
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
    
def union(llist_1, llist_2):  # Overall complexity O(n)
    # Your Solution Here
    # check if None input. Initiate empty list in such case to cover algorithm (defensive)
    if not llist_1:
        llist_1 = LinkedList()
    if not llist_2:
        llist_2 = LinkedList()
    
    union_list = LinkedList()
    discovered_values = set()
    
    node = llist_1.head
    # traverse list 1 to capture its unique values
    while node:
        if node.value not in discovered_values:             # traverse O(n1)
            # add to union values not yet discovered
            union_list.append(node.value)                   # O(1)
            # keep track of the values already discovered
            discovered_values.add(node.value)               # O(1)
        node = node.next
    
    # repeat approach with list 2
    node = llist_2.head
    while node:                                             # traverse O(n2)
        if node.value not in discovered_values:
            # add to union values not yet discovered
            union_list.append(node.value)
            # keep track of the values already discovered
            discovered_values.add(node.value)
        node = node.next
            
    return union_list


def intersection(llist_1, llist_2):
    # Your Solution Here
    len_1 = llist_1.size()    # calculate length list1 - complexity O(n1)
    if len_1 == 0:            # check if list1 empty - complexity O(1)
        return None
    len_2 = llist_2.size()    # calculate length list2 - complexity O(n2)
    if len_2 == 0:            # check if list2 empty - complexity O(1)
        return None
        
    discovered_values_1 = set()
    discovered_values_2 = set()
    
    node = llist_1.head
    while True:               # Traverse list once - O(n1)
        discovered_values_1.add(node.value)
        if node.next:
            node = node.next
            while node.value in discovered_values_1 and node.next: # Time complexity of this operation is O(1) on average
                node = node.next
        else:
            break
        
    node = llist_2.head
    while True:               # Traverse list once - O(n2)
        discovered_values_2.add(node.value)
        if node.next:
            node = node.next
            while node.value in discovered_values_2 and node.next: # Time complexity of this operation is O(1) on average
                node = node.next
        else:
            break
    
    intersection_list = LinkedList()
    intersection_values = set()
    
    element = llist_1.head
    while element:       # Traverse list - O(n1)
        if (element.value not in discovered_values_1) or (element.value not in discovered_values_2): # Time complexity of this operation is O(1) on average
            # do not add values not part of both sets
            pass
        elif element.value not in intersection_values:
            # add the value not yet discovered and update the tracking set
            intersection_list.append(element.value)
            intersection_values.add(element.value)
        element = element.next
        
    element = llist_2.head
    while element:       # Traverse list - O(n2)
        if (element.value not in discovered_values_1) or (element.value not in discovered_values_2): # Time complexity of this operation is O(1) on average
            # do not add values not part of both sets
            pass
        elif element.value not in intersection_values:
            # add the value not yet discovered and update the tracking set
            intersection_list.append(element.value)
            intersection_values.add(element.value)
        element = element.next    
    

    return intersection_list



# Test case 1
print('================== Test n°1 ================')
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print('list 1:', element_1)
print('list 2:', element_2)
print ('Union =',union(linked_list_1,linked_list_2))
print ('Intersection', intersection(linked_list_1,linked_list_2))

# Test case 2
print('================== Test n°2 ================')
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print('list 1:', element_1)
print('list 2:', element_2)
print ('Union =',union(linked_list_3,linked_list_4))
print ('Intersection', intersection(linked_list_3,linked_list_4))

# Test case 3
print('================== Test n°3 ================')
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [3,2,16]
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print('list 1:', element_1)
print('list 2:', element_2)
print ('Union =',union(linked_list_5,linked_list_6))
print ('Intersection', intersection(linked_list_5,linked_list_6))

# Test case 4
print('================== Test n°4 ================')
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = [3,0,16,5]
element_2 = [5]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print('list 1:', element_1)
print('list 2:', element_2)
print ('Union =',union(linked_list_7,linked_list_8))
print ('Intersection', intersection(linked_list_7,linked_list_8))

# Test case 5
print('================== Test n°5 ================')
linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

element_1 = [11,11]
element_2 = []

for i in element_1:
    linked_list_9.append(i)

for i in element_2:
    linked_list_10.append(i)

print('list 1:', element_1)
print('list 2:', element_2)
print ('Union =',union(linked_list_9,linked_list_10))
print ('Intersection', intersection(linked_list_9,linked_list_10))

# Test case 6
print('================== Test n°6 ================')
linked_list_11 = LinkedList()
linked_list_12 = LinkedList()

element_1 = []
element_2 = [0,5,8,8]

for i in element_1:
    linked_list_11.append(i)

for i in element_2:
    linked_list_12.append(i)

print('list 1:', element_1)
print('list 2:', element_2)
print ('Union =',union(linked_list_11,linked_list_12))
print ('Intersection', intersection(linked_list_11,linked_list_12))