from utils import get_target_directory
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        file_path_str: str = get_target_directory(working_directory, file_path)
    except Exception as e:
        match e.args[0]: 
            case "OOB":
                return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
            case "INVAL":
                return f'Error: File not found or is not a regular file: "{file_path}"'
            case _:
                return f'Error: "{e}"'
            
    try:
        with open(file_path_str) as f:
            content : str = f.read(MAX_CHARS)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return content
    except Exception as e:
        return f'Error: "{e}"'