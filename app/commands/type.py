from pathlib import Path
from app.commands.execute import get_executable
from app.utilities.load_builtin import get_builtins

def check_command(*args: str) -> None: 
    builtins = get_builtins()
    for command in args:
        if command in builtins:
            print(f"{command} is a shell builtin")
        elif (executable := get_executable(command)):
            print(f"{command} is {executable}")
        else:
            print(f"{command}: not found")
