from Huffman_Coding_Helpers import create_huffman_tree, generate_codes

""" huffman_encoding method:
    Performs data compression using huffman coding algorithm.

    Args:
      data(str): the data to be compressed

    Returns:
      1- encoded_data(str): stores the compressed data
      2- root(class:Huffman_Tree_Node): stores the root node of the huffman tree
"""
def huffman_encoding(data):
    # helper function that will create the huffman tree and return its root
    root = create_huffman_tree(data)
    # helper function that will create a map of each letter and its corresponding code
    codes = generate_codes(root)

    # edge case, if there was 1 unique character in our data
    if( len(codes) ) == 1:
        # we simply convert all characters to 0 and return it
      return "0"*len(data), root
    
    ### Encode the data using the map and return it:-
    # we loop through all characters, and convert each character to its huffman code
    encoded_data = [codes[char] for char in data] #we create a list of characters
    
    # we return the code string by joining the list, we also return the huffman tree root
    return ''.join(encoded_data), root