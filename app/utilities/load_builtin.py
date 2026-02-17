from pathlib import Path
from functools import lru_cache
import os

data = Path(__file__).resolve().parent.parent / "data" / "builtins.txt"


# lazy load the builtins file
def get_builtins() -> None:
    mtime = os.path.getmtime(data)
    return load_builtins(mtime)


@lru_cache(maxsize=1)
def load_builtins(mtime: float) -> set[str]:
    builtins = set()

    with open(data) as f:
        for command in f:
            builtins.add(command.strip())

    return builtins
