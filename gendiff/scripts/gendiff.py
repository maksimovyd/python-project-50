import argparse
import json
from gendiff.scripts.parser import read_files_to_dict
from gendiff.scripts.stylish import stylish
from gendiff.scripts.plain import plain


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file", help="The first configuration file.")
    parser.add_argument("second_file", help="The second configuration file.")
    parser.add_argument(
        "-f", "--format", help="set format of output",
        default="stylish", choices=["stylish", "plain", "json"])
    args = parser.parse_args()
    generate_diff(args.first_file, args.second_file, formatter=args.format)


if __name__ == "__main__":
    main()


def generate_diff(file_path1, file_path2, formatter='stylish'):
    dict_one = read_files_to_dict(file_path1)
    dict_two = read_files_to_dict(file_path2)
    res_dict = create_diff(dict_one, dict_two)
    if formatter == 'stylish':
        res_str = stylish(res_dict)
        # res_str = (
        #     'gendiff ' + str(os.path.basename(file_path1)) +
        #     ' ' + str(os.path.basename(file_path2)) + '\n' + res_str
        #     )
        print(res_str)
        return res_str
    elif formatter == 'plain':
        res_str = plain(res_dict, dict_one, dict_two, [], '')
        # res_str = (
        #     'gendiff --format plain ' + str(os.path.basename(file_path1)) +
        #     ' ' + str(os.path.basename(file_path2)) + '\n' + res_str
        #     )
        res_str = res_str[:-1]
        print(res_str)
        return res_str
    elif formatter == 'json':
        res_dict = create_diff(dict_one, dict_two)
        json_str = json.dumps(res_dict, indent=4)
        print("\n".join(json_str.splitlines()))
        return "\n".join(json_str.splitlines())
        # print(json.dumps(create_diff(dict_one, dict_two)))
        # return json.dumps(create_diff(dict_one, dict_two))


def create_diff(dict_one, dict_two):
    all_keys = sorted(list(dict_one.keys() | dict_two.keys()))
    res_dict = {}
    for key_ in all_keys:
        if key_ in dict_one and key_ in dict_two:
            if isinstance(dict_one[key_], dict) and \
               isinstance(dict_two[key_], dict):
                res_dict[('    ' + key_)] = create_diff(
                    dict_one[key_],
                    dict_two[key_])
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


def create_diff_json(dict_one, dict_two):
    all_keys = sorted(list(dict_one.keys() | dict_two.keys()))
    res_dict = {}
    for key_ in all_keys:
        if key_ in dict_one and key_ in dict_two:
            if isinstance(dict_one[key_], dict) and \
               isinstance(dict_two[key_], dict):
                res_dict[key_] = create_diff_json(dict_one[key_],
                                                  dict_two[key_])
            elif dict_one[key_] == dict_two[key_]:
                res_dict[key_] = dict_one[key_]
            else:
                res_dict[key_] = dict_one[key_]
                res_dict[key_] = dict_two[key_]
        elif key_ in dict_one and key_ not in dict_two:
            res_dict[key_] = dict_one[key_]
        else:
            res_dict[key_] = dict_two[key_]
    return res_dict
