import os
import glob
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

OBSIDIAN_POSTS = os.getenv("OBSIDIAN_POSTS")
OBSIDIAN_POSTS_RESOURCES = os.getenv("OBSIDIAN_POSTS_RESOURCES")
HUGO_POSTS = os.getenv("HUGO_POSTS")
HUGO_POSTS_RESOURCES = os.getenv("HUGO_POSTS_RESOURCES")

print("OBSIDIAN_POSTS:", OBSIDIAN_POSTS)
print("OBSIDIAN_POSTS_RESOURCES:", OBSIDIAN_POSTS_RESOURCES)
print("HUGO_POSTS:", HUGO_POSTS)
print("HUGO_POSTS_RESOURCES:", HUGO_POSTS_RESOURCES)

# Ensure the directory exists
if not os.path.isdir(HUGO_POSTS):
    raise FileNotFoundError(f"Directory not found: {HUGO_POSTS}")

md_files = glob.glob(os.path.join(HUGO_POSTS, "*.md"))

# Print the list of Markdown files
for md_file in md_files:
    print(f"Found: {md_file}")

# Optionally, read each file's content
for md_file in md_files:
    with open(md_file, "r", encoding="utf-8") as f:
        content = f.read()
        print(f"Contents of {md_file} (first 100 chars):\n{content[:100]}...\n")
