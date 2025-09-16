from lexer import Lexer
from parser import Parser
from evaluator import Evaluator
from output_formatter import OutputFormatter
from context import Context, SymbolTable

"""
lexer = Lexer("ᚢ⋅ᛒ⋅ᛚ\nᚫ⋅ᚢ\nᛒ⋅ᛚ⋅ᚫ\nᚢ⋅ᛒ\nᛒᛁᛄᛁᛄ.ᛁ\nᚲ⋅ᛁ")
lexer.lex()
print(lexer.tokens)
"""

#lexer = Lexer("ᛒ⋅ᛁᛄ.ᛁᛄ⋅ᛚ⋅ᚿ⋅ᛁᛄᛁ⋅ᛚ⋅ᛁᛄᛁ⋅ᚢ⋅ᛒ⋅ᛁᛄᛁ⋅ᛆ") # ᛁᛄ.ᛁᛄ * ( ᛁᛄᛁ * ᛁᛄᛁ + - ᛁᛄᛁ )
lexer = Lexer("ᛣᛠᛝᚹ⋅ᚲ⋅ᛁᛄ.ᛁᛄ⋅ᛚ⋅ᛁᛄ")
#lexer = Lexer("ᛣᛠᛝᚹ")
lexer.lex()
print(lexer.tokens)
print("-------------------------------------------------")

parser = Parser(lexer.tokens[0])
ast = parser.parse_line()
print(ast)
print("-------------------------------------------------")

evaluator = Evaluator(ast)
context = Context("global_context", symbol_table=SymbolTable())
#context.symbol_table.symbols["ᛣᛠᛝᚹ"] = 69
result = evaluator.traverse(context)
print(result)
print("-------------------------------------------------")

formatter = OutputFormatter(result)
formatted_result = formatter.format()
print(formatted_result)
print("-------------------------------------------------")
