rawStr = input('Enter a number:\n')
try:
  ival = int(rawStr)
except:
  ival = -1
if ival > 0 :
  print('nice work')
else:
  print('Not a number')