from src.HtmlParser import HtmlParser

htmlparser = HtmlParser("http://localhost:3000/")

css = htmlparser.get_css_paths()
js = htmlparser.get_js_paths()

print("JS Scripts:", js)
print("CSS Stylesheets:", css)
