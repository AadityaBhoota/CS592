def find_adverbs(text):
    adverb_positions = []
    adverbs = re.findall(r'\b\w+ly\b', text)
    for adv in adverbs:
        start = text.find(adv)
        end = start + len(adv)
        adverb_positions.append(f'{start}-{end}: {adv}')
    if adverb_positions:
        return adverb_positions[0]
    return None

# Test cases




def check(candidate):
    assert find_adverbs("Clearly, he has no excuse for such behavior.") == '0-7: Clearly'
    assert find_adverbs("Please handle the situation carefuly") == '28-36: carefuly'
    assert find_adverbs("Complete the task quickly") == '18-25: quickly'

check(find_adverbs)