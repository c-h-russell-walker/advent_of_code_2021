black:
	black ./

isort:
	isort ./

flake:
	flake8

mypy:
	mypy  --config-file=mypy.ini ./

lint: isort black mypy flake
