from Linked_List_Node import Node

class LinkedList:
    def __init__(self):
        self.head = None # pointer to the head node

    # string method to convert a linked list to a string of values
    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    # appending a new node to the linked list
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    # method to return the size of the linked list through traversal
    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
