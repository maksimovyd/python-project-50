from gendiff.scripts import gendiff
import os


def test_flat_gendiff():
    current_dir = os.path.dirname(__file__)
    file_path1 = os.path.join(current_dir, 'fixtures', 'file1.json')
    file_path2 = os.path.join(current_dir, 'fixtures', 'file2.json')
    assert gendiff.generate_diff(file_path1, file_path2) == 'gendiff file1.json file2.json\n{\n  - follow: False\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: True\n}'
