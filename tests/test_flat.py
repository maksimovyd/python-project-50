from gendiff.scripts import parser
import os


def test_flat_gendiff():
    current_dir = os.path.dirname(__file__)
    file_path1 = os.path.join(current_dir, 'fixtures', 'file1.json')
    file_path2 = os.path.join(current_dir, 'fixtures', 'file2.json')
    file_res = os.path.join(current_dir, 'fixtures', 'res_test_1_2.txt')
    with open(file_res, 'r') as res_test_1_2:
        res_file_1_2 = res_test_1_2.read()
    assert parser.generate_diff(file_path1, file_path2, 'stylish') == str(res_file_1_2)


def test_flat_gendiff_two_empty_file_two():
    current_dir = os.path.dirname(__file__)
    file_path1 = os.path.join(current_dir, 'fixtures', 'file_test_flat2_1.json')
    file_path2 = os.path.join(current_dir, 'fixtures', 'file_test_flat2_2.json')
    file_res = os.path.join(current_dir, 'fixtures', 'res_test_flat_2.txt')
    with open(file_res, 'r') as res_test_1_2:
        res_file_1_2 = res_test_1_2.read()
    assert parser.generate_diff(file_path1, file_path2, 'stylish') == str(res_file_1_2)


def test_yml():
    current_dir = os.path.dirname(__file__)
    file_path1 = os.path.join(current_dir, 'fixtures', 'yml_file1.yml')
    file_path2 = os.path.join(current_dir, 'fixtures', 'yml_file2.yml')
    file_res = os.path.join(current_dir, 'fixtures', 'res_test_yml_1_2.txt')
    with open(file_res, 'r') as res_test_1_2:
        res_file_1_2 = res_test_1_2.read()
    assert parser.generate_diff(file_path1, file_path2, 'stylish') == str(res_file_1_2)


def test_two_level_yml():
    current_dir = os.path.dirname(__file__)
    file_path1 = os.path.join(current_dir, 'fixtures', 'yml_file_1_two_level.yml')
    file_path2 = os.path.join(current_dir, 'fixtures', 'yml_file_2_two_level.yml')
    file_res = os.path.join(current_dir, 'fixtures', 'yml_res_test_two_level.txt')
    with open(file_res, 'r') as res_test_1_2:
        res_file_1_2 = res_test_1_2.read()
    assert parser.generate_diff(file_path1, file_path2, 'stylish') == str(res_file_1_2)


def test_two_level_json():
    current_dir = os.path.dirname(__file__)
    file_path1 = os.path.join(current_dir, 'fixtures', 'file_1_two_level.json')
    file_path2 = os.path.join(current_dir, 'fixtures', 'file_2_two_level.json')
    file_res = os.path.join(current_dir, 'fixtures', 'res_test_two_level.txt')
    with open(file_res, 'r') as res_test_1_2:
        res_file_1_2 = res_test_1_2.read()
    assert parser.generate_diff(file_path1, file_path2, 'stylish') == str(res_file_1_2)


# Ожидаемое значение в тестах — объемная строчка. А в будущих шагах она станет значительно сложнее. В таких случаях принято сохранять их также в фикстуры в виде текстовых файлов и читать в нужных тестах
# Убрать строку сравнение в файл