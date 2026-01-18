from pathlib import Path
import os
from app.commands.execute import get_executable

builtins = set()

data = Path(__file__).resolve().parent.parent / "data" / "builtins.txt"

with open(data) as f:
    for command in f:
        builtins.add(command.strip())

def check_command(*args: str) -> None: 
    for command in args:
        if command in builtins:
            print(f"{command} is a shell builtin")
        elif (executable := get_executable(command)):
            print(f"{command} is {executable}")
        else:
            print(f"{command}: not found")
