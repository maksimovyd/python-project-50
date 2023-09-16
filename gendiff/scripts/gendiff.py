import argparse
import json
import os


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file", help="The first configuration file.")
    parser.add_argument("second_file", help="The second configuration file.")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    generate_diff(args.first_file, args.second_file)


if __name__ == "__main__":
    main()


def generate_diff(file_path1, file_path2):
    with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2:
        json_dict_one = json.loads(file1.read())
        json_dict_two = json.loads(file2.read())
    res_str = generate_result_string_dif(
        file_path1, file_path2, json_dict_one, json_dict_two
        )
    print(res_str + '}')
    return res_str + '}'


def generate_result_string_dif(f_path1, f_path2, json_dict_o, json_dict_t):
    res = 'gendiff ' + str(os.path.basename(f_path1)) + ' ' + str(os.path.basename(f_path2)) + '\n' + '{' + '\n'
    for key, value in sorted(json_dict_o.items() | json_dict_t.items()):
        if key in json_dict_o:
            if (
                key in json_dict_t and
                json_dict_t[key] == value and
                json_dict_o[key] == value
            ):
                res += '    ' + str(key) + ': ' + str(value) + '\n'
            elif key not in json_dict_t:
                res += '  ' + '-' + ' ' + str(key) + ': ' + str(value) + '\n'
            elif key in json_dict_t and json_dict_t[key] != value:
                res += '  ' + '-' + ' ' + str(key) + ': ' + str(value) + '\n'
                res += (
                    '  ' + '+' + ' ' + str(key) + ': '
                    + str(json_dict_t[key]) + '\n'
                )
        elif key not in json_dict_o:
            if key in json_dict_t:
                res += '  ' + '+' + ' ' + str(key) + ': ' + str(value) + '\n'
    return res
