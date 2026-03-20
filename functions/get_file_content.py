from utils import get_target_path
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        file_path_str: str = get_target_path(working_directory, file_path)
        with open(file_path_str) as f:
            content : str = f.read(MAX_CHARS)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return content
    except FileNotFoundError:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    except NotADirectoryError:
        return f'Error: File not found or is not a regular file: "{file_path}"'
    except Exception as e:
        return f'Error: "{e}"'