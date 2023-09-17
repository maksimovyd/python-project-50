import json
import os
import yaml


def generate_diff(file_path1, file_path2):
    json_dict_one = read_files(file_path1)
    json_dict_two = read_files(file_path2)
    res_str = generate_result_string_dif(
        file_path1, file_path2, json_dict_one, json_dict_two
        )
    print(res_str + '}')
    return res_str + '}'


def read_files(file_path):
    ext = get_file_extension(file_path)
    res_dict = {}
    if ext == 'json':
        with open(file_path, 'r') as file_read:
            res_dict = json.loads(file_read.read())
    elif ext == 'yml' or ext == 'yaml':
        with open(file_path, 'r') as yaml_file:
            res_dict = yaml.load(yaml_file, Loader=yaml.FullLoader)
    return res_dict


def get_file_extension(file_path):
    _, extension = os.path.splitext(file_path)
    return extension.lstrip('.')


def generate_result_string_dif(f_path1, f_path2, dict_o, dict_t):
    res = (
        'gendiff ' + str(os.path.basename(f_path1)) + ' ' +
        str(os.path.basename(f_path2)) + '\n' + '{' + '\n'
    )
    for key, value in sorted(dict_o.items() | dict_t.items()):
        if key in dict_o:
            if (
                key in dict_t and
                dict_t[key] == value and
                dict_o[key] == value
            ):
                res += '    ' + str(key) + ': ' + str(value) + '\n'
            elif key not in dict_t:
                res += '  ' + '-' + ' ' + str(key) + ': ' + str(value) + '\n'
            elif key in dict_t and dict_t[key] != value:
                res += '  ' + '-' + ' ' + str(key) + ': ' + str(value) + '\n'
                res += (
                    '  ' + '+' + ' ' + str(key) + ': '
                    + str(dict_t[key]) + '\n'
                )
        elif key not in dict_o:
            if key in dict_t:
                res += '  ' + '+' + ' ' + str(key) + ': ' + str(value) + '\n'
    return res
