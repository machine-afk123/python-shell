import re
import sys
import shlex

def echo(input: str) -> None:
    input = input.replace("echo", "", 1)
    lexer = shlex.shlex(input, posix=True)
    lexer.whitespace_split = True
    lexer.whitespace = " \t\r\n"
    lexer.quotes = "'\""

    tokens = list(lexer)

    cleaned = " ".join(tokens)
    sys.stdout.write(cleaned + "\n")
    