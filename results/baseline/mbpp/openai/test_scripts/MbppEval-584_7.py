import re

def find_adverbs(text):
    adverb_pattern = r'\b\w+ly\b'
    matches = re.finditer(adverb_pattern, text)
    for match in matches:
        start = match.start()
        end = match.end()
        adverb = match.group()
        return f'{start}-{end}: {adverb}'

# Test cases




def check(candidate):
    assert find_adverbs("Clearly, he has no excuse for such behavior.") == '0-7: Clearly'
    assert find_adverbs("Please handle the situation carefuly") == '28-36: carefuly'
    assert find_adverbs("Complete the task quickly") == '18-25: quickly'

check(find_adverbs)