from os.path import abspath, commonpath, isfile, join, normpath
from google.genai import types


MAX_CHARS = 10_000

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_dir_path_str: str = abspath(working_directory) 
        file_abs_path_str: str = normpath(join(working_dir_path_str, file_path))
        if not commonpath([working_dir_path_str, file_abs_path_str]) == working_dir_path_str:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not isfile(file_abs_path_str):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        with open(file_abs_path_str) as f:
            content : str = f.read(MAX_CHARS)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return content
    except Exception as e:
        return f'Error: "{e}"'
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="get the contents of a specified file relative to the working directory, limited to 10000 characters",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to read from, relative to the working directory"
            ),
        },
    ),
)