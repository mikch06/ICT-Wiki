    # write_messages.py
from pathlib import Path



from jinja2 import Environment, FileSystemLoader
from datetime import datetime

# Filepath
source = 'pages'
dest = 'web'

environment = Environment(loader=FileSystemLoader("./templates/"))
template = environment.get_template("results.html")
article_template = environment.get_template('article.html')





# for student in students:
#
#     results_filename = "./web/students_results.html"
#     results_template = environment.get_template("results.html")
#
#
#     with open(results_filename, mode="w", encoding="utf-8") as results:
#         results.write(results_template.render(context))
#         print(f"... wrote {results_filename}")

# Generate html files from markdown files
mdowns = Path(source).glob('*')
for file in mdowns:

    results_filename = "./web/students_results.html"
    results_template = environment.get_template("results.html")

    with open(results_filename, mode="w", encoding="utf-8") as results:
        #results.write
        results.write(results_template.name)
        print(f"... wrote {file}")





#     env = jinja2.Environment( loader=MyTemplateLoader(tpl_path or './') )