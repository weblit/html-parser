import requests
from src.HtmlParser import HtmlParser
from src.find_source_script import find_source_script
from src.find_source_css import find_source_css
from src.relative_path import relative_path

htmlparser = HtmlParser("http://localhost:3000/")

stylesheet = htmlparser.find_linked_css_urls()

scripts = htmlparser.find_linked_scripts_url()

for script in scripts:
    source = find_source_script(script)
    print("Relative path", relative_path(source, "http://localhost:3000"))

for css in stylesheet:
    source = find_source_css(css)
    print("Relative path", relative_path(source, "http://localhost:3000"))
