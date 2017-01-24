'''
Your main task for this lab is to count the number of occurrences of
words in a piece of text. More precisely, given the name of a text
file, we want to store the words that occur in the file along with
their frequency (number of occurrences).

We want to be able to perform the following operations on these collections
of key words:
- Find the "top n" words, meaning the n most frequent words; break
  ties using alphabetic order
- Given two collections, remove shared words from both
  collections
'''

class wordCounter:
    def __init__(self, file, wordDictionary):
        self.file = file
        wordDictionary = {}

    def readLines(self, file, wordDictionary):
        f = open(file, 'r')
        for line in f:
            for word in line.split():
                count = 0
                wordDictionary[word] = count
                count += 1
        return wordDictionary
            
            
'''
For testing
a = wordCounter('sample1.txt')

a.readLines('sample1.txt')
'''
