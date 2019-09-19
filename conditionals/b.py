num = int(input('Enter a three digit number\t:'))
if ((num < 100) | (num > 999)):
  print('You have not entered a number between 100 and 999')
else:
  flag = 0
  u = num % 10
  t = int(num / 10) % 10
  h = int(num / 100) % 10
  print('u\t:', str(u), 't\t:', str(t), 'h\t:', str(h))
  rev = h + t * 10 + u * 100
  print('The number obtained by reversing the order of the digits\t:', str(rev))
  sum1 = num + rev
  print('Sum of the number and that obtained by reversing the order of digits\t:', str(sum1))
  if sum1 < 1000:
    u1 = sum1 % 10
    t1 = int(sum1 / 10) % 10
    h1 = int(sum1 / 100) % 10
    print('u1\t:', str(u1), 't1\t:', str(t1), 'h1\t:', str(h1))
  if ((u == u1) | (u == t1) | (u == h1) | (t == u1) | (t == t1) | (t == h1) | (h == u1) | (h == t1) | (h == h1)):
    print('Condition true')
    flag == 1
  else:
    u1 = sum1 % 10
    t1 = int(sum1 / 10) % 10
    h1 = int(sum1 / 100) % 10
    th1 = int(sum1 / 1000) % 10
    print('u1\t:', str(u1), 't1\t:', str(t1), 'h1\t:', str(h1), 'th1\t', str(th1))
  if ((u == u1) | (u == t1) | (u == h1) | (u == th1) | (t == u1) | (t == t1) | (t == h1) | (t == th1) | (h == u1) | (h == t1) | (h == h1) | (h == th1)):
    print('Condition true')
    flag == 1
  else:
      print('No digit of the sum is same as the original number')