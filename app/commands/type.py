from pathlib import Path
import os

builtins = set()

data = Path(__file__).resolve().parent.parent / "data" / "builtins.txt"

with open(data) as f:
    for command in f:
        builtins.add(command.strip())

def get_executable(command: str) -> str:
    paths = os.getenv("PATH", "").split(os.pathsep)
    for path in paths:
        fullPath = os.path.join(path, command)
        if os.access(fullPath, os.X_OK):
            return fullPath

    return ""

def check_command(*args: str) -> None: 
    for command in args:
        if command in builtins:
            print(f"{command} is a shell builtin")
        elif (executable := get_executable(command)):
            print(f"{command} is {executable}")
        else:
            print(f"{command}: not found")
