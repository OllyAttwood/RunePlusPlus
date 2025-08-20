from lexer import Lexer
from parser import Parser

"""
lexer = Lexer("ᚢ⋅ᛒ⋅ᛚ\nᚫ⋅ᚢ\nᛒ⋅ᛚ⋅ᚫ\nᚢ⋅ᛒ\nᛒᛁᛄᛁᛄ.ᛁ\nᚲ⋅ᛁ")
lexer.lex()
print(lexer.tokens)
"""

lexer = Lexer("ᛁᛄᛁᛄ⋅ᛚ⋅ᚿ⋅ᛁᛄᛁ⋅ᛚ⋅ᛁᛄᛁ⋅ᚢ⋅ᛒ⋅ᛁᛄᛁ⋅ᛆ")
lexer.lex()
print(lexer.tokens)

parser = Parser(lexer.tokens[0])
ast = parser.parse_expression()
print(ast)
