import re
import sys

def echo(input: str) -> None:
    input = input.replace("echo", "")
    pattern = r"'+|\"+|[\[\]]"
    splitted = re.split(pattern, input)
    splitted = [s.strip() for s in splitted if s]
    sys.stdout.write("".join(splitted) + "\n")
