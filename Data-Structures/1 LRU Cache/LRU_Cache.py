# will use an ordered dictionary to store the data and achieve the desired solution
# https://docs.python.org/3/library/collections.html#collections.OrderedDict
from collections import OrderedDict

class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        # ordered dictionary has the same properties as dictionary
        # except that it reserves the order of inserted elements
        self.LRU_dict = OrderedDict()
        # how many elements we currently have in the cache
        self.current_size = 0
        # the maximum capacity of the cache
        self.capacity = capacity

    def get(self, key): # O(1)
        # edge case if key was passed a null value
        if key is None:
            return -1
        
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.LRU_dict: #if the key exists
            value = self.LRU_dict[key] #save the value temporarily
            del self.LRU_dict[key] # del the item from the cache
            # Reinsert the item to the cache
            # This will change the order of items
            # And the most recently used item will be moved to the end of the cache
            self.LRU_dict[key] = value
            
            return value # return the required value
        else:
            return -1

    def set(self, key, value): #O(1)
        # edge case if key was passed a null value, or if the capacity was initially set to 0
        if key is None or value is None or self.capacity == 0:
            return
        
        if key in self.LRU_dict: #if the key already exists in the cache
            # we will delete the existing entry so we can add it to the end of the dictionary,
            # since it was the most recently accessed.
            del self.LRU_dict[key]
        
        else: #if the key doesn't exist
            # we check if we reached the maximum capacity
            if self.current_size == self.capacity:
                # If so, we remove the least recently used item
                #refer to collections.OrderedDict documentation for more information
                self.LRU_dict.popitem(last=False) #last=False means FIFO
                # the first item that was added to the dictionary is the least recently used item
                # the last item added to the dictionary is the most recently used item
            
            else: # if we haven't reached the maximum capacity,
                # we increment the cache elements counter.
                self.current_size += 1
        
        # after checking all cases and regardless of the case,
        # we will add the new item to our cache.
        self.LRU_dict[key] = value
    
    # helper function to visualize the contents of the data structure
    # you can use print() to print the dictionary, current size and capacity
    def __repr__(self):
        return repr('LRU_dict: ' + str(list(self.LRU_dict)) + ' current_size = '
        + str(self.current_size) + ' capacity = ' + str(self.capacity))
