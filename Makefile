install:
	poetry install

build:
	poetry build

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml

lint:
	poetry run flake8 gendiff/

selfcheck:
	poetry check

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

gendiff:
	poetry run gendiff

check:
	poetry run flake8 gendiff/
