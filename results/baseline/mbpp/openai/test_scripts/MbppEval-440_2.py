import re

def find_adverb_position(text):
    adverb_match = re.search(r'\b(\w+ly)\b', text)
    if adverb_match:
        adverb = adverb_match.group(1)
        start = adverb_match.start()
        end = adverb_match.end()
        return start, end, adverb
    else:
        return None

# Test cases




def check(candidate):
    assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')
    assert find_adverb_position("seriously!! there are many roses")==(0, 9, 'seriously')
    assert find_adverb_position("unfortunately!! sita is going to home")==(0, 13, 'unfortunately')

check(find_adverb_position)