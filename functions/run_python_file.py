from os.path import abspath, commonpath, isfile, join, normpath
from subprocess import CompletedProcess, run
from google.genai import types


def run_python_file(working_directory: str, file_path: str, args: list = None) -> str:
    try:
        working_dir_path_str: str = abspath(working_directory) 
        file_abs_path_str: str = normpath(join(working_dir_path_str, file_path))
        if not commonpath([working_dir_path_str, file_abs_path_str]) == working_dir_path_str:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not isfile(file_abs_path_str):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_abs_path_str.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        command: list[str] = ["python", file_abs_path_str]
        if args:
            command.extend(args)
        completed_process: CompletedProcess = run(command, cwd=abspath(working_directory), capture_output=True, text=True, timeout=30)
        result: str = f"Process exited with code {completed_process.returncode}" if completed_process.returncode > 0 else ""
        if completed_process.stdout == "" and completed_process.stderr == "":
            return str + "No output produced"
        result += f'\nSTDOUT:{completed_process.stdout}' if completed_process.stdout else ""
        result += f'\nSTDERR:{completed_process.stderr}' if completed_process.stderr else ""
        return result
    except Exception as e: 
        return f'Error: executing Python file: {e}'
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="run a specified python script relative to the working directory with specified arguments",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path run, relative to the working directory"
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="the list of arguments to be passed to the main function call of the file, each argument should be a STRING and this function will parse out the actual type",
                items=types.Schema(
                    type=types.Type.STRING
                )
            ),
        },
    ),
)