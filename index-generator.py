import os
import date_extractor

s = open("html/index_start.html", "r")
html_start = s.read()

e = open("html/index_end.html", "r")
html_end = e.read()

s.close()
e.close()

i = open("index.html", "w")

generated_file = ""

directory_name = "html/blog_posts/"
directory = os.fsencode(directory_name)
    
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    blog_file = open(directory_name + filename, "r")
    blog_post = blog_file.read()

    date_extractor.get_date(blog_post, filename)

    generated_file = "<div class=post>" + blog_post + "</div>" + generated_file
    blog_file.close()

generated_file = html_start + generated_file + html_end
i.write(generated_file)
i.close()