from os import makedirs
from os.path import abspath, normpath, join, commonpath, dirname, isdir
# from utils import get_target_path, OOBError, NotAPathError



def write_file(working_directory: str, file_path: str, content: str) -> str:
    # try:
    #     file_path_str: str = get_target_path(working_directory, file_path)
    #     if isdir(file_path_str):
    #         return f'Error: Cannot write to "{file_path}" as it is a directory'
    #     with open(file_path_str, "w") as f:
    #         count = f.write(content)
    #     return f'Successfully wrote to "{file_path}" ({count} characters written)'
    # except OOBError:
    #     return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    # except NotAPathError:
    #     makedirs(normpath(join(abspath(working_directory), dirname(file_path))), exist_ok=True)
    #     write_file(working_directory, file_path, content)
    # except Exception as e:
    #     return f'Error: "{e}"'
    try:
        working_dir_path_str: str = abspath(working_directory) 
        target_path_str: str = normpath(join(working_dir_path_str, file_path))
        if not commonpath([working_dir_path_str, target_path_str]) == working_dir_path_str:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if isdir(target_path_str):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        makedirs(dirname(target_path_str), exist_ok=True)
        with open(target_path_str, "w") as f:
            count = f.write(content)
        return f'Successfully wrote to "{file_path}" ({count} characters written)'
    except Exception as e:
        return f'Error: "{e}"'