from Route_Trie import RouteTrie

## The Router class will wrap the Trie class
class Router:
    ## Create a new RouteTrie for holding our routes
    def __init__(self, root_handler = None, not_found_handler = "Path Not Found"):
        self.route_trie = RouteTrie(root_handler)
        ## A handler for 404 (page not found) responses as well!
        self.not_found_handler = not_found_handler

    ## Class method to add a handler for a given path
    def add_handler(self, path, handler):
        ## You will need to split the path and pass the path parts
        ## as a list to the RouteTrie
        
        # Get the path pieces using the split_path helper
        path_pieces = self.split_path(path)
        
        # Forward the path pieces to the insert method of the route trie object
        self.route_trie.insert(path_pieces, handler)
        # If the path pieces is an empty list, the handler will be inserted into the root node

    ## Class method to lookup path and return the associated handler
    def lookup(self, path):
        # Get the path pieces using the split_path helper
        path_pieces = self.split_path(path)
        # Forward the path pieces to the find method of the route trie object
        handler = self.route_trie.find(path_pieces)
        # If the path pieces is an empty list, the received handler will be the root handler

        # If a handler exists for the given path, return it
        # Otherwise, if the received handler is None, return the not found handler
        # The 2nd case will occur if the path is invalid or it has no handler
        return handler if handler is not None else self.not_found_handler

    ## Class helper that will split a given path into path pieces used to navigate the trie
    def split_path(self, path):
        # Edge case, null path
        if path is None:
            # Assume it means the root node and return an empty list
            return []
        
        # Remove '/' from the beginning and end of the path string
        path = path.strip('/')
        
        # Edge case, empty string before/after stripping '/'
        if path == "":
            # Return an empty list indicating the root
            return []
        
        # Split the path string into a list of path pieces and return it
        return path.split('/')
