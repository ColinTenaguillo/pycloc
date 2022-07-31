import os
from typing import List


def listdir(path: str) -> List[str]:
    listOfFiles: List[str] = list()
    for (dirpath, dirnames, filenames) in os.walk(path):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]

    return listOfFiles