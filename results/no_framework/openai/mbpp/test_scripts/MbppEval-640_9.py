import re
def remove_parenthesis(items):
    cleaned_items = []
    for item in items:
        cleaned_item = re.sub(r'\(.*?\)', '', item)
        cleaned_items.append(cleaned_item.strip())
    return tuple(cleaned_items)

# Test cases




def check(candidate):
    assert remove_parenthesis(["python (chrome)"])==("python")
    assert remove_parenthesis(["string(.abc)"])==("string")
    assert remove_parenthesis(["alpha(num)"])==("alpha")

check(remove_parenthesis)