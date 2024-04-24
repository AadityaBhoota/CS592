import re

def find_adverbs(text):
    adverb_positions = []
    adverb_words = []

    # Using regular expression to find adverbs
    pattern = r'\b\w+ly\b'
    for match in re.finditer(pattern, text):
        adverb_positions.append((match.start(), match.end()))
        adverb_words.append(match.group())

    if adverb_words:
        first_adverb_pos = adverb_positions[0]
        first_adverb_word = adverb_words[0]
        return f'{first_adverb_pos[0]}-{first_adverb_pos[1]-1}: {first_adverb_word}'
    else:
        return None

# Test cases




def check(candidate):
    assert find_adverbs("Clearly, he has no excuse for such behavior.") == '0-7: Clearly'
    assert find_adverbs("Please handle the situation carefuly") == '28-36: carefuly'
    assert find_adverbs("Complete the task quickly") == '18-25: quickly'

check(find_adverbs)