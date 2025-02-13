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
else
	@echo "Running on macOS or Linux"
	rsync -avu --include='*.md' --exclude='*' "$(OBSIDIAN_POSTS)/" "$(HUGO_POSTS)/"
	rsync -avu "$(OBSIDIAN_POSTS_RESOURCES)/" "$(HUGO_POSTS_RESOURCES)/"
endif
	$(MAKE) python


python: $(PYTHON)
	@echo "Running Python script"
	@$(PYTHON) python/transform.py


clean:
	@echo "Cleaning up..."


.PHONY: sync clean python
