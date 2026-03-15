import gnureadline as readline
import sys
from app.utilities.load_builtin import get_builtins
from app.commands.execute import load_executable_filenames
import termios


builtins: set[str] = get_builtins()
executables: set[str] = load_executable_filenames()
all_matches = list(builtins.union(executables))

def format_matches_hook(
    substitution: str, matches: list[str], longest_match_length: int
):
    print()
    print("  ".join(matches))
    # line_buffer = readline.get_line_buffer()
    sys.stdout.write("$ ")
    sys.stdout.flush()

def longestCommonPrefix(strs: list[str]) -> str | None:
    if not strs: # edge case
        return None
    
    common = strs[0]
    for string in strs:
        l = 0; r = 0; prefix = ""
        while l < len(common) and r < len(string):
            if common[l] == string[r]:
                prefix += common[l]
                l += 1; r += 1
            else:
                break
        common = prefix
    
    return common

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
            completer.matches = builtins[:] # this is the array of all the matches

    if state >= len(completer.matches):
        return None
    else:
        if ctype in (9, 37):
            sys.stdout.write("\a")  # first time a <TAB> is pressed
            sys.stdout.flush()
        
        if len(completer.matches) > 1 and state == 0:
            return longestCommonPrefix(completer.matches)

        return completer.matches[state]


def initialize_completer():
    readline.set_completion_display_matches_hook(format_matches_hook)
    readline.parse_and_bind("set completion-query-items 0")
    readline.set_completer(completer)
    if "libedit" in readline.__doc__:
        readline.parse_and_bind("bind ^I rl_complete")
    else:
        readline.parse_and_bind("tab:complete")
