import re

def extract_values(text):
    """
    Write a function to extract values between quotation marks from a string.

    Examples:
    extract_values('"Python", "PHP", "Java"') == ['Python', 'PHP', 'Java']
    extract_values('"python","program","language"') == ['python','program','language']
    extract_values('"red","blue","green","yellow"') == ['red','blue','green','yellow']
    """
    pattern = r'"([^"]*)"'
    return re.findall(pattern, text)

def check(candidate):
    assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']
    assert extract_values('"python","program","language"')==['python','program','language']
    assert extract_values('"red","blue","green","yellow"')==['red','blue','green','yellow']

check(extract_values)