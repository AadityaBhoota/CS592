import re

def find_adverbs(text):
    adverbs = re.findall(r'\b\w+ly\b', text)
    if adverbs:
        first_adverb = adverbs[0]
        start_index = text.find(first_adverb)
        end_index = start_index + len(first_adverb) - 1
        return '{}-{}: {}'.format(start_index, end_index, first_adverb)
    else:
        return None

# Test the function




def check(candidate):
    assert find_adverbs("Clearly, he has no excuse for such behavior.") == '0-7: Clearly'
    assert find_adverbs("Please handle the situation carefuly") == '28-36: carefuly'
    assert find_adverbs("Complete the task quickly") == '18-25: quickly'

check(find_adverbs)