def extract_values(text):
    values = re.findall(r'"(.*?)"', text)
    return values

# Test cases




def check(candidate):
    assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']
    assert extract_values('"python","program","language"')==['python','program','language']
    assert extract_values('"red","blue","green","yellow"')==['red','blue','green','yellow']

check(extract_values)