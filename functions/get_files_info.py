from os import listdir
from os.path import join, isdir, getsize
from utils import get_target_path, OOBError


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        dir_abs_path_str: str = get_target_path(working_directory, directory)
        if not isdir(dir_abs_path_str):
            return f'Error: "{directory}" is not a directory'
        return "\n".join(map(lambda f: f"- {f}: file_size={getsize(join(dir_abs_path_str, f))}, is_dir={isdir(join(dir_abs_path_str, f))}", listdir(dir_abs_path_str)))
    except OOBError:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    except Exception as e:
        return f'Error: "{e}"'