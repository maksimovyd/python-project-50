import argparse
import json



def main():
    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file", help="The first configuration file.")
    parser.add_argument("second_file", help="The second configuration file.")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    generate_diff(args.first_file, args.second_file)


if __name__ == "__main__":
    main()


def generate_diff(file_path1, file_path2):

    with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2:
        json_dict_one, json_dict_two = json.loads(file1.read()), json.loads(file2.read())

    res_str = 'gendiff ' + str(file_path1) + ' ' + str(file_path2) + '\n' + '{' + '\n'

    for key, value in sorted(json_dict_one.items() | json_dict_two.items()):
        if key in json_dict_one:
            if key in json_dict_two and json_dict_two[key] == value and json_dict_one[key] == value:
                res_str += '    ' + str(key) + ': ' + str(value) + '\n'
            elif key not in json_dict_two:
                res_str += '  ' + '-' + ' ' + str(key) + ': ' + str(value) + '\n'
            elif key in json_dict_two and json_dict_two[key] != value:
                res_str += '  ' + '-' + ' ' + str(key) + ': ' + str(value) + '\n'
                res_str += '  ' + '+' + ' ' + str(key) + ': ' + str(json_dict_two[key]) + '\n'
        elif key not in json_dict_one:
            if key in json_dict_two:
                res_str += '  ' + '+' + ' ' + str(key) + ': ' + str(value) + '\n'
    print(res_str + '}')
    return res_str + '}'



    # возвращает строки с \n в конце
