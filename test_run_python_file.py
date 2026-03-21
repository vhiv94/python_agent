from sys import path

path.append("functions")

from run_python_file import run_python_file


test_cases = [
    ("calculator", "main.py"),
    ("calculator", "main.py", ["3 + 5"]),
    ("calculator", "tests.py"),
    ("calculator", "../main.py"),
    ("calculator", "nonexistent.py"),
    ("calculator", "lorem.txt"),
]

def test():
    for case in test_cases:
        print(f"Result from running {case[1]}:")
        print(run_python_file(*case))
        print('')

test()