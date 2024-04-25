import re

def find_adverb_position(text):
    adverb_regex = r'\b\w+ly\b'
    matches = re.search(adverb_regex, text)
    if matches:
        adverb = matches.group()
        start_position = matches.start()
        end_position = matches.end()
        return start_position, end_position, adverb
    return None

def check(candidate):
    assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')
    assert find_adverb_position("seriously!! there are many roses")==(0, 9, 'seriously')
    assert find_adverb_position("unfortunately!! sita is going to home")==(0, 13, 'unfortunately')

check(find_adverb_position)