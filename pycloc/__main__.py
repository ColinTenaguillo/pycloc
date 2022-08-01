import os
import sys
from pycloc.config import LANGUAGES
from pycloc.utils import listdir
from pycloc.utils.better_sum import better_sum
from pycloc.utils.countlines import countlines
from tabulate import tabulate

def compute_data(path: str):
    """Compute all files in directory and subdirectories.

    Args:
        path (str): Path to directory

    Returns:
        List[List[str|int]]: Returns the list of data for each language
    """    
    file_paths = listdir(path)
    for path in file_paths:
        _filename, file_extension = os.path.splitext(path)
        try:
            language = next(v for k, v in LANGUAGES.items() if file_extension in k)
        except StopIteration:
            continue

        count = countlines(
            path, 
            language.single_line_comments, 
            language.multiline_comments_regex
        )
        if count is not None:
            language.add_count(**count)

    data = [lang.format() for lang in LANGUAGES.values() if lang.files > 0]
    sum_total = [better_sum(i) for i in zip(*data)]
    sum_total[0] = "SUM :"
    data.append(["----------", "----------", "----------", "----------", "----------", "----------"])
    data.append(sum_total)
    return data

def main():
    dir_path = sys.argv[1]
    data = compute_data(dir_path)
    headers = ["Language", "Files", "Lines", "Codes", "Comments", "Blanks"]
    table = tabulate(data, headers=headers, tablefmt="simple")

    print(table)

if __name__ == "__main__":
    main()
