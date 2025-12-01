# Install dependencies
install:
	pip install --upgrade pip 
	pip install --no-cache-dir -r requirements.txt

# Run tests
test:
	pytest

# Format code
format:
	black .

# Lint code
lint:
	flake8 . --exclude=.venv,__pycache__,build,dist

# Run everything: install, format, lint, test
all: install format lint test
