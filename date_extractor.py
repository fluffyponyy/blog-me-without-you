from html.parser import HTMLParser
import json
import dateparser

class DateParser(HTMLParser):
    is_date_element = False
    current_date = ""
    def handle_starttag(self, tag, attrs):
        date_class_attribute = ('class', 'date')
        if attrs:
            if date_class_attribute in attrs:
                DateParser.is_date_element = True

    def handle_data(self, data):
        if DateParser.is_date_element:
            DateParser.current_date = data
            DateParser.is_date_element = False #dates are only ever one line

def get_date(blog_post, fn):
    parser = DateParser()
    parser.feed(blog_post)

    date_time = dateparser.parse(parser.current_date)
    year = str(date_time.year)
    month = str(date_time.month)
    day = str(date_time.day)

    updated_dictionary = {}

    with open("post_archive.json", "r") as infile:
        d = infile.read()

        d = json.loads(d)

        #Insert into dictionary
        if year not in d:
            d[year] = {}
        if month not in d[year]:
            d[year][month] = {}
        if day not in d[year][month]:
            d[year][month][day] = {}

        d[year][month][day] = fn #Only allows one post per day
        updated_dictionary = d

    # Serializing json
    json_object = json.dumps(updated_dictionary, indent=4)

    with open("post_archive.json", "w") as outfile:
        outfile.write(json_object)

    return f'{year}{month}{day}'
