from LRU_Cache import LRU_Cache

# testing the edge case of a 0 capacity cache. cache should remain empty
empty_cache = LRU_Cache(0) #creates a cache with maximum capacity of 0
empty_cache.set(1, 1) #should do nothing
print(empty_cache.get(1)) #should return -1

# testing the cache functionality
our_cache = LRU_Cache(5) #creates a cache with maximum capacity of 5

our_cache.set(1, 1) #adds 1,1 to the cache
our_cache.set(2, 2) #adds 2,2 to the cache
our_cache.set(3, 3) #adds 3,3 to the cache
our_cache.set(4, 4) #adds 4,4 to the cache

# Accessing cache elements using get should change the order least recently used element
print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

# Adding 2 elements to the cache
our_cache.set(5, 5) #adds 5,5 to the cache
our_cache.set(6, 6) #cache capacity is full, the least recently used element will be removed

# Trying to access the removed element from last step
print(our_cache.get(3))
# returns -1 because the cache reached it's capacity and 3 was the least recently used entry

''' EXPECTED OUTPUT
-1
1
2
-1
-1
'''