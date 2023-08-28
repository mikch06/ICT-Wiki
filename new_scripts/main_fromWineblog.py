from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
import os

with open('./db/new-db.json', 'r') as file:
    data = json.load(file)

env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape()
)

home_template = env.get_template("home.html")
post_template = env.get_template('post.html')
test_template = env.get_template('test.html')

# Handling posts
for wine in data['wines']:
    post_html = post_template.render(wine=wine)
    #post_html = post_template.render(wine=['wine'])
    print("data: ", data)

    post_file_path = 'output/posts/{name}.html'.format(name=wine['name'])

    os.makedirs(os.path.dirname(post_file_path), exist_ok=True)
    with open(post_file_path, 'w', encoding="utf-8") as file:
        file.write(post_html)

# Handling index.html
for wine in data['wines']:
    home_html = home_template.render(data)
    #print(home_html)

    with open('output/index.html', 'w', encoding="utf-8") as file:
        file.write(home_html)

# Handling categories.html
for wine in data['wines']:
    categories_html = home_template.render(data)

    with open('output/categories.html', 'w', encoding="utf-8") as file:
        file.write(categories_html)
