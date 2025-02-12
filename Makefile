include .env

PYTHON_VENV = python/venv

ifeq ($(OS),Windows_NT)
    PYTHON = $(PYTHON_VENV)/Scripts/python.exe
else
    PYTHON = $(PYTHON_VENV)/bin/python
endif

# Create virtual environment if it does not exist and install dependencies
$(PYTHON):
	python3 -m venv $(PYTHON_VENV)
	$(PYTHON) -m pip install --upgrade pip
ifneq ("$(wildcard python/requirements.txt)", "")
	$(PYTHON) -m pip install -r python/requirements.txt
endif

sync:
	@echo "Sync posts ..."
ifeq ($(OS),Windows_NT)
	@echo "Running on Windows"
	- @cmd /c sync_posts.bat
	find "$(HUGO_POSTS)" -type f -name "*.md" -exec sed -i -E "s/!\[\[([^]]+)\]\]/![\1]\(\/images\/\1\)/g" {} +
else
	@echo "Running on macOS or Linux"
	rsync -avu --include='*.md' --exclude='*' "$(OBSIDIAN_POSTS)/" "$(HUGO_POSTS)/"
	rsync -avu "$(OBSIDIAN_POSTS_RESOURCES)/" "$(HUGO_POSTS_RESOURCES)/"
	find $(HUGO_POSTS) -type f -name "*.md" -exec sed -i '' -E 's/!\[\[([^]]+)\]\]/![\1]\(\/images\/\1\)/g' {} +
endif

clean:
	@echo "Cleaning up..."

python: $(PYTHON)
	@echo "Running Python script"
	@$(PYTHON) python/sync.py

.PHONY: sync clean python
