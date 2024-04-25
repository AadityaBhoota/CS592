def remove_parenthesis(items):
    new_items = []
    for item in items:
        new_item = re.sub(r'\(.*?\)', '', item)
        new_item = new_item.strip()
        new_items.append(new_item)
    return tuple(new_items)

# Test cases




def check(candidate):
    assert remove_parenthesis(["python (chrome)"])==("python")
    assert remove_parenthesis(["string(.abc)"])==("string")
    assert remove_parenthesis(["alpha(num)"])==("alpha")

check(remove_parenthesis)