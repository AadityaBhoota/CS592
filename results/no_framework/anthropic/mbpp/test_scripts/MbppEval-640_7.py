import re

def remove_parenthesis(items):
    """
    Write a function to remove the parenthesis and what is in between them from a string.

    Examples:
    remove_parenthesis(["python (chrome)"]) == ["python"]
    remove_parenthesis(["string(.abc)"]) == ["string"]
    remove_parenthesis(["alpha(num)"]) == ["alpha"]
    """
    result = []
    for item in items:
        cleaned_item = re.sub(r'\([^)]*\)', '', item)
        result.append(cleaned_item.strip())
    return result

def check(candidate):
    assert remove_parenthesis(["python (chrome)"])==("python")
    assert remove_parenthesis(["string(.abc)"])==("string")
    assert remove_parenthesis(["alpha(num)"])==("alpha")

check(remove_parenthesis)