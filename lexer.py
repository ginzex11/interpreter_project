# lexer.py
import re

class TokenType:
    INTEGER = 'INTEGER'
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
        self.pos = 0
        self.current_char = self.text[self.pos]

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            if self.current_char.isdigit():
                return Token(TokenType.INTEGER, self.integer())
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
                return Token(TokenType.LAMBDA)
            self.error()

        return Token(TokenType.EOF)

    def error(self):
        raise Exception('Invalid character')



