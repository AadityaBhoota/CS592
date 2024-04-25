import re
def find_adverbs(text):
    adverbs = re.finditer(r'\b\w+ly\b', text)
    first_adverb = next((adverb for adverb in adverbs), None)
    if first_adverb:
        return f'{first_adverb.start()}-{first_adverb.end()}: {first_adverb.group()}'
    else:
        return "No adverbs ending with 'ly' found in the text."

def check(candidate):
    assert find_adverbs("Clearly, he has no excuse for such behavior.") == '0-7: Clearly'
    assert find_adverbs("Please handle the situation carefuly") == '28-36: carefuly'
    assert find_adverbs("Complete the task quickly") == '18-25: quickly'

check(find_adverbs)