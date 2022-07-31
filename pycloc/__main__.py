import sys
from pycloc.utils import listdir
from pycloc.utils.countlines import countlines
from tabulate import tabulate
import pandas as pd

def main():
    headers = ["Language", "Files", "Lines", "Codes", "Comments", "Blanks"]

    dir_path = sys.argv[1]
    file_paths = listdir(dir_path)

    for path in file_paths:
        count = countlines(path)

        if count is not None:
            print(count)

    data = [[1, 'Liquid', 24, 12],
    [2, 'Virtus.pro', 19, 14],
    [3, 'PSG.LGD', 15, 19],
    [4,'Team Secret', 10, 20]]
    print(tabulate(data, headers=headers))


if __name__ == "__main__":
    main()
