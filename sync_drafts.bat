@echo off

:: Load .env
for /f "tokens=1,2 delims==" %%a in (.env) do set %%a=%%b

robocopy "%OBSIDIAN_POSTS%" "%HUGO_POSTS%" /E "*.md"
