### Chapter 10 (Tuples): Python 101 :Jimmy Moore ###

# Ex.10.1

file = raw_input('Enter a file name: ')
try:
	fhand = open(file)
except:
	print 'File cannot be opened: ', file
	exit()	
emails = dict()
for line in fhand:
	words = line.split()
	# print 'Debug', words
	if len(words) == 0 or words[0] != 'From' : continue
	emails[words[1]] = emails.get(words[1], 0) + 1	
	lst = []
	for key, val in sorted(emails.items()):
		lst.append((val,key))
	lst.sort(reverse=True)
for key, val in lst[:1]:
	print key, val
	
# Ex.10.2

file = raw_input('Enter a file name: ')
try:
	fhand = open(file)
except:
	print 'File cannot be opened: ', file
	exit()	
emails = dict()
for line in fhand:
	words = line.split()
	# print 'Debug', words
	if len(words) == 0 or words[0] != 'From' : continue
	hour = words[5].split(':')
	emails[hour[0]] = emails.get(hour[0], 0) + 1	
	lst = []
	for key, val in sorted(emails.items()):
		lst.append((val,key))
for key, val in lst:
	print val, key
	
# Ex. 10.3

import string

def most_frequent(f):
	letters = dict()
	for line in fhand:
		line = line.translate(None, string.punctuation)
		line = line.translate(None, ' ')
		line = line.lower()
		line = line.translate(None, '0123456789')
		line = line.strip()
		for letter in line:
			letters[letter] = letters.get(letter, 0) + 1
		lst = list()
		for key, val in letters.items():
			lst.append((val,key))
		lst.sort(reverse=True)
	return lst
	
file = raw_input('Enter a file name: ')
try:
	fhand = open(file)
except:
	print 'File cannot be opened: ', file
	exit()	
rslt = most_frequent(fhand)
for key, val in rslt[0:25]:
	print key, val
		