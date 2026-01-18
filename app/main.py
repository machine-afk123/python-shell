import sys


def main():
    while True:
        sys.stdout.write("$ ")
        usr_input = input()
        if usr_input:
            print(f"{usr_input}: command not found")

if __name__ == "__main__":
    main()
