def generate_blog_page(start, post, end, fn, fp):
    individual_blog_page = start + post + end
    s = open(fp + fn, "w")
    s.write(individual_blog_page)
    s.close()

import os
import date_extractor

s = open("html/index_start.html", "r")
html_start = s.read()

si = open("html/individual_start.html", "r")
individual_start = si.read()

e = open("html/index_end.html", "r")
html_end = e.read()

s.close()
e.close()

i = open("index.html", "w")

generated_file = ""

directory_name = "html/blog_posts/"
directory = os.fsencode(directory_name)

ordered_blog_posts = os.listdir(directory)
ordered_blog_posts = [x[:len(x)-5] for x in ordered_blog_posts] #cut .html off the end of each filename
ordered_blog_posts.sort(key=int) #sort ascending numerically; ensures "10" comes after "9" instead of coming after "1"
    
for file in ordered_blog_posts:
    filename = os.fsdecode(file) + ".html"
    blog_file = open(directory_name + filename, "r")
    blog_post = blog_file.read()

    day = date_extractor.get_date(blog_post, filename)

    new_post = "<div class=post>" + blog_post + "</div>"

    generated_file =  new_post + generated_file

    blog_file.close()

    individual_filepath = "html/individual_pages/"

    if not os.path.isfile(individual_filepath + day + ".html"): #only generate page if it does not already exist
        generate_blog_page(individual_start, new_post, html_end, day + ".html", individual_filepath)
    

generated_file = html_start + generated_file + html_end
i.write(generated_file)
i.close()