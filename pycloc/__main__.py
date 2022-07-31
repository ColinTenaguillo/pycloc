import sys
from pycloc.utils import listdir

def main():
    path = sys.argv[1]
    print(listdir(path))

if __name__ == "__main__":
    main()
