"""Post_gen_project.py."""
# import os
import sys


def set_python_version():
    """Set_python_version."""
    python_version = str(sys.version_info.major) + "." + str(sys.version_info.minor)

    file_names = ["pyproject.toml"]
    for file_name in file_names:
        with open(file_name, encoding="utf-8") as f:
            contents = f.read()
            contents = contents.replace(r"{python_version}", python_version)
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(contents)


SUCCESS = "\x1b[1;32m"
INFO = "\x1b[1;33m"
TERMINATOR = "\x1b[0m"


def main():
    """Main."""
    set_python_version()
    print(SUCCESS + "Project successfully initialized" + TERMINATOR)


if __name__ == "__main__":
    main()
