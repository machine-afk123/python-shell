from pathlib import Path

builtins = set()

data = Path(__file__).resolve().parent.parent / "data" / "builtins.txt"

with open(data) as f:
    for command in f:
        builtins.add(command.strip())

def check_command(*args: str) -> None: 
    for command in args:
        if command in builtins:
            print(f"{command} is a shell builtin")
        else:
            print(f"{command}: not found")
    
    return
