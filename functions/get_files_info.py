from os import path, listdir


def get_files_info(working_directory: str, directory: str = ".") -> str:
    ## validate target directory
    try:
        working_dir_abspath = path.abspath(working_directory) 
        target_dir = path.normpath(path.join(working_dir_abspath, directory))
        if not path.commonpath([working_dir_abspath, target_dir]) == working_dir_abspath:
            return RuntimeError(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        if not path.isdir(target_dir):
            return RuntimeError(f'Error: "{directory}" is not a directory')
    except Exception as e:
        return RuntimeError(f'Error:{e}\n"{working_directory}" cannot be found')
    
    ## read and format directory contents
    try:
        return "\n".join(map(lambda f: f"- {f}: file_size={path.getsize(path.join(target_dir, f))}, is_dir={path.isdir(path.join(target_dir, f))}", listdir(target_dir)))
    except Exception as e:
        return RuntimeError(f"Error: {e}")


get_files_info("calculator", ".")