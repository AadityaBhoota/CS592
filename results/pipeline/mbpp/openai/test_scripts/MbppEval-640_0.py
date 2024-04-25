import re

def remove_parenthesis(items):
    pattern = r"\(.*?\)"
    result = re.sub(pattern, "", items[0])
    return result

def check(candidate):
    assert remove_parenthesis(["python (chrome)"])==("python")
    assert remove_parenthesis(["string(.abc)"])==("string")
    assert remove_parenthesis(["alpha(num)"])==("alpha")

check(remove_parenthesis)