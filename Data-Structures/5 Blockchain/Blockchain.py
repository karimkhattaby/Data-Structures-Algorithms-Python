from Blockchain_Block import Block

# LinkedList class modifited to link blocks defined in the Block class.
class BlockChain:
    # each block chain will keep information of:
    def __init__(self):
        #the head block (latest added block)
        self.head = None
        #the size of the chain (how many blocks are in the chain)
        self.size = 0
    
    # adds a new block to the chain
    # NOTE null data IS NOT allowed. empty strings ARE allowed
    def add_block(self, data):
        # if the passed data is null
        if data is None:
            # raise a value error
            raise ValueError
        
        # create a new block object
        new_block = Block(data)
        
        # if the chain is not empty (can also be checked from the size)
        if self.head:
            # get the new block to point to the previous block
            new_block.previous_block = self.head
            new_block.previous_hash = self.head.hash
        
        # update the chain head and size
        self.head = new_block
        self.size += 1
    
    # returns the head of the block chain
    def get_head(self):
        return self.head
    
    # returns the size of the block chain
    def get_size(self):
        return self.size
    
    # searches for a block, -1 if it doesn't exist
    def find_block(self, data):
        # edge case, since None data is NOT allowed, we know it will never exist in the chain
        if data is None:
            return -1
        
        # start from the head block
        current_block = self.head
        
        # loop through all the blocks
        while current_block is not None:
            # if we found the block that holds the data we need
            if current_block.data == data:
                # return the found block
                return current_block
            # otherwise, go the previous block and keep looping
            current_block = current_block.previous_block
        
        # if the block doesn't exist or if the chain is empty, return -1
        return -1

    # returns a list of blocks traversed upto a given data value
    # if no data was given or the data doesn't exist in the chain, return all blocks in the chain
    # if chain is empty, it will return an empty list
    def get_blocks(self, data = None):
        # create a list of blocks visited so far
        blocks_list = []

        # start from the head block
        current_block = self.head
        # loop through all blocks in the chain
        while current_block is not None:
            # add the visited block to the list
            blocks_list.append(current_block)
            # if we found the required block
            if current_block.data == data:
                # return the list of visited blocks
                return blocks_list
            # otherwise, go to the previous block and keep looping
            current_block = current_block.previous_block
        
        # after the loop (data not found or null data), return the list of visited blocks
        return blocks_list
