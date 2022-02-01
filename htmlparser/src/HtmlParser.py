from htmlparser.helpers.clean_attributes import clean_attributes
from utils.get_linked_css_url import get_linked_css_url
from utils.get_linked_scripts_url import get_linked_scripts_url
from src.find_source_css import find_source_css
from src.find_source_script import find_source_script
from src.relative_path import relative_path

class HtmlParser:
    def __init__(self, url) -> None:
        self.url = url
    
    def find_linked_css_urls(self) -> list:
        return get_linked_css_url(self.url)

    def find_linked_css_count(self) -> int:
        return len(get_linked_css_url(self.url))

    def find_linked_scripts_url(self) -> list:
        return get_linked_scripts_url(self.url)

    def find_linked_scripts_count(self) -> int:
        return len(get_linked_scripts_url(self.url))

    def get_css_paths(self) -> list(str):
        css = self.find_linked_css_urls()
        source = find_source_css(css)

        return relative_path(clean_attributes(source), self.url)

    def get_js_paths(self) -> list(str):
        css = self.find_linked_scripts_url()
        source = find_source_script(css)

        return relative_path(clean_attributes(source), self.url)
