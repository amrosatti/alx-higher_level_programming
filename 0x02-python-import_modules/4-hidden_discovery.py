#!/usr/bin/python3
import hidden_4


def main():
    for name in dir(hidden_4):
        if name[0] == '_':
            continue

        print(name)


if __name__ == "__main__":
    main()
