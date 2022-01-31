from src.HtmlParser import HtmlParser
from src.find_source_script import find_source_script

htmlparser = HtmlParser("./html-parser/tests/index.html")

print(htmlparser.find_linked_css_count())

scripts = htmlparser.find_linked_scripts_url()

for script in scripts:
    print(find_source_script(script))