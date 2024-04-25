def start_withp(words):
    result = []
    for word in words:
        # Using regular expression to find words starting with 'p'
        matches = re.findall(r'\bP\w+', word)
        result.extend(matches)
    if len(result) >= 2:
        return tuple(result[:2])
    elif len(result) == 1:
        return tuple(result + [''])
    else:
        return ('', '')
def check(candidate):
    assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
    assert start_withp(["Python Programming","Java Programming"])==('Python','Programming')
    assert start_withp(["Pqrst Pqr","qrstuv"])==('Pqrst','Pqr')

check(start_withp)