import glob
import os
import re

from dotenv import load_dotenv

load_dotenv()

HUGO_POSTS = os.getenv("HUGO_POSTS")

if not os.path.isdir(HUGO_POSTS):
    raise FileNotFoundError(f"Directory not found: {HUGO_POSTS}")

md_files = glob.glob(os.path.join(HUGO_POSTS, "*.md"))

date_pattern = re.compile(r"\[(\d{4}-\d{2}-\d{2}) (.*?)\]\((.*?)\)")

for md_file in md_files:
    with open(md_file, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = re.split(r"^## Hidden\s*---", content, flags=re.MULTILINE)[0].strip()

    new_content = date_pattern.sub(r"[\2](\3)", new_content)

    with open(md_file, "w", encoding="utf-8") as f:
        f.write(new_content + "\n")
