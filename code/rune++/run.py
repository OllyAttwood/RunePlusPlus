"""Run scripts using the functions in this module"""
from lexer import Lexer
from parser import Parser
from evaluator import Evaluator
from output_formatter import OutputFormatter
import global_context_setup
import sys

def run_from_string(code_str):
    """
    Runs the Rune++ code that is given as a string. Sets up a new context each time this
    function is called.
    """
    lexer = Lexer(code_str)
    lexer.lex()
    parser = Parser(lexer.tokens)
    ast = parser.parse_all()
    evaluator = Evaluator(ast)
    global_context = global_context_setup.init_global_context()
    result = evaluator.traverse(global_context)
    formatter = OutputFormatter(result)
    formatted_result = formatter.format()
    print(formatted_result)

def run_from_file_path(file_path):
    """
    Runs the Rune++ code that is saved at the given location. Sets up a new context each
    time this function is called.
    """
    with open(file_path) as code_file:
        code_str = code_file.read()

        # Remove trailing new line if there is one
        if code_str[-1] == "\n":
            code_str = code_str[:-1]

        run_from_string(code_str)

def run_from_command_line():
    """
    Runs the Rune++ code that is saved at the given location (provided as a command line
    argument e.g. 'python3 run.py "/home/docs/example.py"'). Sets up a new context each
    time this function is called.
    """
    # The two args are the 'run.py' file name (we ignore this) and the file path
    if len(sys.argv) != 2:
        print("One command line argument should be provded to run.py (the file path)")
    else:
        run_from_file_path(sys.argv[1])

# Runs if the module is called from the command line e.g. 'python3 run.py "/home/docs/example.py"'
if __name__ == "__main__":
    run_from_command_line()
