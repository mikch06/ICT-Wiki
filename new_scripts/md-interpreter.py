import os
from datetime import datetime
from jinja2 import Environment, PackageLoader
from markdown2 import markdown
import json

posts = {}

for markdown_post in os.listdir('content'):
    file_path = os.path.join('content', markdown_post)

    with open(file_path, 'r') as file:
        posts[markdown_post] = markdown(file.read(), extras=['metadata'])

env = Environment(loader=PackageLoader('main', 'templates'))

home_template = env.get_template('home.html')
post_template = env.get_template('post.html')

posts_metadata = [posts[post].metadata for post in posts]

home_html = home_template.render(posts=posts_metadata)

with open('output/index.html', 'w') as file:
    file.write(home_html)

for post in posts:
    post_metadata = posts[post].metadata

    post_data = {
        'content': posts[post],
        'winename': post_metadata['winename'],
        'date': post_metadata['date'],
        'category': post_metadata['category'],
        'image': post_metadata['image'],
        'tags': post_metadata['tags'],
    }

    #postname = os.path.split(markdown_post)[1]
    # for markdown_post in os.listdir('content'):
    # #postname = os.listdir('content')
    #     postname = os.path.splitext(markdown_post)[0]
    #     postname = postname + ".html"
    #     print("art: ", postname)

    post_html = post_template.render(post=post_data)
    post_file_path = 'output/posts/{date}.html'.format(date=post_metadata['date'])


    os.makedirs(os.path.dirname(post_file_path), exist_ok=True)
    with open(post_file_path, 'w') as file:
        file.write(post_html)
