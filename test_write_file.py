from sys import path

path.append("functions")

from write_file import write_file


test_cases = [
    ("calculator", "lorum.txt", "wait, this isn't lorem ipsum"),
    ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
    ("calculator", "/tmp/temp.txt", "this should not be allowed"),
]

def test():
    for case in test_cases:
        print("Result for current directory:") if case[1] == "." else print(f"Result for {case[1]} directory:")
        print(write_file(*case))
        print('')

test()