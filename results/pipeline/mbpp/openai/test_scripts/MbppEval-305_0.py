import re
def start_withp(words):
    # Step 1
    words_list = [word for sentence in words for word in sentence.split()]
    
    # Step 2
    p_words = [word for word in words_list if re.match(r'^[Pp]', word)]
    
    # Step 3
    return tuple(p_words[:2])

def check(candidate):
    assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
    assert start_withp(["Python Programming","Java Programming"])==('Python','Programming')
    assert start_withp(["Pqrst Pqr","qrstuv"])==('Pqrst','Pqr')

check(start_withp)