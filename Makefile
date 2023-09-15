install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

gendiff:
	poetry run gendiff

check:
	poetry run flake8 gendiff/
