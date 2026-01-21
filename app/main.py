import sys
from app.commands.type import check_command
from app.commands.execute import execute
from app.commands.pwd import pwd
from app.commands.cd import cd

def main():
    while True:
        sys.stdout.write("$ ")
        usr_input = input()
        usr_input_args = usr_input.split()
        command = usr_input_args[0] if usr_input_args else ""
        match command:
            case "exit":
                break
            case "echo":
                print(" ".join(usr_input_args[1:]))
            case "type":
                check_command(*usr_input_args[1:])
            case "pwd":
                pwd()
            case "cd":
                path = usr_input_args[1] if len(usr_input_args) > 1 else ""
                cd(path)
            case "":
                continue
            case _:
                execute(*usr_input_args)

if __name__ == "__main__":
    main()
