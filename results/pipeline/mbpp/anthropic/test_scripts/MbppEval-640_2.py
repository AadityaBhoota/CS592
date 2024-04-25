import re

def remove_parenthesis(items):
    result = []
    for item in items:
        modified_item = re.sub(r'\([^)]*\)', '', item)
        result.append(modified_item)
    return result

def check(candidate):
    assert remove_parenthesis(["python (chrome)"])==("python")
    assert remove_parenthesis(["string(.abc)"])==("string")
    assert remove_parenthesis(["alpha(num)"])==("alpha")

check(remove_parenthesis)