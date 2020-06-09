from Trie import Trie

## Testing it all out
# Run the following code to add some words to your trie
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

# Test Cases
print("\nThe words list is:")
print(wordList)

print("\n----------------------")
print("Checking Edge Cases...")
print("----------------------\n")
print("TEST_CASE_1: null prefix, MyTrie.find() returns None")
print(MyTrie.find(None))
print("\nTEST_CASE_2: no prefix given, find returns the trie root, suffixes returns all words")
print(MyTrie.find('').suffixes())

print("\n----------------------")
print("Checking Other Cases...")
print("----------------------\n")
print("TEST_CASE_3: Prefix: a, Suffixes:")
print(MyTrie.find('a').suffixes())
print("\nTEST_CASE_4: Prefix: ant, Suffixes:")
print(MyTrie.find('ant').suffixes())
print("\nTEST_CASE_5: Prefix: anta, Suffixes:")
print(MyTrie.find('anta').suffixes())
print("\nTEST_CASE_6: Prefix: f, Suffixes:")
print(MyTrie.find('f').suffixes())
print("\nTEST_CASE_7: Prefix: fu, Suffixes:")
print(MyTrie.find('fu').suffixes())
print("\nTEST_CASE_8: Prefix: trig, Suffixes:")
print(MyTrie.find('trig').suffixes())

'''EXPECTED OUTPUT
The words list is:
['ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function', 'factory', 'trie', 'trigger', 'trigonometry', 'tripod']

----------------------
Checking Edge Cases...
----------------------

TEST_CASE_1: null prefix, MyTrie.find() returns None
None

TEST_CASE_2: no prefix given, find returns the trie root, suffixes returns all words
['fun', 'function', 'factory', 'trigger', 'trigonometry', 'trie', 'tripod', 'ant', 'antonym', 'anthology', 'antagonist']

----------------------
Checking Other Cases...
----------------------

TEST_CASE_3: Prefix: a, Suffixes:
['nt', 'ntonym', 'nthology', 'ntagonist']

TEST_CASE_4: Prefix: ant, Suffixes:
['', 'onym', 'hology', 'agonist']

TEST_CASE_5: Prefix: anta, Suffixes:
['gonist']

TEST_CASE_6: Prefix: f, Suffixes:
['un', 'unction', 'actory']

TEST_CASE_7: Prefix: fu, Suffixes:
['n', 'nction']

TEST_CASE_8: Prefix: trig, Suffixes:
['ger', 'onometry']
'''