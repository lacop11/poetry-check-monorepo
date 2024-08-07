import os
import subprocess
import sys

if __name__ == '__main__':
    directories = set(os.path.dirname(file) for file in sys.argv[1:])
    all_ok = True
    for directory in directories:
        full_path = os.path.join(os.getcwd(), directory)
        print(f"Checking {full_path}")
        ret = subprocess.run(["poetry", "check"], cwd=full_path)
        all_ok = all_ok and ret.returncode == 0
    sys.exit(0 if all_ok else 1)