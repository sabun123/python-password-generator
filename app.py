# 9 November 2024 Yusuf Ismail Shukor

from app.greet import greet_player
from app.generate_password import generate_passwordv2
from app.allowed_content import get_allowed_content

greet_player()

allowed_content = get_allowed_content()

generated_password = generate_passwordv2(allowed_content)
print('Here is the password you have generated: ', generated_password)