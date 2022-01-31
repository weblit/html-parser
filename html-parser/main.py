from src.HtmlParser import HtmlParser
from src.find_source_script import find_source_script
from src.find_source_css import find_source_css

htmlparser = HtmlParser("./html-parser/tests/index.html")

stylesheet = htmlparser.find_linked_css_urls()

scripts = htmlparser.find_linked_scripts_url()

for script in scripts:
    print(find_source_script(script))

for css in stylesheet:
    print(find_source_css(css))