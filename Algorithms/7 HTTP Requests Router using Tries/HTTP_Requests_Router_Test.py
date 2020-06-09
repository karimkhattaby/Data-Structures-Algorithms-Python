from HTTP_Requests_Router import Router

# test cases

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about me", "about me handler")  # add a route

# perform some lookups with the expected output
print(router.lookup(None)) # should print 'root handler'
print(router.lookup("")) # should print 'root handler'
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler'
print(router.lookup("/home/about me")) # should print 'about me handler'
print(router.lookup("/home/about me/")) # should print 'about me handler'
print(router.lookup("/home/about")) # should print 'not found handler'
print(router.lookup("/home/about me/me")) # should print 'not found handler'
router.add_handler(None, "New root handler")
print(router.lookup(None)) # should print 'New root handler'
print(router.lookup('/')) # should print 'New root handler'

'''EXPECTED OUTPUT
root handler
root handler
root handler
not found handler
about me handler
about me handler
not found handler
not found handler
New root handler
New root handler
'''