def find_adverbs(text):
    adverbs = re.findall(r'\b\w+ly\b', text)
    if adverbs:
        adverb = adverbs[0]
        start = text.find(adverb)
        end = start + len(adverb)
        return f'{start}-{end}: {adverb}'
    




def check(candidate):
    assert find_adverbs("Clearly, he has no excuse for such behavior.") == '0-7: Clearly'
    assert find_adverbs("Please handle the situation carefuly") == '28-36: carefuly'
    assert find_adverbs("Complete the task quickly") == '18-25: quickly'

check(find_adverbs)