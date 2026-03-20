from os import path, listdir
from utils import get_target_directory


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        dir_path_str: str = get_target_directory(working_directory, directory)
    except Exception as e:
        match e.args[0]: 
            case "OOB":
                return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
            case "INVAL":
                return f'Error: "{directory}" is not a directory'
            case _:
                return f'Error: "{e}"'

    try:
        return "\n".join(map(lambda f: f"- {f}: file_size={path.getsize(path.join(dir_path_str, f))}, is_dir={path.isdir(path.join(dir_path_str, f))}", listdir(dir_path_str)))
    except Exception as e:
        return f'Error: "{e}"'