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
#lexer = Lexer("ᛣᛠᛝᚹ⋅ᚲ⋅ᛁᛄ.ᛁᛄ⋅ᛚ⋅ᛁᛄ") # Variable assignment test
#lexer = Lexer("ᛣᛠᛝᚹ") # Variable access test
#lexer = Lexer("ᛁᛄᛁ⋅ᛖ⋅ᛁᛁ⋅ᚢ⋅ᛁᛄ") # Comparison operator test
#lexer = Lexer("ᚸ⋅ᛖᛏ⋅ᚷ") # Boolean data type test
#lexer = Lexer("ᛁᛩ⋅ᚷ⋅⋮⋅ᛁ⋅ᚺᛅᛁᛩ⋅ᚷ⋅⋮⋅ᛁᛄ⋅ᚺᛅᛣ⋅ᛁᛁ") # If statement test
#lexer = Lexer("ᛞ⋅ᚷ⋅ᛅᚺᛣ⋅ᛁᛄᛄᛄᛄᛄᛄᛄᛄᛄᛄᛄᛄᛄᛄᛄᛄᛄᛄᛄ⋅⋮⋅ᚷ⋅ᚲ⋅ᚷ⋅ᚢ⋅ᛁ") # While loop test
#lexer = Lexer("ᛩᛟᛉᚴ⋅ᛒᛒᛒ⋅ᛟ⋅ᛧ⋅ᛟᛟ⋅ᛧ⋅ᛟᛟᛟ⋅⋮⋅ᛟ⋅ᛚ⋅ᛟᛟ⋅ᛚ⋅ᛟᛟᛟ") # Function declaration test
#lexer = Lexer("ᛧᛧᛩᛟᛉᚴᛧᛧ⋅ᚢ⋅ᛧᛧᛒᛒᛒᛧᛧ") # String test
lexer = Lexer("ᚺ⋅ᛁᛄᛁ⋅ᛧ⋅ᛁᛄ⋅ᛧ⋅ᛁᛁᛁ⋅ᛧ⋅ᛁᛄ⋅ᚢ⋅ᛁᛄ⋅ᚻ")

lexer.lex()
print(lexer.tokens)
print("-------------------------------------------------")

parser = Parser(lexer.tokens[0])
ast = parser.parse_line()
print(ast)
print("-------------------------------------------------")

evaluator = Evaluator(ast)
context = Context("global_context", symbol_table=SymbolTable())
# True and False variables
context.symbol_table.set("ᚷ", False)
context.symbol_table.set("ᚸ", True)
#context.symbol_table.symbols["ᛣᛠᛝᚹ"] = 69
result = evaluator.traverse(context)
print(result)
print("-------------------------------------------------")

formatter = OutputFormatter(result)
formatted_result = formatter.format()
print(formatted_result)
print("-------------------------------------------------")
