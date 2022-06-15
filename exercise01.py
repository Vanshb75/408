import difflib

A = "hello";

C = ["hello", "goodbye", "hola", "hello hellen","helmet", "hellorheaven", "hillsboro", "say hello", "myfellow"]

count = 0;
for i in range(0, len(C)):
    # if match found increase count
    if (A == C[i]):
        count = count + 1
print ('Number of times hello occurs as a string: ',count)   # No. of times hello occurs in the array

X = ''.join(C)
# print(X)
Y = X.count('hello')    # No. of times hello occurs in the array as a substring(word)
print ('Number of times hello occurs as a word: ',Y)

# exact string is just 1 time whereas the word hello occurs 4 times
B = "goodfellow"
print('The closest match to goodfellow in our list is',difflib.get_close_matches(B, C))


