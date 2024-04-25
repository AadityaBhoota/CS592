import re

def find_adverb_position(text):
    match = re.search(r'\b([a-zA-Z]+ly)\b', text)
    if match:
        return match.start(), match.end(), match.group()
    else:
        return None

# Test the function with the given examples




def check(candidate):
    assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')
    assert find_adverb_position("seriously!! there are many roses")==(0, 9, 'seriously')
    assert find_adverb_position("unfortunately!! sita is going to home")==(0, 13, 'unfortunately')

check(find_adverb_position)