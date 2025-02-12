import os
import glob
import re

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


def to_kebab_case(title):
    return re.sub(r'[^a-zA-Z0-9]+', '-', title.strip().lower()).strip('-')


def transform_wiki_links(p_content):
    """
    Replace [[Title]] with [Title](/posts/title-in-kebab-case)
    """
    return re.sub(
        r'\[\[(.*?)\]\]',
        lambda match: f"[{match.group(1)}](/posts/{to_kebab_case(match.group(1))})",
        p_content
    )


# Ensure the directory exists
if not os.path.isdir(HUGO_POSTS):
    raise FileNotFoundError(f"Directory not found: {HUGO_POSTS}")

md_files = glob.glob(os.path.join(HUGO_POSTS, "*.md"))

for md_file in md_files:
    with open(md_file, "r", encoding="utf-8") as f:
        content = f.read()

    updated_content = transform_wiki_links(content)

    # Write the updated content back to the file
    with open(md_file, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print(f"Updated: {md_file}")

print("✅ All markdown files have been processed.")
