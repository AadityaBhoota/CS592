import re

def find_adverbs(text):
    adverb_positions = []
    adverb_words = []

    # Find all words ending with 'ly' using regex
    words = re.findall(r'\b\w+ly\b', text)

    # Find the positions of the adverbs in the text
    for word in words:
        start_pos = text.find(word)
        end_pos = start_pos + len(word)
        adverb_positions.append(f"{start_pos}-{end_pos}")
        adverb_words.append(word)

    if adverb_positions:
        return f"{adverb_positions[0]}: {adverb_words[0]}"
    else:
        return None

# Test cases




def check(candidate):
    assert find_adverbs("Clearly, he has no excuse for such behavior.") == '0-7: Clearly'
    assert find_adverbs("Please handle the situation carefuly") == '28-36: carefuly'
    assert find_adverbs("Complete the task quickly") == '18-25: quickly'

check(find_adverbs)