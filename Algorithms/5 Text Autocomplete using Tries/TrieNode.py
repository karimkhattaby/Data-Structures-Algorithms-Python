## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False # define if this node marks the end of a valid word
        self.children = {} # children nodes
    
    # Class method that collects the suffix for all complete words below this point
    def suffixes(self, suffix = ''):
        # An empty list to store found suffixes
        suffixes_list = []
        
        # if the current node marks a valid word
        if self.is_word:
            # append the suffix to the list
            suffixes_list.append(suffix)
        
        # Get current node children
        children_to_visit = list(self.children.items())
        # (is_word, children)
        
        # We loop until no children nodes are avialble
        while len(children_to_visit) > 0:            
            # We extract the current word and node
            current_word, current_node = children_to_visit.pop()
            
            # If the current node is a word
            if current_node.is_word:
                # add it to the suffixes list
                suffixes_list.append(current_word)
            
            # Get the current node children
            # and add them to the children to be checked
            for child in current_node.children:
                children_to_visit.append((current_word+child, current_node.children[child]))
        
        # After the loop, return the suffixes found
        return suffixes_list
