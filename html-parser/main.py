from src.HtmlParser import HtmlParser

htmlparser = HtmlParser("https://hashable.space")

print(htmlparser.find_linked_css_count())

print(htmlparser.find_linked_scripts_url())