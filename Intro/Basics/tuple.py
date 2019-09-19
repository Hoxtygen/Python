'''
A tuple contains elements which can be treated individually or as a group. A
tuple (say (x, y)) can be printed using the standard print( ) function. The elements
of a tuple can be accessed by assigning it to a tuple.
Tuples are immutable.
'''

tup1 = (2, 4)
print(tup1)
(x, y) = tup1
print('First element is', x)
print("Second element is", y)
#How to bypass the immutability of tuple
#1 . Convert the tuple to a list
tuple_list = list(tup1)

#2. Append more elements to the list
tuple_list.append(100)
tuple_list.append(10)
tuple_list.append('hello')

#3. Convert back to tuple
tup7 = tuple(tuple_list)
print(tup7)
#(a, b, c, d, e) = tup7 //complaining


l = 45
m = 48
n = 'world'

tup2 = (l, m, n)
(k, v, f)  = tup2

tup100 = ('5', 56, 99)
a = tup100
b = 'atom'
new = (*a, b)
print(new)
tupme = tup7+tup100
#print(tupme)
(a) = tupme
print(a)

# A program to swap two numbers using tuple
''' 
print('Enter the first number\t:')
num1 = int(input())
print('Enter the second number\t:')
num2 = int(input())
print('The numbers entered are', num1, '&', num2)
(num1, num2) = (num2, num1)
print('The numbers entered are now ', num1, '&', num2)

'''