### Chapter 6: Python 101 :Jimmy Moore ###

# Ex. 6.1
fruit = 'banana'
index = len(fruit)-1
while index >=0:
   letter = fruit[index]
   print letter,
   index = index-1

   
# Ex. 6.2
# fruit[:] is a slice of the full string. full slice?

# Ex. 6.3
def counter(string,index):
   count =0
   for letter in string:
      if letter == index:
         count = count+1
   print count

counter('banana', 'a')

# Ex. 6.4
word = 'banana'
print word.count('a')


# Ex. 6.5
str = 'X-DSPAM-Confidence: 0.8475'
extract = str[str.find(':')+1:]
print float(extract)


# Ex. 6.6
string = 'hello, world!'
print string.capitalize() #returns Hello, world!
print string.find('lo') #returns 3
print string.isalnum() #returns false
print string.isalpha() #returns false (! is not alphanumeric)
print string.replace('hello', 'goodbye') #returns goodbye, world!
print string.strip('h!') #returns ello, world
print string.title() #returns Hello, World!
