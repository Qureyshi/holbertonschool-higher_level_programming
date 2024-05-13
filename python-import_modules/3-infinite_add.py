#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    length = len(argv) - 1
    c = 0
    if length == 0:
        print(c)
    else:
        for i in range(length):
            c += int(argv[i + 1])
        print("{}".format(c))
