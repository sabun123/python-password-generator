import random
from app.password_length import get_password_length

def generate_passwordv2(given_content):
  password_length = get_password_length()
  password = ''

  for index in range(password_length):
    content = random.choice(given_content)
    random_letter_index = random.randint(0, len(content) - 1)
    random_letter = content[random_letter_index]
    password = password + random_letter

  return password