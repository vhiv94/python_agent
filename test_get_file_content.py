from sys import path

path.append("functions")

from get_file_content import get_file_content


test_cases = [
    ("calculator", "main.py"),
    ("calculator", "pkg/calculator.py"),
    ("calculator", "/bin/cat"),
    ("calculator", "pkg/does_not_exist.py"),
]

def test():
    for case in test_cases:
        print("Result for current directory:") if case[1] == "." else print(f"Result for {case[1]} directory:")
        print(get_file_content(*case))
        print('')

test()