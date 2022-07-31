def _count_generator(reader):
    b = reader(1024 * 1024)
    while b:
        yield b
        b = reader(1024 * 1024)

with open(r'E:\demos\files\read_demo.txt', 'rb') as fp:
    c_generator = _count_generator(fp.raw.read)
    # count each \n
    count = sum(buffer.count(b'\n') for buffer in c_generator)
    print('Total lines:', count + 1)


def main():
    print("toto")

if __name__ == "__main__":
    main()
