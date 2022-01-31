import re

""" 
Checks for relative path and if present fixes them to a parent url
"""
def relative_path(string: str, parent_url: str) -> str:
    if string.startswith("."):
        result = f"{parent_url}/{string[2:]}"

    return result
