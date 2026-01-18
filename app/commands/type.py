builtins = set()

with open("./data/builtins.txt") as f:
    for command in f:
        builtins.add(command.strip())

def check_command(*args: str) -> None:
    if not args:
        return 
    for command in args:
        if command in builtins:
            print(f"{command} is a shell builtin")
        else:
            print(f"{command}: command not found")
