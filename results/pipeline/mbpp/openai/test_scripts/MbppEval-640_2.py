import re

def remove_parenthesis(items):
    modified_items = []  # Step 0: Initialize an empty list to hold the modified strings.
    
    for item in items:
        modified_item = re.sub(r'\(.*?\)', '', item)  # Step 3: Remove text within parentheses
        modified_items.append(modified_item.strip())  # Removing any leading or trailing whitespace
        
    return modified_items

def check(candidate):
    assert remove_parenthesis(["python (chrome)"])==("python")
    assert remove_parenthesis(["string(.abc)"])==("string")
    assert remove_parenthesis(["alpha(num)"])==("alpha")

check(remove_parenthesis)