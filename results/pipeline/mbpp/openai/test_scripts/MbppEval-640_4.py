import re

def remove_parenthesis(items):
    result = re.sub(r'\(.*?\)', '', items[0])
    return result

def check(candidate):
    assert remove_parenthesis(["python (chrome)"])==("python")
    assert remove_parenthesis(["string(.abc)"])==("string")
    assert remove_parenthesis(["alpha(num)"])==("alpha")

check(remove_parenthesis)