from functions.get_files_info import get_files_info


test_cases = [
    ("calculator", "."),
    ("calculator", "pkg"),
    ("calculator", "/bin"),
    ("calculator", "../"),
]

def test():
    for case in test_cases:
        print("Result for current directory:") if case[1] == "." else print(f"Result for {case[1]} directory:")
        print(get_files_info(*case))
        print('')

test()