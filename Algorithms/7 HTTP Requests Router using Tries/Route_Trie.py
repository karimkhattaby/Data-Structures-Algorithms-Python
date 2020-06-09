from Route_Trie_Node import RouteTrieNode

## A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    ## Initialize the trie with a root node and a handler, this is the root path or home page node
    def __init__(self, root_handler = None):
        self.root = RouteTrieNode(root_handler)

    ## Class method to add a path and a handler to the Trie
    def insert(self, path_pieces, handler):
        # Start from the Trie root
        current_node = self.root

        # Loop through all path pieces
        for path_piece in path_pieces:
            # Insert each path piece as a child node of the previous
            if path_piece not in current_node.children:
                current_node.insert(path_piece)
            # Go to the next node in the path
            current_node = current_node.children[path_piece]
        
        # After the loop, assign the handler to the last piece in the path
        # to indicate that it's a page
        current_node.handler = handler
        # Assuming null handlers mean we want to remove a page
        # If the path string was empty, the handler will be assigned to the root node
        # Assuming this is valid since root is the homepage

    ## Class method to navigate the Trie and return the handler of a specific path
    def find(self, path_pieces):
        # Start from the Trie root
        current_node = self.root

        # Loop through all directories in the path list
        for path_piece in path_pieces:
            # If the directory is not a child of the previous directory
            if path_piece not in current_node.children:
                # Then the path is not found, return None
                return None
            # Go to the next node
            current_node = current_node.children[path_piece]
        
        # After the loop, return the handler of the current node
        return current_node.handler
