from lexer import Lexer
from parser import Parser
from evaluator import Evaluator
from output_formatter import OutputFormatter

"""
lexer = Lexer("ᚢ⋅ᛒ⋅ᛚ\nᚫ⋅ᚢ\nᛒ⋅ᛚ⋅ᚫ\nᚢ⋅ᛒ\nᛒᛁᛄᛁᛄ.ᛁ\nᚲ⋅ᛁ")
lexer.lex()
print(lexer.tokens)
"""

lexer = Lexer("ᛒ⋅ᛁᛄ.ᛁᛄ⋅ᛚ⋅ᚿ⋅ᛁᛄᛁ⋅ᛚ⋅ᛁᛄᛁ⋅ᚢ⋅ᛒ⋅ᛁᛄᛁ⋅ᛆ") # ᛁᛄ.ᛁᛄ * ( ᛁᛄᛁ * ᛁᛄᛁ + - ᛁᛄᛁ )
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

formatter = OutputFormatter(result)
formatted_result = formatter.format()
print(formatted_result)
print("-------------------------------------------------")
