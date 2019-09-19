'''
String in python is non-mutable
The * operator, of string, concatenates a given string the number of times, given
as the first argument.
'''

name = 'Harsh'
print (name)
print(name[0])
print(name[3])

multname = 4*name
print(multname)

#Slicing: Slicing, in strings, refers to removing some part of a string
inside = 'Agoraphobia'
slice = inside[4:]
slice1 = inside[:4]
slice2 = inside[-4:]
print(slice)
print(slice1)
print(slice2)

def sayName(args):
  return 'I am' + ' ' + args

print(sayName('Shola'))

bagName = 'HPpower'
bagName[4] = 'J' # returns TypeError: 'str' object does not support item assignment

    