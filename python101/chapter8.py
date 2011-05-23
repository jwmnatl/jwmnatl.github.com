### Chapter 8: Python 101 :Jimmy Moore ###

# Ex. 8.1

def chop(t):
   last = len(t)-1
   extract = t[1:last]
   
def middle(t):
	last = len(t)-1
	return t[1:last]

letters = ['a', 'b', 'c', 'd']

extract = middle(letters)
print extract

# Ex. 8.2

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
	words = line.split()
	# print 'Debug', words
	if len(words) == 0 : continue
	if words[0] != 'From' : continue
	if len(words) < 2:
		print words[1]
	else:
		print words[2]


# Ex. 8.3

fhand = open('mbox-short.txt')
for line in fhand:
	words = line.split()
	# print 'Debug', words
	if len(words) == 0 or words[0] != 'From' : continue
	if len(words) < 2:
		print words[1]
	else:
		print words[2]

# Ex. 8.4
romeo = []
fhand = open('romeo.txt')
for line in fhand:
	words = line.split()
	for word in words:
		if word in romeo : continue
		else:	
			romeo.append(word)
romeo.sort()
print romeo

# Ex. 8.5

file = raw_input('Enter a file name: ')
fhand = open(file)
count = 0
for line in fhand:
	words = line.split()
	# print 'Debug', words
	if len(words) == 0 or words[0] != 'From' : continue
	print words[1]
	count = count + 1
print 'There were ' + str(count) + ' lines in the file with From as the first word'

# Ex. 8.6

numbers = []
while True:
	try:
		input = raw_input('Enter a number: ')
		if input == 'done': break
		n = float(input)
	except:
		print 'enter only numbers, please.'
	numbers.append(n)
print 'Maximum: ' + str(max(numbers))
print 'Minimum: ' + str(min(numbers))