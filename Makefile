include .env

drafts:
	@echo "Sync drafts ..."
ifeq ($(OS),Windows_NT)
	@echo "Running on Windows"
	robocopy "$(OBSIDIAN_POSTS)" "$(HUGO_POSTS)" /MIR *.md
else
	@echo "Running on macOS or Linux"
	rsync -avu "$(OBSIDIAN_POSTS)/" "$(HUGO_POSTS)/"
	find $(HUGO_POSTS) -type f -name "*.md" -exec sed -i '' -E 's/!\[\[([^]]+)\]\]/![\1]\(\/images\/\1\)/g' {} +
endif

clean:
	@echo "Cleaning up..."

.PHONY: drafts clean
