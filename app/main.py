import sys


def main():
    while True:
        sys.stdout.write("$ ")
        usr_input = input()
        # for every arg we want the first to be the command
        usr_input_args = usr_input.split()
        command = usr_input_args[0]
        match command:
            case "exit":
                break
            case "echo":
                # if usr_input_args[1].startswith("-"):
                #     continue
                print(" ".join(usr_input_args[1:]))
            case "":
                continue
            case _:
                print(f"{usr_input}: command not found")

if __name__ == "__main__":
    main()
