import sys
from pycloc.utils import listdir
from pycloc.utils.readlines import countlines

def main():
    dir_path = sys.argv[1]
    file_paths = listdir(dir_path)

    for path in file_paths:
        print(countlines(path))

if __name__ == "__main__":
    main()
