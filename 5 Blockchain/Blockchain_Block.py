import hashlib # used to generate hashes
import datetime # used to get current time

# Node class modified to hold each block information.
class Block:
    def __init__(self, data, previous_hash = None):
      self.data = data #stores the block transaction data
      self.timestamp = datetime.datetime.utcnow() #stores the transaction time
      self.hash = self.calc_hash() #stores the current block hash
      self.previous_hash = previous_hash #stores the previous block hash
      # added a pointer to the previous block
      # otherwise the block will go for garbage collection when adding a new block
      self.previous_block = None
    
    # hash calculation helper function.
    def calc_hash(self):
      sha = hashlib.sha256()
      hash_str = self.data.encode('utf-8')
      sha.update(hash_str)
      return sha.hexdigest()
    
    # NOTE TODO UNCOMMENT THE BELOW LINES IF YOU WANT TO VISUALIZE THE CONTENT OF BLOCKS
    #### helper string representation to visualize the block data
    #def __repr__(self):
        #return repr("data: "+str(self.data)+", timestamp: "+str(self.timestamp)+
        #", hash: "+ str(self.hash)+", previous block hash: "+str(self.previous_hash))
