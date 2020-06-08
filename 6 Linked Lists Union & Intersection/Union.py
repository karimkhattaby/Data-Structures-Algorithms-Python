from Linked_List import LinkedList

""" union method:
    Finds the union of 2 linked lists.

    Args:
      llist_1(class: Linked_List): list 1 to be unioned with list 2
      llist_2(class: Linked_List): list 2 to be unioned with list 1

    Returns:
      unioned_list(class: Linked_List): the resulting linked list of the union operation
"""
def union(llist_1, llist_2):
    # edge case, if either of the lists is null, we return the other list
    if llist_1 is None or llist_1.head is None:
        return llist_2
    if llist_2 is None or llist_2.head is None:
        return llist_1
    
    # the final linked list which we will return
    unioned_list = LinkedList()

    # in union, we need to make sure that elements in list 1 aren't repeated in list 2
    # so we need to use a set to ensure no duplicates
    unioned_set = set()

    # we loop through the first linked list, and add its elements to the set
    current_node = llist_1.head
    while current_node is not None:
        unioned_set.add(current_node.value)
        current_node = current_node.next
    
    # we loop through the second linked list, and add its elements to the set
    current_node = llist_2.head
    while current_node is not None:
        unioned_set.add(current_node.value)
        current_node = current_node.next

    # now we create the final linked list and return it
    for value in unioned_set:
        unioned_list.append(value)
        
    return unioned_list
