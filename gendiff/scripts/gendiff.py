import argparse

from gendiff.scripts.parser import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file", help="The first configuration file.")
    parser.add_argument("second_file", help="The second configuration file.")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    generate_diff(args.first_file, args.second_file, formatter='stylish')


if __name__ == "__main__":
    main()
