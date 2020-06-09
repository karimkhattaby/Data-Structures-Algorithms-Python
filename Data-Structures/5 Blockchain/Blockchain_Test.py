from Blockchain import BlockChain

# Creating a new block chain
block_chain = BlockChain()

# test case, operations on an empty block chain
print("\nChecking TEST_CASE_1: Empty block chain\n")
# size of block chain
print("The size of block chain is: "+str(block_chain.get_size()))
# block chain head block
print("The head of block chain is: "+str(block_chain.get_head()))
# searching for a block which doesn't exist
print("Is there a block with data '1' in the block chain ? "+str(block_chain.find_block('1')))
# printing the list of all blocks in the block chain
print("The list of blocks in the block chain are: "+str(block_chain.get_blocks()))
# adding a block
block_chain.add_block("1")
print("Added a block with data '1' to the empty block chain...")
'''
Checking TEST_CASE_1: Empty block chain

The size of block chain is: 0
The head of block chain is: None
Is there a block with data '1' in the block chain ? -1
The list of blocks in the block chain are: []
Added a block with data '1' to the empty block chain...
'''

# test case, operations on a block chain which includes 1 block
print("\nChecking TEST_CASE_2: block chain with a single block\n")
# size of block chain
print("The size of block chain is: "+str(block_chain.get_size()))
# block chain head block
print("The head of block chain is: "+str(block_chain.get_head()))
# searching for a block which exists
print("Is there a block with data '1' in the block chain ? "+str(block_chain.find_block('1')))
# searching for a block which doesn't exist
print("Is there a block with data '2' in the block chain ? "+str(block_chain.find_block('2')))
# printing the list of all blocks in the block chain
print("The list of blocks in the block chain are: "+str(block_chain.get_blocks()))
# adding 2 blocks
block_chain.add_block("2")
print("Added a block with data '2' to the empty block chain...")
block_chain.add_block("3")
print("Added a block with data '3' to the empty block chain...")
'''
Checking TEST_CASE_2: block chain with a single block

The size of block chain is: 1
The head of block chain is: <__main__.Block instance at 0x1020ef0e0>
Is there a block with data '1' in the block chain ? <__main__.Block instance at 0x1020ef0e0>
Is there a block with data '2' in the block chain ? -1
The list of blocks in the block chain are: [<__main__.Block instance at 0x1020ef0e0>]
Added a block with data '2' to the empty block chain...
Added a block with data '3' to the empty block chain...
'''

# test case, operations on a block chain which includes multipls blocks
print("\nChecking TEST_CASE_3: block chain with multiple blocks\n")
# size of block chain
print("The size of block chain is: "+str(block_chain.get_size()))
# block chain head block
print("The head of block chain is: "+str(block_chain.get_head()))
# searching for a block which exists
print("Is there a block with data '2' in the block chain ? "+str(block_chain.find_block('2')))
# searching for a block which doesn't exist
print("Is there a block with data '4' in the block chain ? "+str(block_chain.find_block('4')))
# printing the list of all blocks in the block chain
print("The list of blocks in the block chain are: "+str(block_chain.get_blocks()))
# printing the list of all blocks upto a certain block
print("The list of blocks in the block chain upto the block which includes'2' "
        +str(block_chain.get_blocks('2')))
'''
Checking TEST_CASE_3: block chain with multiple blocks

The size of block chain is: 3
The head of block chain is: <__main__.Block instance at 0x1020ef1b8>
Is there a block with data '2' in the block chain ? <__main__.Block instance at 0x1020ef170>
Is there a block with data '4' in the block chain ? -1
The list of blocks in the block chain are: [<__main__.Block instance at 0x1020ef1b8>, <__main__.Block instance at 0x1020ef170>, <__main__.Block instance at 0x1020ef0e0>]
The list of blocks in the block chain upto the block which includes'2' [<__main__.Block instance at 0x1020ef1b8>, <__main__.Block instance at 0x1020ef170>]
'''

# edge test case, adding a block with null data
print("\nChecking TEST_CASE_4: null data\n")

try:
    block_chain.add_block(None)
except ValueError:
    print("Adding a block of null data raised a ValueError")

print("Searching for a block which contains null data will return -1 in O(1) time, result: "
    + str(block_chain.find_block(None)))
'''
Checking TEST_CASE_4: null data

Adding a block of null data raised a ValueError
Searching for a block which contains null data will return -1 in O(1) time, result: -1
'''