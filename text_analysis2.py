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

"""def getWordCounts(filename):    
    with open(filename,'r') as f:        
        wordlist = [word for word in re.sub(r"\W"," ",f.read().lower()).split()]
        stats = {x:wordlist.count(x) for x in wordlist}
    #return [(key,value) for key,value in sorted(stats.items())] #returns sorted list by alphanumeric character of key     
    return [(key,stats[key]) for key in sorted(stats, key=stats.__getitem__)] #returns sorted list by value in ascending order 
word_counts = getWordCounts('John17.txt')
print word_counts 
print ""
"""

def getAverages(filename):
    with open(filename,'r') as f:        
            wordlist = [word for word in re.sub(r"\W"," ",f.read().lower()).split()]
            stats = {x:wordlist.count(x) for x in wordlist}    
            total = float(sum([i for i in stats.values()]))
            averages = {x:(wordlist.count(x)/total) for x in wordlist}
    return (stats,averages)
word_dic = getAverages('John17.txt')[0]
print word_dic 
total_averages = getAverages('John17.txt')[1]
maximum = max(total_averages, key=total_averages.get)  # Just use 'min' instead of 'max' for minimum.
minimum = min(total_averages, key=total_averages.get)
print "[max probability is: \"", maximum,"\",", total_averages[maximum], '.  min probability is: \'',minimum,"',", total_averages[minimum],"]"
print '[this is a probability space because the total sum is', sum(total_averages.values()),"]"
print 'verify :you: is in dict',word_dic['you'], 'times', 41.0/618, 'percent'



