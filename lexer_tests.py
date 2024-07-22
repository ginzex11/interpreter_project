import unittest
from lexer import Lexer, Token, TokenType

class TestLexer(unittest.TestCase):
    def assertTokens(self, lexer, expected_tokens):
        tokens = []
        while True:
            token = lexer.get_next_token()
            tokens.append(token)
            if token.type == TokenType.EOF:
                break
        self.assertEqual(tokens, expected_tokens)

    def test_integer(self):
        lexer = Lexer('123 456')
        self.assertTokens(
            lexer,
            [
                Token(TokenType.INTEGER, 123),
                Token(TokenType.INTEGER, 456),
                Token(TokenType.EOF)
            ]
        )

    def test_operators(self):
        lexer = Lexer('+ - * / % && || != == > >= < <=')
        self.assertTokens(
            lexer,
            [
                Token(TokenType.PLUS),
                Token(TokenType.MINUS),
                Token(TokenType.MUL),
                Token(TokenType.DIV),
                Token(TokenType.MOD),
                Token(TokenType.AND),
                Token(TokenType.OR),
                Token(TokenType.NEQ),
                Token(TokenType.EQ),
                Token(TokenType.GT),
                Token(TokenType.GTE),
                Token(TokenType.LT),
                Token(TokenType.LTE),
                Token(TokenType.EOF)
            ]
        )

    def test_parentheses_and_braces(self):
        lexer = Lexer('() { .')
        self.assertTokens(
            lexer,
            [
                Token(TokenType.LPAREN),
                Token(TokenType.RPAREN),
                Token(TokenType.DEFUN),
                Token(TokenType.LAMBDA),
                Token(TokenType.EOF)
            ]
        )

    def test_error(self):
        lexer = Lexer('a')
        with self.assertRaises(Exception):
            lexer.get_next_token()

if __name__ == '__main__':
    unittest.main()
