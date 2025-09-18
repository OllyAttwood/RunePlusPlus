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
lexer = Lexer("ᛁᛄᛁ⋅ᛖ⋅ᛁᛁ⋅ᚢ⋅ᛁᛄ") # Comparison operator test

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


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MON   - variables
	- <>is VarAssignNode needed? is returning raw data types ok, rather than Number etc?
	- <> implement own version of VarAssignNode
	- <> VarAccessNode
	- implement a 'None' equivalent (not as a variable name, rather as a keyword?)
	- <> number converter not handling 69 rather than 69.0
	- <> fix failed tests
	- <> add tests for number_converter.py?
	- <> watch ep4 again to check everything is done

TUES  - <> context
	- <> understand it fully
	- <> implement

WEDS  - comparisons and logical operators
	- <> can I use the token map for keywords instead of dedicated keyword management??
	- <> implement lexer
		- <> less than
		- <> more than
		- <> equals

		- <> and
		- <> or
		- <> not
	- <> do I need a dedicated != symbol, or is not(==) ok?
	- I'm using the bitwise 'and' and 'or' functions - is this ok? I think so, so long as the operands are always booleans - could implement lambda functions instead for true and/or functionality?
	- implement True/False characters (from input as well as program output)?
	- <> TEST ALL FUNCTIONALITY

THURS - if statements

#################################################################################

https://www.geeksforgeeks.org/python/dunder-magic-methods-python/
