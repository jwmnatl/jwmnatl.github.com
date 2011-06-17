### Chapter 7: Python 101 :Jimmy Moore ###

# Ex. 7.1

file = raw_input ('Enter a file name: ')
try:
    fhand = open(file)
except:
    print 'Cannot open file : ', file
    exit()
for line in fhand:
    line = line.rstrip()
    print line.upper()
   
# Ex. 7.2

file = raw_input ('Enter a file name: ')
try:
    fhand = open(file)
except:
    print 'Cannot open file : ', file
    exit()
count = 0
vspam = 0
for line in fhand:
    line = line.rstrip()
    if line.find('X-DSPAM-Confidence:') == -1:
        continue
    value = line[line.find(':')+1:]
    value = value.strip()
    vspam = vspam + float(value)
    count = count + 1
avg = vspam/count
print 'The average spam confidence from the file', file, 'is: ', avg

# Ex. 7.3

file = raw_input ('Enter a file name: ')
if file == 'na na boo boo':
    print 'NA NA BOO BOO TO YOU - You have been punk\'d!'
    exit()
try:
    fhand = open(file)
except:
    print 'File cannot be opened: ', file
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print 'There were', count, 'subject lines in', file