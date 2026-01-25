import os
from pathlib import Path

def cd(path: str) -> None:
    path = path.strip()
    if path == "~":
        path = os.getenv("HOME")

    new_path = Path(path).resolve()
    if new_path.is_dir() and new_path.exists():
        os.chdir(new_path)
    else:
        print(f"cd: {path}: No such file or directory")
