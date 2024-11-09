

# Ask user how long password should be
def get_password_length():
  while True:
    print('')
    password_length = input('How long do you want your password to be? ')
    try:
      password_length = int(password_length)
      return password_length
    except ValueError:
      print('Only numbers are allowed. Please try again.')