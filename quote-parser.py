#Basic parsing of my webpages for quotes with only built-in Python classes.

from html.parser import HTMLParser


quote_list = []

class QuoteParser(HTMLParser):
    quote = False
    def handle_starttag(self, tag, attrs):
        if tag == "q":
            QuoteParser.quote = True

    def handle_endtag(self, tag):
        if tag == "q":
            QuoteParser.quote = False

    def handle_data(self, data):

        if QuoteParser.quote:
            quote_list.append(data)



parser = QuoteParser()

f = open("index.html", "r")
parser.feed(f.read())
f.close()


f = open("index.html", "a")
#appending is unideal; need to generate entire page over each time basically

for q in quote_list:
    #Definitely not good to keep writing to a file instead of generating all at once and then writing
    f.write("<h3>" + q + "</h3>")