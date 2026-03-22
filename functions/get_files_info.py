from os import listdir
from os.path import commonpath, join, isdir, getsize, normpath
from posixpath import abspath
from google.genai import types


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_path_str: str = abspath(working_directory) 
        dir_abs_path_str: str = normpath(join(working_dir_path_str, directory))
        if not commonpath([working_dir_path_str, dir_abs_path_str]) == working_dir_path_str:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not isdir(dir_abs_path_str):
            return f'Error: "{directory}" is not a directory'
        return "\n".join(map(lambda f: f"- {f}: file_size={getsize(join(dir_abs_path_str, f))}, is_dir={isdir(join(dir_abs_path_str, f))}", listdir(dir_abs_path_str)))
    except Exception as e:
        return f'Error: "{e}"'
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)"
            ),
        },
    ),
)