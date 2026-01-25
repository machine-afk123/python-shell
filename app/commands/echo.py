import re
import sys

def echo(input: str) -> None:
    input = input.replace("echo", "")
    pattern = r"'+|\"+|[\[\]]"
    splitted = re.split(pattern, input)
    sys.stdout.write("".join(splitted) + "\n")
