import re

f = raw_input('enter file name in format: Word.txt--> ') 

def getWordCounts(filename):
    f = open(filename,'r')    
    text = f.read().lower()
    f.close()									
    text = re.sub('[^a-z\ \']+', " ", text)# replaces anything that is not a lowercase letter, a space, or an apostrophe with a space:
    words = list(text.split())    
    return words 
L = getWordCounts(f)

def countItemsDict(L): #produces dictionary of words 
    stats = {x:L.count(x) for x in L}
    return stats 
dic =countItemsDict(L) 

sortedWords = [] #sorts dictionary 
for key, value in sorted(dic.iteritems(),key = lambda (k,v): (v,k)):	
	sortedWords.append((key,value))
print sortedWords 

#print 'stats =',dic
#maximum = max(dic, key=dic.get)  # Just use 'min' instead of 'max' for minimum.
#minimum = min(dic, key=dic.get)
#print 'max value is',maximum,",", dic[maximum]
#print 'min value is',minimum,",", dic[minimum]