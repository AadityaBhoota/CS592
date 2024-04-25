import re

def extract_values(text):
    values = re.findall(r'"(.*?)"', text)
    values = [value.strip() for value in values]
    return values

def check(candidate):
    assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']
    assert extract_values('"python","program","language"')==['python','program','language']
    assert extract_values('"red","blue","green","yellow"')==['red','blue','green','yellow']

check(extract_values)