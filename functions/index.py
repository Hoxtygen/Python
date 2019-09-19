def Hello():
  print('Hello, this is my first function')
  print('Can you spot the difference?')

Hello()

def greeting(lang):
  if lang == 'en':
    return 'Hello'
  elif lang == 'es':
    return 'Hola'
  else:
    return 'Bonjour'

print(greeting('gr'), 'Jean')