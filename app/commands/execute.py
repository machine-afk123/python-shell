import os
import subprocess

def get_executable(file: str) -> str:
    paths = os.getenv("PATH", "").split(os.pathsep)
    for path in paths:
        fullPath = os.path.join(path, file)
        if os.access(fullPath, os.X_OK):
            return fullPath

    return ""

def execute(*args: str) -> None:
    file = args[0]
    fullPath = get_executable(file)
    if fullPath:
        try:
            result = subprocess.run([fullPath] + list(args[1:]), capture_output=True, text=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.cmd} exited with non-zero status {e.returncode}")
            print(e.stdout); print(e.stderr)
    else:
        print(f"{file}: command not found")
        