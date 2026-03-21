from os.path import abspath, normpath, join, commonpath


class OOBError(BaseException):
    pass

def get_target_path(working_directory: str, target_path: str) -> str:
    """
    get an absolute path if it is within the set boundary

    Args:
        working_directory (str): A fence for keeping the function contained
        target_path (str): The desired directory or file to get the path of

    Returns:
        str: A valid path string to the desired path

    Raises:
        OOBError: If the requested path is outside the set working_directory
    """
    working_dir_path_str: str = abspath(working_directory) 
    target_path_str: str = normpath(join(working_dir_path_str, target_path))
    if not commonpath([working_dir_path_str, target_path_str]) == working_dir_path_str:
        raise OOBError()
    return target_path_str