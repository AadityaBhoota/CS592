def find_adverbs(text):
    adverb_positions = []
    adverb = ""
    words = re.findall(r'\b\w+\b', text)
    for i, word in enumerate(words):
        if word.endswith("ly"):
            adverb_positions.append(f"{sum(len(w) + 1 for w in words[:i])}-{sum(len(w) + 1 for w in words[:i]) + len(word)}: {word}")
    if adverb_positions:
        return adverb_positions[0]
    else:
        return None

# Test cases




def check(candidate):
    assert find_adverbs("Clearly, he has no excuse for such behavior.") == '0-7: Clearly'
    assert find_adverbs("Please handle the situation carefuly") == '28-36: carefuly'
    assert find_adverbs("Complete the task quickly") == '18-25: quickly'

check(find_adverbs)