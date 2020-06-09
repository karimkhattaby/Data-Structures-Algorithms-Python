import sys # will be used to get the size in which a string is stored
from Huffman_Encoding import huffman_encoding
from Huffman_Decoding import huffman_decoding

# test case provided by the problem statement
a_great_sentence = "The bird is the word"
print("Performing encoding on TEST_CASE_1 a_great_sentence\n")

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))

# if the decoded sentence is exactly the same as the sentence before encoding, print True
# else, print False
print("Are the 2 sentences equal ? {}\n".format(a_great_sentence == decoded_data))

""" EXCEPTED OUTPUT
Performing encoding on TEST_CASE_1 a_great_sentence

The size of the data is: 57

The content of the data is: The bird is the word

The size of the encoded data is: 36

The content of the encoded data is: 1001001111011001100000101111110000100011010110011110110101001110101111

The size of the decoded data is: 57

The content of the encoded data is: The bird is the word

Are the 2 sentences equal ? True
"""




# test case, when all letters are the same
same_characters_sentence = "AAAAAAAAAAAAA"
print("Performing encoding on TEST_CASE_2 same_characters_sentence\n")

print ("The size of the data is: {}\n".format(sys.getsizeof(same_characters_sentence)))
print ("The content of the data is: {}\n".format(same_characters_sentence))

encoded_data, tree = huffman_encoding(same_characters_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))

print("Are the 2 sentences equal ? {}\n".format(same_characters_sentence == decoded_data))

""" EXPECTED OUTPUT
Performing encoding on TEST_CASE_2 same_characters_sentence

The size of the data is: 50

The content of the data is: AAAAAAAAAAAAA

The size of the encoded data is: 24

The content of the encoded data is: 0000000000000

The size of the decoded data is: 50

The content of the encoded data is: AAAAAAAAAAAAA

Are the 2 sentences equal ? True
"""




# test case, very large input
very_large_sentence = """Uh, wickey wild wild
Wicky wicky wild
Wickey wild, wicky wicky wild wild wild west,
Jim West, desperado, rough rider
No you don't want nada
None of this, six gun in this, brotha runnin' this,
Buffalo soldier, look it's like I told ya
Any damsel that's in distress
Be out of that dress when she meet Jim West
Rough neck so go check the law and abide
Watch your step, we'll flex and get a hole in your side
Swallow your pride, don't let your lip react,
You don't wanna see my hand where my hip be at,
With all of this, from the start of this,
Runnin' the game, James West tamin' the west so remember the name
Now who ya gonna call?
Not the G.B.'s
Now who you gon' call?
J double A G
If you have a riff with, people wanna bust, break out!
Before you get bum-rushed at the (Wild Wild West)
When I roll into the (Wild Wild West)
When I stroll into the (Wild Wild West)
When I bounce into the (Wild Wild West) Sisqo, Sisqo
We going straight to the Wild Wild West
We going straight to the Wild Wild West
Now, now, now, now once upon a time in the west
Mad man lost his damn mind in the west
Loveless, kidnap a dime, nothin' less
Now I must put his behind to the test (Can you feel me?)
Then through the shadows, in the saddle, ready for battle
Bring all your boys in, here come the poison
Behind my back, all the riffin' ya did,
Front and center, now where ya lip at kid?
Who dat is? A mean brotha, bad for your health
Lookin' damn good though, if I could say it myself
Told me Loveless is a mad man, but I don't fear that
Got mad weapons too, ain't tryin' to hear that
Tryin' to bring down me, the champion
When y'all clowns gon' see that it can't be done
Understand me son, I'm the slickest they is,
I'm the quickest as they is, did I say I'm the slickest they is
So if you barking up the wrong tree we comin', don't be startin' nothin'
Me and my partner gonna test your chest, Loveless
Can't stand the heat then get out the Wild Wild West
We going straight to (when I roll into the) the Wild Wild West (When I stroll into the)
We going straight to (when I bounce into the) the Wild Wild West
We going straight to the Wild Wild West
We going straight to the Wild Wild West
Yeah, can you feel it, c'mon c'mon, yeah
Keep it movin', keep it movin' ooh yeah
To any outlaw tryin' to draw, thinkin' you're bad,
Any draw on West best with a pen and a pad,
Don't even think about it, six gun, weighin' a ton,
10 paces and turn, just for fun, son,
Up till sundown, rolling around,
See where the bad guys ought to be found and make 'em lay down,
The defenders of the west,
Crushin' on pretenders in the west,
Don't mess with us 'cause we're in the (Wild Wild West)
Going straight to the Wild Wild West
We going straight to the Wild Wild West
We going straight to the Wild Wild West
We going straight to the Wild Wild West
We going straight to the Wild Wild West
We going straight to the Wild Wild West, c'mon
Woo, uh
(The Wild, Wild West) Ha ha ha ha
(The Wild, Wild West) Uh Dru, Dru
(The Wild, Wild West) I done done it again y'all done done it again
(The Wild, Wild West) Ha ha ha ha
(The Wild, Wild West) Big Will, Dru Hill, uh
(The Wild, Wild West) Big Will, Dru Hill ha ha ha ha
(The Wild, Wild West) The Wild Wild West
(The Wild, Wild West) Uh
(The Wild, Wild West) One time
(The Wild, Wild West) Uh,
(The Wild, Wild West) The wild wild west bring in the heat, bring in the Heat, what?
(Wild Wild West)
(The Wild, Wild West)
The wild wild wicky wickidy wild wild wild wickidy wild wild
Wickidy wild wild, the wickidy wickidy wickidy wickidy (The Wild, Wild West)
(The Wild, Wild West)
(The Wild, Wild West)
(The Wild, Wild West) Can't stop the bum-rush,
The wild wild (The Wild, Wild West)"""
print("Performing encoding on TEST_CASE_3 very_large_sentence\n")

# NOTE print was suppressed here to avoid cluttering the output area
print ("The size of the data is: {}\n".format(sys.getsizeof(very_large_sentence)))
#print ("The content of the data is: {}\n".format(very_large_sentence))

encoded_data, tree = huffman_encoding(very_large_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
#print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
#print ("The content of the encoded data is: {}\n".format(decoded_data))

print("Are the 2 sentences equal ? {}\n".format(very_large_sentence == decoded_data))

""" EXPECTED OUTPUT
Performing encoding on TEST_CASE_3 very_large_sentence

The size of the data is: 4058

The size of the encoded data is: 2356

The size of the decoded data is: 4058

Are the 2 sentences equal ? True
"""