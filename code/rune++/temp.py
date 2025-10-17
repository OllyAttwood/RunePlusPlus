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
#lexer = Lexer("ᚺ⋅ᛁᛄᛁ⋅ᛧ⋅ᛁᛄ⋅ᛧ⋅ᛁᛁᛁ⋅ᛧ⋅ᛁᛄ⋅ᚢ⋅ᛁᛄ⋅ᚻ") # List create test
#lexer = Lexer("ᚺ⋅ᛁᛄᛁ⋅ᛧ⋅ᛁᛄ⋅ᛧ⋅ᛁᛁᛁ⋅ᛧ⋅ᛁᛄ⋅ᚢ⋅ᛁᛄ⋅ᚻ⋅ᛝ⋅ᛁᛄ⋅ᚢ⋅ᛁᛄ") # List indexing test
#lexer = Lexer("ᚹᛏᛁᛉᛚ⋅ᚿ⋅ᛁᛄᛁ⋅ᛆ") # native function / print test
#lexer = Lexer("ᛁᛉᚹ⋅ᚿ⋅ᛧᛧᛁᛉᚹᛟᛚᛧᛧ⋅ᛆ") # Input function test
#lexer = Lexer("ᛉᛟᛒ⋅ᚿ⋅ᛧᛧᛁᛄᛁ.ᛄᛁᛧᛧ⋅ᛆ") # Num function test (string to int/float)
#lexer = Lexer("ᛉᛟᛒ⋅ᚿ⋅ᛁᛉᚹ⋅ᚿ⋅ᛆ⋅ᛆ") # Get string input from user and then convert to number
#lexer = Lexer("ᛣᛠᛝᚹ⋅ᚲ⋅ᛁᛄ.ᛁᛄ⋅ᛚ⋅ᛁᛄ\nᛝᛠᚹᛝ⋅ᚲ⋅ᛁᛁᛄ\nᚹᛏᛁᛉᛚ⋅ᚿ⋅ᛣᛠᛝᚹ⋅ᚢ⋅ᛝᛠᚹᛝ⋅ᛆ") # New line lexer test
#lexer = Lexer("ᛁᛩ⋅ᚷ\nᛣᛠᛝᚹ⋅ᚲ⋅ᛁᛄ\nᚹᛏᛁᛉᛚ⋅ᚿ⋅ᛣᛠᛝᚹ⋅ᚢ⋅ᛁ⋅ᛆ\nᚺᛅᛁᛩ⋅ᚷ\nᛁᛄ\nᚺᛅᛣ\nᛁᛁ") # If statement test with new grammar rules
#lexer = Lexer("ᛣᛠᛝᚹ⋅ᚲ⋅ᛄ\nᛞ⋅ᛣᛠᛝᚹ⋅ᛅᚺᛣ⋅ᛁᛄᛁ\nᚹᛏᛁᛉᛚ⋅ᚿ⋅ᛣᛠᛝᚹ⋅ᛆ\nᛣᛠᛝᚹ⋅ᚲ⋅ᛣᛠᛝᚹ⋅ᚢ⋅ᛁ") # While loop test with new grammar rules
lexer = Lexer("ᛩᛟᛉᚴ⋅ᛒᛒᛒ⋅ᛟ⋅ᛧ⋅ᛟᛟ⋅ᛧ⋅ᛟᛟᛟ\nᛣᛠᛝᚹ⋅ᚲ⋅ᛟ⋅ᛚ⋅ᛟᛟ\nᛣᛠᛝᚹ⋅ᛚ⋅ᛟᛟᛟ\n\nᛒᛒᛒ⋅ᚿ⋅ᛁᛄ⋅ᛧ⋅ᛁᛁ⋅ᛧ⋅ᛁᛄᛄ⋅ᛆ") # Function declaration test with new grammar rules

lexer.lex()
print(lexer.tokens)
print("-------------------------------------------------")

parser = Parser(lexer.tokens)
ast = parser.parse_all()
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
