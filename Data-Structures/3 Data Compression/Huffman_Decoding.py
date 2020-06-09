from Huffman_Coding_Helpers import generate_codes

""" huffman_decoding method:
    Performs compressed data extraction using huffman coding algorithm.

    Args:
      1- data(str): the data to be extracted/decompressed
      2- tree(class:Huffman_Tree_Node): the root node of the huffman tree

    Returns:
      decoded_data(str): stores the extracted data
"""
def huffman_decoding(data,tree):
    # helper function that will create a map of each code and its corresponding letter
    codes = generate_codes(tree, encode=False)

    # edge case, if there was 1 unique character in our data
    if( len(codes) ) == 1:
      # we simply convert all 0s in the data string to the stored character in the tree and return it
      return tree.char*len(data)
    
    # decode the data using the map and return it
    decoded_data = []
    j = 0
    for i in range(len(data)):
      # use slicing since codes have different lengths
      if data[j:i+1] in codes:
        decoded_data.append(codes[data[j:i+1]])
        j = i+1
    # we return the extracted string by joining the list
    return ''.join(decoded_data)