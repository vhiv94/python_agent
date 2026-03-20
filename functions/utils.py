from os.path import abspath, normpath, join, commonpath, isdir, isfile

def get_target_directory(working_directory: str, directory: str) -> str:
    ## validate and return target directory
    working_dir_path_str: str = abspath(working_directory) 
    target_path_str: str = normpath(join(working_dir_path_str, directory))
    if not commonpath([working_dir_path_str, target_path_str]) == working_dir_path_str:
        raise Exception("OOB")
    if not isdir(target_path_str) and not isfile(target_path_str):
        raise Exception("INVAL")
    return target_path_str