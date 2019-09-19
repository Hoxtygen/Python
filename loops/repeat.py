def repeat(num):
    while num > 0:
      print(num)
      num = num - 1
    print('fuckoff')
    print(num)

# repeat(5)

def amies():
    friends = ['Matthew', 'Remi', 'Tigran', 'Benjamin']
    for friend in friends:
      print('Happy new year ', friend)
      if friend == 'Remi':
        break
    print('Done')

amies()