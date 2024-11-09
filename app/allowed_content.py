import string

# Ask user if they want lowercase, uppercase, numbers or symbols

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
#symbols = string.punctuation
symbols = '!@#$%^&*?'

def get_allowed_content():
  allowed_content = []
  print('')
  while True:
    print('Help us figure out what you want in your password.')
    try:
      want_lowercase = input('Do you want lowercase letters? (y/n) ')

      if want_lowercase != 'y' and want_lowercase != 'n':
        print('Only y or n are allowed. Please try again.')
        continue

      want_uppercase = input('Do you want uppercase letters? (y/n) ')

      if want_uppercase != 'y' and want_uppercase != 'n':
        print('Only y or n are allowed. Please try again.')
        continue

      want_numbers = input('Do you want numbers? (y/n) ')

      if want_numbers != 'y' and want_numbers != 'n':
        print('Only y or n are allowed. Please try again.')
        continue
    
      want_symbols = input('Do you want symbols? (y/n) ')

      if want_symbols != 'y' and want_symbols != 'n':
        print('Only y or n are allowed. Please try again.')
        continue

      if want_lowercase == 'n' and want_uppercase == 'n' and want_numbers == 'n' and want_symbols == 'n':
        print('You must choose at least one option. Please try again.')
        continue

      if want_lowercase == 'y':
        allowed_content.append(lowercase)
      if want_uppercase == 'y':
        allowed_content.append(uppercase)
      if want_numbers == 'y':
        allowed_content.append(numbers)
      if want_symbols == 'y':
        allowed_content.append(symbols)

      if len(allowed_content) > 0:
        return allowed_content
    except ValueError:
      print('Only y or n are allowed. Please try again.')