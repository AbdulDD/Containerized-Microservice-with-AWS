# Install dependencies
install:
	pip install --upgrade pip 
	pip install -r requirements.txt

# Run tests
test:
	pytest

# Format code
format:
	black

# Run everything
all: install format test