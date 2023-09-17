from gendiff.scripts import gendiff
import os


def test_flat_gendiff():
    current_dir = os.path.dirname(__file__)
    file_path1 = os.path.join(current_dir, 'fixtures', 'file1.json')
    file_path2 = os.path.join(current_dir, 'fixtures', 'file2.json')
    file_res = os.path.join(current_dir, 'fixtures', 'res_test_1_2.txt')
    with open(file_res, 'r') as res_test_1_2:
        res_file_1_2 = res_test_1_2.read()
    assert gendiff.generate_diff(file_path1, file_path2) == str(res_file_1_2)


def test_flat_gendiff_two_empty_file_two():
    current_dir = os.path.dirname(__file__)
    file_path1 = os.path.join(current_dir, 'fixtures', 'file_test_flat2_1.json')
    file_path2 = os.path.join(current_dir, 'fixtures', 'file_test_flat2_2.json')
    file_res = os.path.join(current_dir, 'fixtures', 'res_test_flat_2.txt')
    with open(file_res, 'r') as res_test_1_2:
        res_file_1_2 = res_test_1_2.read()
    assert gendiff.generate_diff(file_path1, file_path2) == str(res_file_1_2)


# Ожидаемое значение в тестах — объемная строчка. А в будущих шагах она станет значительно сложнее. В таких случаях принято сохранять их также в фикстуры в виде текстовых файлов и читать в нужных тестах
# Убрать строку сравнение в файл