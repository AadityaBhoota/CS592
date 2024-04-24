def find_adverbs(text):
    adverb = re.search(r'\b\w+ly\b', text)
    if adverb:
        start_pos = adverb.start()
        end_pos = adverb.end()
        return f"{start_pos}-{end_pos}: {adverb.group()}"
    return None

# Test cases




def check(candidate):
    assert find_adverbs("Clearly, he has no excuse for such behavior.") == '0-7: Clearly'
    assert find_adverbs("Please handle the situation carefuly") == '28-36: carefuly'
    assert find_adverbs("Complete the task quickly") == '18-25: quickly'

check(find_adverbs)