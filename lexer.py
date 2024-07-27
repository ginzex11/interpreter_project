# lexer.py
class TokenType:
    INTEGER = 'INTEGER'
    FLOAT = 'FLOAT'
    BOOLEAN = 'BOOLEAN'
    IDENTIFIER = 'IDENTIFIER'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    MUL = 'MUL'
    DIV = 'DIV'
    MOD = 'MOD'
    AND = 'AND'
    OR = 'OR'
    NOT = 'NOT'
    EQ = 'EQ'
    NEQ = 'NEQ'
    GT = 'GT'
    LT = 'LT'
    GTE = 'GTE'
    LTE = 'LTE'
    LPAREN = 'LPAREN'
    RPAREN = 'RPAREN'
    LAMBDA = 'LAMBDA'
    DEFUN = 'DEFUN'
    EOF = 'EOF'

class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)})"

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def number(self):
        result = ''
        dot_count = 0
        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
            if self.current_char == '.':
                dot_count += 1
                if dot_count > 1:
                    self.error()
            result += self.current_char
            self.advance()
        if result.startswith('.') or result.endswith('.'):
            self.error()
        if dot_count == 0:
            return Token(TokenType.INTEGER, int(result))
        else:
            return Token(TokenType.FLOAT, float(result))

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            if self.current_char.isdigit() or self.current_char == '.':
                return self.number()
            if self.current_char == '+':
                self.advance()
                return Token(TokenType.PLUS)
            if self.current_char == '-':
                self.advance()
                return Token(TokenType.MINUS)
            if self.current_char == '*':
                self.advance()
                return Token(TokenType.MUL)
            if self.current_char == '/':
                self.advance()
                return Token(TokenType.DIV)
            if self.current_char == '%':
                self.advance()
                return Token(TokenType.MOD)
            if self.current_char == '&':
                self.advance()
                if self.current_char == '&':
                    self.advance()
                    return Token(TokenType.AND)
            if self.current_char == '|':
                self.advance()
                if self.current_char == '|':
                    self.advance()
                    return Token(TokenType.OR)
            if self.current_char == '!':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token(TokenType.NEQ)
                return Token(TokenType.NOT)
            if self.current_char == '=':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token(TokenType.EQ)
            if self.current_char == '>':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token(TokenType.GTE)
                return Token(TokenType.GT)
            if self.current_char == '<':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token(TokenType.LTE)
                return Token(TokenType.LT)
            if self.current_char == '(':
                self.advance()
                return Token(TokenType.LPAREN)
            if self.current_char == ')':
                self.advance()
                return Token(TokenType.RPAREN)
            if self.current_char == '{':
                self.advance()
                return Token(TokenType.DEFUN)
            if self.current_char == '.':
                self.advance()
                if self.current_char.isdigit():
                    return self.number()
                self.error()
            if self.current_char.isalpha():
                return self.identifier()
            self.error()

        return Token(TokenType.EOF)

    def identifier(self):
        result = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        return Token(TokenType.IDENTIFIER, result)

    def error(self):
        raise Exception(f"Invalid character: '{self.current_char}'")
