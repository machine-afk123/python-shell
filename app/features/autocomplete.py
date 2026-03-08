import readline
import sys
from app.utilities.load_builtin import get_builtins
from app.commands.execute import load_executable_filenames
import termios


builtins: set[str] = get_builtins()
executables: set[str] = load_executable_filenames()
all_matches = builtins.union(executables)


def format_matches_hook(
    substitution: str, matches: list[str], longest_match_length: int
):
    for match in sorted(matches):
        print(match, end="  ", flush=True)
    print()

    # buf = readline.get_line_buffer()
    readline.clear_history()
    sys.stdout.write("$ ")
    sys.stdout.flush()


def completer(text: str, state: int) -> str:
    # custom completer function
    # when a second tab is pressed readline starts a new completion event and state is reset to 0
    ctype = readline.get_completion_type()
    if state == 0:
        if text:
            completer.matches = [
                match for match in all_matches if match.startswith(text)
            ]
        else:
            completer.matches = builtins[:]

    if state > len(completer.matches):
        return
    else:
        if ctype in (9, 37):
            sys.stdout.write("\a")  # first time a <TAB> is pressed
            sys.stdout.flush()
        return completer.matches[state]


def initialize_completer():
    readline.set_completion_display_matches_hook(format_matches_hook)
    readline.parse_and_bind("set completion-query-items 0")
    readline.set_completer(completer)
    if "libedit" in readline.__doc__:
        readline.parse_and_bind("bind ^I rl_complete")
    else:
        readline.parse_and_bind("tab:complete")
