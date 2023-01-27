# write_messages.py

from jinja2 import Environment, FileSystemLoader
from datetime import datetime



environment = Environment(loader=FileSystemLoader("./templates/"))
template = environment.get_template("results.html")





for student in students:

    results_filename = "./web/students_results.html"
    results_template = environment.get_template("results.html")


    with open(results_filename, mode="w", encoding="utf-8") as results:
        results.write(results_template.render(context))
        print(f"... wrote {results_filename}")