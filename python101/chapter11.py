### Chapter 11: Python 101 :Jimmy Moore ###

# Ex. 11.1

import re
count = 0
rexp = raw_input ('Enter a regular expression: ')
try:
    hand = open('mbox.txt')
except:
    print 'File cannot be opened'
    exit()
    
for line in hand:
    line = line.rstrip()
    x = re.findall(rexp, line)
    if x: count +=1

print 'mbox.txt had '+ str(count) + ' lines that matched ' + rexp

# Ex. 11.2

import re
revisions = []
try:
    hand = open('mbox.txt')
except:
    print 'File cannot be opened'
    exit()
    
for line in hand:
    line = line.rstrip()
    x = re.findall('^New Revision: ([0-9.]+)', line)
    if x : 
        revisions.append(int(x[0]))
        
print 'Average: ' + str((sum(revisions)/len(revisions)))

