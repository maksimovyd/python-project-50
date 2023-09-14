import argparse


def main():

    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file", help="The first configuration file.")
    parser.add_argument("second_file", help="The second configuration file.")
    # parser.add_argument("-h", "--help", help="Show this help message and exit.")

    args = parser.parse_args()

    print(parser.format_help())


    # if args.help:
    #     parser.print_help()
    # else:
    #     # Код для выполнения сравнения файлов
    #     print(f"Сравниваем файлы: {args.first_file} и {args.second_file}")


if __name__ == "__main__":
    main()