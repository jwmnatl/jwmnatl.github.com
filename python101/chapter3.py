###Exercises for Chapter 3

#Ex. 3.1

hours = raw_input('Enter Hours Worked: ')
rate = raw_input('Enter Rate: ')
if (hours > 40):
ot = hours - 40
otpay = ot * (1.5 * rate)
pay = (40 * rate) + otpay
print 'Your pay = ' + str(pay)
else:
pay = int(hours) * float(rate)
print 'Your pay = ' + str(pay)

#Ex. 3.2

try:
input_hours = raw_input('Enter Hours Worked: ')
hours = float(input_hours)
input_rate = raw_input('Enter Rate: ')
rate = float(input_rate)
if (hours > 40):
ot = hours - 40
otpay = ot * (1.5 * rate)
pay = (40 * rate) + otpay
print 'Your pay = ' + str(pay)
else:
pay = int(hours) * float(rate)
print 'Your pay = ' + str(pay)
except:
print 'Error, please enter numeric input'

#Ex. 3.3

try:
input_score = raw_input('Enter Test Score for Grade Result: ')
score = float(input_score)

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
except:
print 'Bad score'
