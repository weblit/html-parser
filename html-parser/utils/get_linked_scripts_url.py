import re
from utils.get_raw_html import get_raw_html

def get_linked_scripts_url(url: str) -> str:
    html = get_raw_html(url)

    linked_scripts = re.findall(r'<script .*></script>', html)

    return linked_scripts