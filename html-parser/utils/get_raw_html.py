import requests

def get_raw_html(url: str) -> str:
    req = requests.get(url)

    req.close()

    return req.content.decode()