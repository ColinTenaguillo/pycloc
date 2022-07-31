import sys
from pycloc.language import Language
from pycloc.utils import listdir
from pycloc.utils.countlines import countlines

def main():
    headers = ["Language", "Files", "Lines", "Codes", "Comments", "Blanks"]

    dir_path = sys.argv[1]
    file_paths = listdir(dir_path)

    language = Language("CPP")
    for path in file_paths:
        count = countlines(path)

        if count is not None:
            language.add_count(**count)

    print(language.format())

if __name__ == "__main__":
    main()
