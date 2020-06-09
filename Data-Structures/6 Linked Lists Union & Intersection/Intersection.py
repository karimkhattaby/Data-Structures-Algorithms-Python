from Linked_List import LinkedList

""" intersection method:
    Finds the intersection of 2 linked lists.

    Args:
      llist_1(class: Linked_List): list 1 to be intersected with list 2
      llist_2(class: Linked_List): list 2 to be intersected with list 1

    Returns:
      intersected_list(class: Linked_List): the resulting linked list of the intersection operation
"""
def intersection(llist_1, llist_2):
    # edge case, if any of the lists is null, we return null
    if llist_1 is None or llist_2 is None:
        return None
    if llist_1.head is None or llist_2.head is None:
        return None
    
    # the final linked list which we will return
    intersected_list = LinkedList()

    # in intersection, we need to store items which appear in both lists
    # so we use a set to store the elements in list 1
    set_1 = set()
    # and another set to store the intersected elements
    intersected_set = set()

    # we loop through the first linked list, and add its elements to set 1
    current_node = llist_1.head
    while current_node is not None:
        set_1.add(current_node.value)
        current_node = current_node.next

    # we loop through the second linked list
    current_node = llist_2.head
    while current_node is not None:
        # if the value of the current node exists in list 1, we add it to our final set
        if current_node.value in set_1:
            intersected_set.add(current_node.value)
        current_node = current_node.next
    
    # now we add the intersected elements to our final linked list and return it
    for value in intersected_set:
        intersected_list.append(value)
    
    # if the intersection is an empty list, we return None
    # otherwise we return the list
    return intersected_list if intersected_list.head is not None else None
