import datetime

now = datetime.datetime.now()

def greet_player():
  print('----------', now.strftime("%d %b %Y %H:%M:%S"), '----------')
  print('')
  print('Welcome to a Password Generator coded in Python')
  print('')