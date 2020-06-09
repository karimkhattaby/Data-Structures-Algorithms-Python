from TrieNode import TrieNode

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    ## Class method to add a word to the Trie
    def insert(self, word):
        # Edge case, null value
        if word is None:
            return
        
        # Start from the Trie root
        current_node = self.root
        
        # Loop through all characters in the word
        for char in word:
            # Insert each character as a child node of the previous
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            # Go to next node
            current_node = current_node.children[char]
        
        # At the end of the word, set its flag to mark the end of a valid word
        current_node.is_word = True

    ## Class method to find the Trie node that represents this prefix
    def find(self, prefix):
        # Edge case, null value
        if prefix is None:
            return None
        
        # Start from the Trie root
        current_node = self.root
        
        # Loop through all characters in the prefix
        for char in prefix:
            # If the current character doesn't exist in the Trie node children
            if char not in current_node.children:
                # Return not found
                return None
            # Otherwise, we go to the next node
            current_node = current_node.children[char]
            
        # When we're out of the loop, the current node is the terminal node of the trie
        return current_node
