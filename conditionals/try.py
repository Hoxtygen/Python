ast = "Hello Maxime"
try:
  istr = int(ast)
except:
  istr = -1
print('first', istr)

ast = '123'
try:
  istr = int(ast)
except:
  istr = -1
print('Second', istr)