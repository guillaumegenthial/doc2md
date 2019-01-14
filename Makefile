install:
	pip install -r requirements.txt
	pip install pytest

test:
	cd tests/mydummypackage && python -m pip install -e .
	cd tests/mydummypackage && doc2md mydummypackage -o test-docs -b ../
	python -m pytest tests
