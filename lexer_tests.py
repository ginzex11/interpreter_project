# test_lexer.py
import unittest
from lexer import Lexer, TokenType

class TestLexer(unittest.TestCase):
    def test_integer(self):
        lexer = Lexer("123")
        token = lexer.get_next_token()
        self.assertEqual(token.type, TokenType.INTEGER)
        self.assertEqual(token.value, 123)

    def test_float(self):
        lexer = Lexer("123.456")
        token = lexer.get_next_token()
        self.assertEqual(token.type, TokenType.FLOAT)
        self.assertEqual(token.value, 123.456)

    def test_invalid_float(self):
        with self.assertRaises(Exception):
            lexer = Lexer(".456")
            lexer.get_next_token()
        with self.assertRaises(Exception):
            lexer = Lexer("123.")
            lexer.get_next_token()

    def test_arithmetic_operators(self):
        lexer = Lexer("+-*/%")
        tokens = [lexer.get_next_token() for _ in range(5)]
        token_types = [TokenType.PLUS, TokenType.MINUS, TokenType.MUL, TokenType.DIV, TokenType.MOD]
        for token, expected_type in zip(tokens, token_types):
            self.assertEqual(token.type, expected_type)

    def test_boolean_operators(self):
        lexer = Lexer("&& || !")
        tokens = [lexer.get_next_token() for _ in range(3)]
        token_types = [TokenType.AND, TokenType.OR, TokenType.NOT]
        for token, expected_type in zip(tokens, token_types):
            self.assertEqual(token.type, expected_type)

    def test_comparison_operators(self):
        lexer = Lexer("== != > < >= <=")
        tokens = [lexer.get_next_token() for _ in range(6)]
        token_types = [TokenType.EQ, TokenType.NEQ, TokenType.GT, TokenType.LT, TokenType.GTE, TokenType.LTE]
        for token, expected_type in zip(tokens, token_types):
            self.assertEqual(token.type, expected_type)

    def test_parentheses(self):
        lexer = Lexer("()")
        tokens = [lexer.get_next_token() for _ in range(2)]
        token_types = [TokenType.LPAREN, TokenType.RPAREN]
        for token, expected_type in zip(tokens, token_types):
            self.assertEqual(token.type, expected_type)

    def test_defun_and_lambda(self):
        lexer = Lexer("{ .")
        tokens = [lexer.get_next_token() for _ in range(2)]
        token_types = [TokenType.DEFUN, TokenType.LAMBDA]
        for token, expected_type in zip(tokens, token_types):
            self.assertEqual(token.type, expected_type)

if __name__ == '__main__':
    unittest.main()
