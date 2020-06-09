# RouteTrieNode class represents a trie node
class RouteTrieNode:
    ## Initialize the node with children plus a handler
    def __init__(self, handler = None):
        self.handler = handler
        self.children = {}

    ## Insert a child node to the current node
    def insert(self, path_piece, handler = None):
        self.children[path_piece] = RouteTrieNode(handler)
