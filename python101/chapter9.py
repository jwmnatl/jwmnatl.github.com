### Chapter 9: Python 101 :Jimmy Moore ###

# Ex. 9.1

romeo = dict()
int = 0
fhand = open('romeo.txt')
for line in fhand:
	words = line.split()
	for word in words:
		romeo[word] = int
		int = int + 1
b = 'soft' in romeo
print b

# Ex. 9.2

def histogram(s):
	d = dict()
	for c in s:
		d[c] = d.get(c, 0) + 1 
	return d

print histogram('brontosaurus')

# Ex. 9.3

def print_hist(h):
	for c in h:
		print c, h[c]

file = raw_input('Enter a file name: ')
file = raw_input('Enter a file name: ')
try:
	fhand = open(file)
except:
	print 'File cannot be opened: ', file
	exit()
days = dict()
for line in fhand:
	words = line.split()
	# print 'Debug', words
	if len(words) == 0 or words[0] != 'From' : continue
	days[words[2]] = days.get(words[2], 0) + 1
d = print_hist(days)

# Ex. 9.4

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
	count = None
	for email in emails:
		if count is None or count < emails[email]:
			name = email
			count = emails[email]
print name, count

# Ex. 9.5
def histogram(s):
	d = dict()
	for c in s:
		d[c] = d.get(c, 0) + 1 
	return d

file = raw_input('Enter a file name: ')
try:
	fhand = open(file)
except:
	print 'File cannot be opened: ', file
	exit()
domains = dict()	
for line in fhand:
	words = line.split()
	# print 'Debug', words
	if len(words) == 0 or words[0] != 'From' : continue
	domain = words[1].split('@')[1]
	domains[domain] = domains.get(domain, 0) + 1	
print domains