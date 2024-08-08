import os
import subprocess
import sys

if __name__ == '__main__':
    directories = set(os.path.dirname(file) for file in sys.argv[1:])
    # Spawn all in parallel since it can take a while,
    # pre-commit run --all would take several seconds otherwise.
    processes = {}
    for directory in directories:
        full_path = os.path.join(os.getcwd(), directory)
        processes[full_path] = subprocess.Popen(
            ["poetry", "check"],
            cwd=full_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    all_ok = True
    for path, process in processes.items():
        stdout, stderr = process.communicate()
        print(f"Checking {path}:")
        print(stdout.decode())
        print(stderr.decode(), file=sys.stderr)
        all_ok = all_ok and process.returncode == 0
    sys.exit(0 if all_ok else 1)