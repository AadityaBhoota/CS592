def start_withp(words):
    result = []
    for word in words:
        match = re.findall(r'\bp\S+', word)
        result.extend(match)
    
    if len(result) >= 2:
        return tuple(result[:2])
    else:
        return tuple(result + [''] * (2 - len(result)))

# Test the function




def check(candidate):
    assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
    assert start_withp(["Python Programming","Java Programming"])==('Python','Programming')
    assert start_withp(["Pqrst Pqr","qrstuv"])==('Pqrst','Pqr')

check(start_withp)