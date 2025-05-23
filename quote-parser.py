#Basic parsing of my webpages for quotes with only built-in Python classes.

from html.parser import HTMLParser


quote_list = []

class QuoteParser(HTMLParser):
    quote = False
    current_quote = ""
    def handle_starttag(self, tag, attrs):
        if tag == "q":
            QuoteParser.quote = True
            

    def handle_endtag(self, tag):
        if tag == "br": #allow for quotes with linebreaks inside of them
            QuoteParser.current_quote += "<br/>"
        if tag == "q":
            QuoteParser.quote = False
            quote_list.append(QuoteParser.current_quote)
            QuoteParser.current_quote = "" #reset the current quote to blank
            

    def handle_data(self, data):

        if QuoteParser.quote:
            QuoteParser.current_quote += data



parser = QuoteParser()

f = open("index.html", "r")
parser.feed(f.read())
f.close()


f = open("quote.html", "w")

s = open("html/quote_start.html", "r")
html_start = s.read()

f.write(html_start)
s.close()
for q in quote_list:
    f.write("<h4 class='quote'>" + q + "</h4>")
    f.write("<div class='horizontal-break'>~</div>")