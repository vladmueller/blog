import glob
import os
import re

from dotenv import load_dotenv

load_dotenv()

HUGO_POSTS = os.getenv("HUGO_POSTS")

if not os.path.isdir(HUGO_POSTS):
    raise FileNotFoundError(f"Directory not found: {HUGO_POSTS}")

md_files = glob.glob(os.path.join(HUGO_POSTS, "*.md"))

for md_file in md_files:
    with open(md_file, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = re.split(r"^## Hidden\s*---", content, flags=re.MULTILINE)[0].strip()

    with open(md_file, "w", encoding="utf-8") as f:
        f.write(new_content + "\n")
