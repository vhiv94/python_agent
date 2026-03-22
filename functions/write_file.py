from os import makedirs
from os.path import commonpath, dirname, isdir, join, normpath
from posixpath import abspath
from google.genai import types



def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_dir_path_str: str = abspath(working_directory) 
        file_abs_path_str: str = normpath(join(working_dir_path_str, file_path))
        if not commonpath([working_dir_path_str, file_abs_path_str]) == working_dir_path_str:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if isdir(file_abs_path_str):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        makedirs(dirname(file_abs_path_str), exist_ok=True)
        with open(file_abs_path_str, "w") as f:
            count = f.write(content)
        return f'Successfully wrote to "{file_path}" ({count} characters written)'
    except Exception as e:
        return f'Error: writing file: {e}'
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="overwrite a specified file relative to the working directory with specified content",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path", "content"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to overwrite, relative to the working directory"
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="the new contents to be written to the file"
            ),
        },
    ),
)