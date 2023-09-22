from gendiff.scripts.gendiff import generate_diff
import pytest


json_1 = "tests/fixtures/file1.json"
json_2 = "tests/fixtures/file2.json"
yaml_1 = "tests/fixtures/file1.yml"
yaml_2 = "tests/fixtures/file2.yml"
res_stylish = "tests/fixtures/result_stylish"
res_plain = "tests/fixtures/result_plain"
res_json = "tests/fixtures/result_json.json"

formats = ['stylish', 'plain', 'json']


@pytest.mark.parametrize('path1, path2, format_name, expected', [(json_1, json_2, formats[0], res_stylish),
                                                                 (yaml_1, yaml_2, formats[0], res_stylish),
                                                                 (json_1, json_2, formats[1], res_plain),
                                                                 (yaml_1, yaml_2, formats[1], res_plain),
                                                                 (json_1, json_2, formats[2], res_json),
                                                                 (yaml_1, yaml_2, formats[2], res_json)])
def test_generate_diff(path1, path2, format_name, expected):
    if format_name == 'stylish':
        diff = generate_diff(path1, path2)
    else:
        diff = generate_diff(path1, path2, format_name)
    with open(expected) as f:
        assert diff == f.read()


@pytest.mark.parametrize(format, test_cases)
def test_generate_diff(format):
    file_path1 = get_path(f'file1.{format}')
    file_path2 = get_path(f'file2.{format}')
    result_stylish = generate_diff(file_path1, file_path2, format)
    assert generate_diff(file_path1, file_path2) == result_stylish


def get_path(str_path):
    return 'tests/fixtures/' + str_path