from os.path import abspath, isfile
from subprocess import CompletedProcess, run
from utils import get_target_path, OOBError


def run_python_file(working_directory: str, file_path: str, args: list = None) -> str:
    try:
        file_abs_path_str: str = get_target_path(working_directory, file_path)
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
    except OOBError:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    except Exception as e: 
        return f'Error: executing Python file: {e}'