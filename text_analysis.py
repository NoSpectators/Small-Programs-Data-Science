

"""def CheckWhoWinsTheElection(A):
    A.sort()
    counter = maxCounter = 0
    candidate = maxCandidate = 0
    for i in range(0, len(A)):
        if (A[i] == candidate):
	    counter += 1
	else:
	    counter = 1
	    candidate = A[i]
	if (counter > maxCounter):
	    maxCandidate = A[i]
	    maxCounter = counter
    print maxCandidate, "appeared ", maxCounter, " times" 
A = [2, 3, 2, 1, 2, 2, 3, 2, 2]
CheckWhoWinsTheElection(A)
A = [3, 3, 3, 2, 2, 3]
CheckWhoWinsTheElection(A)"""


def countDuplicatesDict(L):
    stats = {}
    for i in L:
        if i in stats:
            stats[i] += 1
            #print 'update occurred', i, stats[i]
        else:
            stats[i] = 1
            #print 'update occurred',i, stats[i]
    return stats
    #stats = {x:L.count(x) for x in L}
    #return stats
L = ['dog','apple','red','apple','red','red','pear','dog','dog','dog','dog','dog']
dic =countDuplicatesDict(L) 
print 'stats =',dic
maximum = max(dic, key=dic.get)  # Just use 'min' instead of 'max' for minimum.
minimum = min(dic, key=dic.get)
print 'max value is',maximum,",", dic[maximum]
print 'min value is',minimum,",", dic[minimum]

print ""

def countItemsDict(L):
    stats = {x:L.count(x) for x in L}
    return stats 
L = ['camel spider','mechanic', 'package','bosbosa','camel spider','mechanic']
dic =countItemsDict(L) 
print 'stats =',dic
maximum = max(dic, key=dic.get)  # Just use 'min' instead of 'max' for minimum.
minimum = min(dic, key=dic.get)
print 'max value is',maximum,",", dic[maximum]
print 'min value is',minimum,",", dic[minimum]

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


    
