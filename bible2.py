import re

"""from collections import defaultdict

def wordCounts(filename):
    wordCounts = defaultdict(int)
    with open(filename,'r') as f:
        for word in re.sub(r"\W"," ",f.read().lower()).split():
            wordCounts[word]+=1
    return [(key,value) for key,value in sorted(wordCounts.items())] #returns sorted list by alphabetic character (word, occurrences)
    #return [(key, wordCounts[key]) for key in sorted(wordCounts, key=wordCounts.__getitem__)] #returns sorted list of tuples (word, occurrences)

print [pair for pair in wordCounts('John17.txt')]"""

def getWordCounts(filename):    
    wordlist = []
    with open(filename,'r') as f:        
        #for word in re.sub(r"\W"," ",f.read().lower()).split():
            #wordlist.append(word)
        wordlist = [word for word in re.sub(r"\W"," ",f.read().lower()).split()]
        stats = {x:wordlist.count(x) for x in wordlist}
        #return [(key,value) for key,value in sorted(stats.items())] #returns sorted list by alphanumeric character of key
    return [(key,stats[key]) for key in sorted(stats, key=stats.__getitem__)] #returns sorted list by value in ascending order 

print getWordCounts('John17.txt')


