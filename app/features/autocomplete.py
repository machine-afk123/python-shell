import readline
from app.utilities.load_builtin import get_builtins
from app.commands.execute import load_executable_filenames

builtins: set[str] = get_builtins()
executables: set[str] = load_executable_filenames()
all_matches = builtins.union(executables)

def completer(text: str, state: int) -> str:
    # custom completer function
    if state == 0:
        if text:
            matches = [match for match in all_matches if match.startswith(text)]
        else:
            matches = builtins[:]

    if state > len(matches):
        # no match found
        return None
    else:
        return matches[state] + " "


def initialize_completer():
    readline.set_completer(completer)
    if "libedit" in readline.__doc__:
        readline.parse_and_bind("bind ^I rl_complete")
    else:
        readline.parse_and_bind("tab:complete")
