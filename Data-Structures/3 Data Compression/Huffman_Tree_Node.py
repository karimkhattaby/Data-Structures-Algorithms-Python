# Huffman Tree Node Class Definition
class Huffman_Tree_Node:
    def __init__(self, char, freq):
        # Store the character
        self.char = char
        # Store the frequency of the character
        self.freq = freq
        # Left child
        self.left = None
        # Right child
        self.right = None
    # Class method to check if the current node is a leaf node
    def isLeaf(self):
        # a node is a leaf node if it has no children
        return (not self.left) and (not self.right)