from jinja2 import Environment, FileSystemLoader, select_autoescape
import markdown
import json
import os

pages = "pages"
output_dir = "web"

env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape()
)

home_template = env.get_template("home.html")
post_template = env.get_template('post.html')
test_template = env.get_template('test.html')

# Filename list
file_names = []

# Handling posts
for filename in os.listdir(pages):
    # Markdown-Datei einlesen
    with open(os.path.join(pages, filename), "r") as file:
        markdown_text = file.read()

    # Change markdown to html
    html_text = markdown.markdown(markdown_text)

    # offprefix = os.path.splitext(filename)[0]
    # print("Offprefix :", offprefix)

    # Render Jinja template
    rendered_html = post_template.render(page_title=filename, content=html_text)

    # Save html
    output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + ".html")
    with open(output_path, "w") as html_file:
        html_file.write(rendered_html)
        print("Created post: ", output_path)

    file_names.append(os.path.basename(output_path))
    title_name = os.path.splitext(filename)[0]
    print("Title_name: ", title_name)

# Handling index.html
output_path = os.path.join(output_dir, "index.html")
index_rendered = home_template.render(filenames=file_names)
with open(output_path, "w") as index_file:
    index_file.write(index_rendered)
