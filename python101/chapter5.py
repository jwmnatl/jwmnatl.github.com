### Chapter 5 ###

# Ex. 5.1

total = 0
count = 0
avg = 0
while True:
try:
input = raw_input('Enter a number: ')
if input == 'done':
break
n = float(input)
except:
print 'bad idea'
total = total + n
count = count + 1
avg = total/count
print int(total), int(count), float(avg)

# Ex. 5.2

total = 0
count = 0
max = 'none'
min = 'none'
while True:
try:
input = raw_input('Enter a number: ')
if input == 'done':
break
n = float(input)
except:
print 'bad idea'
total = total + n
count = count + 1
if max == 'none' or n >= max:
max = n
if min == 'none' or n <= min:
min = n
print int(total), int(count), int(max), int(min)