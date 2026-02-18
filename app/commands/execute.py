import os
import subprocess
import sys


def get_executable_path(file: str, absolute: bool = True) -> str:
    paths = os.getenv("PATH", "").split(os.pathsep)
    for path in paths:
        fullPath = os.path.join(path, file)
        if os.access(fullPath, os.X_OK):
            if not absolute:
                return file
            return fullPath

    return ""


def load_executable_filenames() -> set[str]:
    paths = os.getenv("PATH", "").split(os.pathsep)
    executable_contents = set()
    for dir in paths:
        if os.path.isdir(dir):
            contents = os.listdir(dir)
            executables = {
                content
                for content in contents
                if (os.access(os.path.join(dir, content), os.X_OK))
            }
            executable_contents.update(executables)
    return executable_contents


def execute(*args: str) -> None:
    file = args[0]
    fullPath = get_executable_path(file)
    if fullPath:
        try:
            result = subprocess.run(
                [file] + list(args[1:]), capture_output=True, text=True
            )
            sys.stdout.write(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.cmd} exited with non-zero status {e.returncode}")
            print(e.stdout)
            print(e.stderr)
    else:
        print(f"{file}: command not found")
