from src.HtmlParser import HtmlParser

htmlparser = HtmlParser("./html-parser/tests/index.html")

print(htmlparser.find_linked_css_count())

print(htmlparser.find_linked_scripts_url()) 