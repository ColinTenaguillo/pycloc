import sys
from pycloc.language import Language
from pycloc.utils import listdir
from pycloc.utils.countlines import countlines
from tabulate import tabulate

def get_summary(path: str):
    file_paths = listdir(path)

    language = Language("CPP")
    for path in file_paths:
        count = countlines(path)

        if count is not None:
            language.add_count(**count)

    return language.format()

def main():
    headers = ["Language", "Files", "Lines", "Codes", "Comments", "Blanks"]

    dir_path = sys.argv[1]
    data = get_summary(dir_path)
    
    table = tabulate([data, data], headers=headers, tablefmt="presto")
    print(table)
    print(table)

if __name__ == "__main__":
    main()
