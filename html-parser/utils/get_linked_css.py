import re
from utils.get_raw_html import get_raw_html

def get_linked_css_url(url: str) -> str:
    html = get_raw_html(url)

    linked_css = re.findall(r'<link .*>|<link .*?/>', html)

    return linked_css