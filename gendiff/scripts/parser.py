import json
import os
import yaml
from gendiff.scripts.stylish import stylish
from gendiff.scripts.plain import plain


def generate_diff(file_path1, file_path2, formatter):
    dict_one = read_files_to_dict(file_path1)
    dict_two = read_files_to_dict(file_path2)
    res_dict = create_diff(dict_one, dict_two)
    if formatter == 'stylish':
        res_str = stylish(res_dict)
        res_str = (
            'gendiff ' + str(os.path.basename(file_path1)) +
            ' ' + str(os.path.basename(file_path2)) + '\n' + res_str
            )
        print(res_str)
        return res_str
    else:
        res_str = plain(res_dict, dict_one, dict_two, [], '')
        res_str = (
            'gendiff --format plain ' + str(os.path.basename(file_path1)) +
            ' ' + str(os.path.basename(file_path2)) + '\n' + res_str
            )
        res_str = res_str[:-1]
        print(res_str)
        return res_str


def create_diff(dict_one, dict_two):
    all_keys = sorted(list(dict_one.keys() | dict_two.keys()))
    res_dict = {}
    for key_ in all_keys:
        if key_ in dict_one and key_ in dict_two:
            if isinstance(dict_one[key_], dict) and \
              isinstance(dict_two[key_], dict):
                res_dict[('    ' +
                          key_)] = create_diff(dict_one[key_], dict_two[key_])
            elif dict_one[key_] == dict_two[key_]:
                res_dict[('    ' + key_)] = dict_one[key_]
            else:
                res_dict[('  - ' + key_)] = dict_one[key_]
                res_dict[('  + ' + key_)] = dict_two[key_]
        elif key_ in dict_one and key_ not in dict_two:
            res_dict[('  - ' + key_)] = dict_one[key_]
        else:
            res_dict[('  + ' + key_)] = dict_two[key_]
    return res_dict


def read_files_to_dict(file_path):
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
