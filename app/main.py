import sys


def main():
    while True:
        sys.stdout.write("$ ")
        usr_input = input()
        match usr_input:
            case "exit":
                break
            case "":
                continue
            case _:
                print(f"{usr_input}: command not found")

if __name__ == "__main__":
    main()
