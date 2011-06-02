### Chapter 4 (Functions): Python 101 :Jimmy Moore ###

# Ex.4.1

import random

for i in range(10):
	x = random.random()
	print x

# Ex. 4.2

repeat_lyrics()
def print_lyrics():
	print "I'm a lumberjack, and I'm okay"
	print "I sleep all night and I work all day"
	
def repeat_lyrics():
	print_lyrics()
	print_lyrics()

# Error message received: NameError: name 'repeat_lyrics' is not defined

# Ex. 4.3
def repeat_lyrics():
	print_lyrics()
	print_lyrics()
	
def print_lyrics():
	print "I'm a lumberjack, and I'm okay"
	print "I sleep all night and I work all day"
		
repeat_lyrics()

# Program works


#Ex. 4.4

def computepay(hours, rate):
    if (hours > 40):
        ot = int(hours) - 40
        otpay = float(ot) * (1.5 * rate)
        pay = (40 * rate) + otpay
        print 'Your pay = ' + str(pay)
    else:
        pay = int(hours) * float(rate)
        print 'Your pay = ' + str(pay)
        
hours = float(raw_input('Enter Hours Worked: '))
rate = float(raw_input('Enter Rate: '))
computepay(hours, rate)
	

# Ex. 4.5

def computegrade(score):
	if score <= 1.0 and score >= 0.0:
		if score >= 0.9:
			grade = 'A'
		elif score >= 0.8:
			grade = 'B'
		elif score >= 0.7:
			grade = 'C'
		elif score >= 0.6:
			grade = 'D'
		else:
			grade = 'F'
		print grade
	else:
		print 'Bad score'

try:
	input_score = raw_input('Enter Test Score for Grade Result: ')
	score = float(input_score)
	computegrade(score)	
except:
	print 'Bad score'