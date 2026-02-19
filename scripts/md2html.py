import markdown
from pathlib import Path
import re

readme_file = Path("README.md")
html_file = Path("index.html")

md_text = readme_file.read_text(encoding="utf-8")


def add_github_icon(md):
 
    def repl(match):
        text = match.group(1)
        url = match.group(2)
        if "github.com" in url:
           
            return f'<a href="{url}" target="_blank"><img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/github.svg" alt="GitHub" class="github-icon">{text}</a>'
        else:
            return f'<a href="{url}" target="_blank">{text}</a>'
    
    pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    return pattern.sub(repl, md)


md_text_with_icons = add_github_icon(md_text)


html_body = markdown.markdown(md_text_with_icons, extensions=['fenced_code', 'tables'])

html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Dmitry Zhuravlev - Portfolio Projects</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
<style>
body {{
    font-family: 'Inter', Arial, sans-serif;
    max-width: 900px;
    margin: 50px auto;
    padding: 0 20px;
    line-height: 1.7;
    color: #1a1a1a;
    background-color: #f9f9f9;
}}
h1, h2, h3 {{
    color: #222;
}}
h1 {{ text-align: center; margin-bottom: 40px; }}
a {{
    color: #007acc;
    text-decoration: none;
}}
a:hover {{
    text-decoration: underline;
}}
ul {{ list-style: none; padding-left: 0; }}
li {{ margin-bottom: 15px; }}
small {{ color: #555; display: block; margin-top: 5px; }}
.github-icon {{
    width: 18px;
    height: 18px;
    margin-right: 6px;
    vertical-align: middle;
}}
</style>
</head>
<body>
{html_body}
</body>
</html>
"""

html_file.write_text(html_template, encoding="utf-8")
print("index.html has been generated successfully!")
