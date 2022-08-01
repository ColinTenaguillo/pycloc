import os
from typing import List


def listdir(path: str) -> List[str]:
    """List files in a directory and sub directories

    Args:
        path (str): path to directory

    Returns:
        List[str]: path to files in directory and subdirectory
    """    
    listOfFiles: List[str] = list()
    for (dirpath, dirnames, filenames) in os.walk(path):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]

    return listOfFiles