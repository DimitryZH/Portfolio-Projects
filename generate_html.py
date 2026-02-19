import markdown
import os
from datetime import datetime

# --- Read README ---
with open("README.md", "r", encoding="utf-8") as f:
    md_content = f.read()

html_body = markdown.markdown(md_content)

# --- CI/CD metadata ---
commit = os.getenv("COMMIT_SHA", "")[:7]
build_date = os.getenv("BUILD_DATE", "")
repo_url = os.getenv("REPO_URL", "")

if build_date:
    build_date = datetime.fromisoformat(
        build_date.replace("Z", "+00:00")
    ).strftime("%Y-%m-%d %H:%M UTC")

# --- HTML template ---
html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Dmitry Zhuravlev — Cloud & DevOps Portfolio</title>

<style>
body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI",
                 Roboto, Helvetica, Arial, sans-serif;
    margin: 40px auto;
    max-width: 900px;
    line-height: 1.6;
    color: #111827;
    padding: 0 20px;
}}

h1, h2, h3 {{
    margin-top: 32px;
}}

a {{
    color: #2563eb;
    text-decoration: none;
}}

a:hover {{
    text-decoration: underline;
}}

.footer {{
    margin-top: 60px;
    padding-top: 20px;
    border-top: 1px solid #e5e7eb;
    font-size: 14px;
    color: #6b7280;
}}

.footer a {{
    color: #2563eb;
}}

.status {{
    margin-bottom: 10px;
}}
</style>
</head>

<body>

{html_body}

<footer class="footer">
  <div class="status">
     Build passing<br>
     Auto deployed via GitHub Actions<br>
     CI/CD enabled
  </div>

  <div class="meta">
    Last deploy: {build_date}<br>
    Commit:
    <a href="{repo_url}/commit/{commit}">
      {commit}
    </a>
  </div>
</footer>

</body>
</html>
"""

# --- Write index.html ---
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("index.html generated successfully")
