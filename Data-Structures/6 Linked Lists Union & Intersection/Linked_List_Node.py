class Node:
    def __init__(self, value):
        self.value = value # the data stored in the node
        self.next = None # a pointer to the next node

    # string representation of the node, will print the value
    def __repr__(self):
        return str(self.value)