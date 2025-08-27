from lexer import Lexer
from parser import Parser
from evaluator import Evaluator

"""
lexer = Lexer("ᚢ⋅ᛒ⋅ᛚ\nᚫ⋅ᚢ\nᛒ⋅ᛚ⋅ᚫ\nᚢ⋅ᛒ\nᛒᛁᛄᛁᛄ.ᛁ\nᚲ⋅ᛁ")
lexer.lex()
print(lexer.tokens)
"""

lexer = Lexer("ᛁᛄ.ᛁᛄ⋅ᛚ⋅ᚿ⋅ᛁᛄᛁ⋅ᛚ⋅ᛁᛄᛁ⋅ᚢ⋅ᛒ⋅ᛁᛄᛁ⋅ᛆ") # ᛁᛄ.ᛁᛄ * ( ᛁᛄᛁ * ᛁᛄᛁ + - ᛁᛄᛁ )
lexer.lex()
print(lexer.tokens)
print("-------------------------------------------------")

parser = Parser(lexer.tokens[0])
ast = parser.parse_line()
print(ast)
print("-------------------------------------------------")

evaluator = Evaluator(ast)
result = evaluator.traverse()
print(result)
print("-------------------------------------------------")

OUTPUT FORMATTER (convert back to runes)
------------------------------------------------      TEST WITH MANY DIFFERENT OUTPUTS - IMPLEMENT PYTEST ALSO      -------------------------------------------------------
print("-------------------------------------------------")
