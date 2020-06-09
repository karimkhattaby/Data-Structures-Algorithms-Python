from Linked_List import LinkedList
from Union import union
from Intersection import intersection

# Test case 1, 2 linked lists with elements in union and intersection
print("\nChecking TEST_CASE_1: 2 linked lists with elements in union and intersection\n")

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)


print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))
'''
Checking TEST_CASE_1: 2 linked lists with elements in union and intersection

32 -> 65 -> 2 -> 35 -> 4 -> 6 -> 1 -> 9 -> 11 -> 3 -> 21 -> 
4 -> 21 -> 6 -> 
'''

# Test case 2, 2 linked lists with elements in union but no intersection
print("\nChecking TEST_CASE_2: 2 linked lists with elements in union but no intersection\n")

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
'''
Checking TEST_CASE_2: 2 linked lists with elements in union but no intersection

65 -> 2 -> 35 -> 4 -> 6 -> 1 -> 8 -> 9 -> 7 -> 11 -> 3 -> 21 -> 23 -> 
None
'''

# Test case 3, one of the linked lists is empty
print("\nChecking TEST_CASE_3: one of the linked lists is empty\n")

linked_list_5 = LinkedList()

print (union(linked_list_4,linked_list_5))
print (intersection(linked_list_4,linked_list_5))
'''
Checking TEST_CASE_3: one of the linked lists is empty

1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 1 -> 
None
'''
