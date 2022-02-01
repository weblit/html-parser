from utils.get_linked_css_url import get_linked_css_url
from utils.get_linked_scripts_url import get_linked_scripts_url

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



