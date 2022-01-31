from src.HtmlParser import HtmlParser
from src.find_source_script import find_source_script
from src.find_source_css import find_source_css
from src.relative_path import relative_path

htmlparser = HtmlParser("./html-parser/tests/index.html")

stylesheet = htmlparser.find_linked_css_urls()

scripts = htmlparser.find_linked_scripts_url()

for script in scripts:
    print(find_source_script(script))

for css in stylesheet:
    source = find_source_css(css)
    print("Relative path", relative_path(source, "apple.com"))
