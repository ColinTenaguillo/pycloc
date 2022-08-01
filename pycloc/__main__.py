import os
import sys
from typing import List
from pycloc.config import LANGUAGES
from pycloc.utils import listdir
from pycloc.utils.countlines import countlines
from tabulate import tabulate

def better_sum(random_list: List):
    total = 0
    for element in random_list:
        if isinstance(element, int) or element.isdigit():
            total += int(element)

    return total


def compute_data(path: str):
    file_paths = listdir(path)
    for path in file_paths:
        _filename, file_extension = os.path.splitext(path)
        try:
            language = next(v for k, v in LANGUAGES.items() if file_extension in k)
        except StopIteration:
            pass

        count = countlines(
            path, 
            language.single_line_comments, 
            language.multiline_comments_regex
        )
        if count is not None:
            language.add_count(**count)

    data = [lang.format() for lang in LANGUAGES.values() if lang.files > 0]
    total = [better_sum(i) for i in zip(*data)]
    total[0] = "SUM :"
    data.append(total)
    return data

def main():
    dir_path = sys.argv[1]
    data = compute_data(dir_path)
    headers = ["Language", "Files", "Lines", "Codes", "Comments", "Blanks"]
    table = tabulate(data, headers=headers, tablefmt="presto")

    print(table)

if __name__ == "__main__":
    main()
