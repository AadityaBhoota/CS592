import re

def find_adverbs(text):
    adverb_positions = []
    adverbs = re.findall(r'\b\w+ly\b', text)
    
    for adverb in adverbs:
        start_position = text.find(adverb)
        end_position = start_position + len(adverb) - 1
        adverb_positions.append(f'{start_position}-{end_position}: {adverb}')
    
    return adverb_positions[0] if adverb_positions else None

# Test cases




def check(candidate):
    assert find_adverbs("Clearly, he has no excuse for such behavior.") == '0-7: Clearly'
    assert find_adverbs("Please handle the situation carefuly") == '28-36: carefuly'
    assert find_adverbs("Complete the task quickly") == '18-25: quickly'

check(find_adverbs)