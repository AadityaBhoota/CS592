import re

def remove_parenthesis(items):
    result = []
    pattern = r'\(.*?\)'
    
    for item in items:
        modified_item = re.sub(pattern, '', item)
        result.append(modified_item.strip())
    
    return tuple(result)

# Test cases




def check(candidate):
    assert remove_parenthesis(["python (chrome)"])==("python")
    assert remove_parenthesis(["string(.abc)"])==("string")
    assert remove_parenthesis(["alpha(num)"])==("alpha")

check(remove_parenthesis)