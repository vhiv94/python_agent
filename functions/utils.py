from os.path import abspath, normpath, join, commonpath, isdir, isfile

class OOBError(BaseException):
    pass

class NotAPathError(BaseException):
    pass

def get_target_path(working_directory: str, path: str) -> str:
    """
    validate and return target directory

    get an absolute path contained to a desired directory

    Args:
        working_directory (str): A fence for keeping the function contained
        path (str): The desired directory or file to get the path of

    Returns:
        str: A valid path string to the desired path

    Raises:
        OOBError: If the requested path is outside the set working_directory
        NotAPathError: If the requested path is neither a file or directory
    """
    working_dir_path_str: str = abspath(working_directory) 
    target_path_str: str = normpath(join(working_dir_path_str, path))
    if not commonpath([working_dir_path_str, target_path_str]) == working_dir_path_str:
        raise OOBError()
    if not isdir(target_path_str) and not isfile(target_path_str):
        raise NotAPathError()
    return target_path_str