import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the variables
OBSIDIAN_POSTS = os.getenv("OBSIDIAN_POSTS")
OBSIDIAN_POSTS_RESOURCES = os.getenv("OBSIDIAN_POSTS_RESOURCES")
HUGO_POSTS = os.getenv("HUGO_POSTS")
HUGO_POSTS_RESOURCES = os.getenv("HUGO_POSTS_RESOURCES")

# Print the variables to verify they are loaded
print("OBSIDIAN_POSTS:", OBSIDIAN_POSTS)
print("OBSIDIAN_POSTS_RESOURCES:", OBSIDIAN_POSTS_RESOURCES)
print("HUGO_POSTS:", HUGO_POSTS)
print("HUGO_POSTS_RESOURCES:", HUGO_POSTS_RESOURCES)
