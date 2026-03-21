from os import makedirs
from os.path import dirname, isdir
from utils import get_target_path, OOBError



def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        file_abs_path_str: str = get_target_path(working_directory, file_path)
        if isdir(file_abs_path_str):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        makedirs(dirname(file_abs_path_str), exist_ok=True)
        with open(file_abs_path_str, "w") as f:
            count = f.write(content)
        return f'Successfully wrote to "{file_path}" ({count} characters written)'
    except OOBError:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    except Exception as e:
        return f'Error: writing file: {e}'