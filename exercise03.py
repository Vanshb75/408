import re
import numpy as np
import collections
import nltk
from nltk.corpus import stopwords


myFile = open("review-1.txt", "r")

line = myFile.read()
#print (line)
line.replace("'", "")

punctuations: str = '''!()-[]{};:'",<>./?@#$%^&*_~'''
for ele in line:
        if ele in punctuations:
            line = line.replace(ele, "")

line = re.sub("(?<=[a-z])'(?=[a-z])", "", line)
line = line.lower()
#print(line)

str = line
arr = str.split()
#print(arr)

x = np.array(arr)
#print(x)

lis = x.tolist()

words = lis
stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "also", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

for i in list(words):  # iterating on a copy since removing will mess things up
    if i in stopwords:
        words.remove(i)

print(words)    # print after removing stopwords

sort = sorted(words)
print(sort)     #print after sorting

y = np.unique(sort)
#print(y)

print (collections.Counter(y))      #print after using the unique function.
print (collections.Counter(sort))   #print after counting occurences




