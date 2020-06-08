import collections
import heapq
from Huffman_Tree_Node import Huffman_Tree_Node

# helper function that will create the huffman tree and return its root
def create_huffman_tree(data):
    # list of tuples to store the frequency of each character
    # here we used collections.Counter to create a dictionary of frequencies
    # and then we converted it into a list of tuples
    frequencies = collections.Counter(data).items()
    
    # flip the list of tuples, so the heap will sort based on frequencies
    # and convert the values into tree nodes
    for i in range(len(frequencies)):
        # frequencies[i][0] is the character
        # frequencies[i][1] is the frequency
        frequencies[i] = (frequencies[i][1], Huffman_Tree_Node(frequencies[i][0], frequencies[i][1]))
        # we create a node of the character and its frequency
        # and we push back the node and frequency as a tuple in the list (frequency, node)
        # if we don't do that, the heap won't maintain the min frequency
    
    # we create a min heap out of the frequencies list
    heapq.heapify(frequencies)
    # the min entry in the heap will always be the entry with lowest frequency
    
    # we loop through all nodes until we have 1 node left in the min heap
    while len(frequencies) > 1:
        item1 = heapq.heappop(frequencies)[1] # we extract the node with min frequency
        item2 = heapq.heappop(frequencies)[1] # we extract the 2nd smallest node
        
        # we create a node with the total frequency of the 2 nodes
        node = Huffman_Tree_Node(item1.char+item2.char, item1.freq+item2.freq)
        # the smallest node becomes a left child of the created node
        node.left = item1
        # the 2nd smallest node becomes a right child of the created node
        node.right = item2
        
        # we push the new node to the heap along with its total frequency to our minheap
        heapq.heappush(frequencies, (node.freq, node))
    
    # after the loop we will have 1 node left, which is the root of our huffman tree
    return frequencies[0][1] # [(frequency, node)]... we only return the node

# helper function that will create a map of each letter and its corresponding code
# will be used for encoding as well as decoding
def generate_codes(root, encode=True):
    # dictionary that will store our characters and their codes
    codes = {}
    # encode = True will define the current mode
    # in encoding mode (encode=True), codes = {char: code}
    # in decoding mode (encode=False), codes = {code: char}
    
    # list of tuples to store each node we're visiting,
    # and the code we have obtained so far from traversing the tree
    nodes_to_visit = [ ("", root) ]

    # we loop through all nodes of the tree
    while len(nodes_to_visit)>0:
        # we extract the current code and current node from the list of tuples
        current_code, current_node = nodes_to_visit.pop()
        
        # if the current node is a leaf (only letters will be leaf nodes)
        if current_node.isLeaf():
            # we add the character stored in the current node to our dictionary
            # and give it the value of the code obtained so far
            if encode: # the encoding table maps characters to codes
                codes[current_node.char] = current_code
            else: # while the decoding table maps codes to characters
                codes[current_code] = current_node.char
        
        # if the current node is not a leaf node
        else:
            # we add the left node to the nodes to visit list
            # and store with it the current code with a 0 added to it
            nodes_to_visit.append((current_code+'0', current_node.left))
            # we add the right node to the nodes to visit list
            # and store with it the current code with a 1 added to it
            nodes_to_visit.append((current_code+'1', current_node.right))
    
    # after the loop we will have a dictionary of characters and their respective codes
    return codes
