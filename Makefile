include .env

PYTHON_VENV = python/venv
PYTHON = $(PYTHON_VENV)/Scripts/python.exe

# Create virtual environment if it does not exist
$(PYTHON):
	python3 -m venv $(PYTHON_VENV)

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
ifeq ($(OS),Windows_NT)
	@echo "Running on Windows"
	@$(PYTHON) python/sync.py
else
	@echo "Running on macOS or Linux"
endif

.PHONY: sync clean python
