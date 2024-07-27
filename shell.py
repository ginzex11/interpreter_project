# shell.py
from lexer import Lexer

while True:
    try:
        text = input('basic > ')
        lexer = Lexer(text)
        while True:
            token = lexer.get_next_token()
            print(token)
            if token.type == 'EOF':
                break
    except Exception as e:
        print(e)
