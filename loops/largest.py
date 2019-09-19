def largest(list):
  largeNum = 0
  for i in list:
      if i > largeNum:
          largeNum = i
  print (largeNum)
  return largeNum


largest([2, 5, 89, 100, 76, 675, 98778])