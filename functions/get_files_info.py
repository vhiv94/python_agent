from os import path, listdir
from utils import get_target_path, OOBError, NotAPathError


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        dir_path_str: str = get_target_path(working_directory, directory)
        return "\n".join(map(lambda f: f"- {f}: file_size={path.getsize(path.join(dir_path_str, f))}, is_dir={path.isdir(path.join(dir_path_str, f))}", listdir(dir_path_str)))
    except OOBError:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    except NotAPathError:
        return f'Error: "{directory}" is not a directory'
    except Exception as e:
        return f'Error: "{e}"'