from os.path import isdir
from utils import get_target_path, OOBError, NotAPathError



def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        file_path_str: str = get_target_path(working_directory, file_path)
        if isdir(file_path_str):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        with open(file_path_str) as f:
            f.write(content)
    except OOBError:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    except NotAPathError:
        return f'Error: File not found or is not a regular file: "{file_path}"'
    except Exception as e:
        return f'Error: "{e}"'