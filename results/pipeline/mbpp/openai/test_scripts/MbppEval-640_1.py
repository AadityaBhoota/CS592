import re

def remove_parenthesis(items):
    # Remove the text inside parentheses from each item in the input list
    pattern = r"\(.*?\)"
    modified_items = tuple(re.sub(pattern, "", item) for item in items)
    
    return modified_items

def check(candidate):
    assert remove_parenthesis(["python (chrome)"])==("python")
    assert remove_parenthesis(["string(.abc)"])==("string")
    assert remove_parenthesis(["alpha(num)"])==("alpha")

check(remove_parenthesis)