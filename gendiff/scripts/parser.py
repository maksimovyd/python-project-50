import json
import os
import yaml


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
