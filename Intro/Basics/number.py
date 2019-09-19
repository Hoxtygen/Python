import math
from fractions import Fraction
from decimal import Decimal


ceiling = math.ceil(2.456)
print (ceiling)

#math.copysign implementation:
def func():
     a = 5
     b = -7
     #implement copysign
     c = math.copysign(a, b)
     return c
    
print(func())#returns -5.0

def factorial(a):
  return math.factorial(a)
print(factorial(5))


print(Fraction(128, -26))
print(Fraction(344, 29))
print(Fraction(-32.75))
print(Fraction(Decimal('1.1')))