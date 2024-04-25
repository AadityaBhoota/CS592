import re

def start_withp(words):
    result = []
    count = 0
    for word_str in words:
        for word in word_str.split():
            if re.match(r'[pP]\w+', word):
                result.append(word)
                count += 1
                if count == 2:
                    return tuple(result)

# Testing the function


def check(candidate):
    assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
    assert start_withp(["Python Programming","Java Programming"])==('Python','Programming')
    assert start_withp(["Pqrst Pqr","qrstuv"])==('Pqrst','Pqr')

check(start_withp)