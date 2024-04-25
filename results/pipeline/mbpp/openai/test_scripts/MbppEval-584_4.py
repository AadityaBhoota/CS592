import re

def find_adverbs(text):
    words = re.findall(r'\b\w+\b', text)
    
    for i, word in enumerate(words):
        if word.endswith('ly') and len(word) > 2:
            start = sum(len(words[j])+1 for j in range(i))
            end = start + len(word)
            return f"{start}-{end}: {word}"
    
    return "No adverb ending with 'ly' found."

# Testing the function with examples




def check(candidate):
    assert find_adverbs("Clearly, he has no excuse for such behavior.") == '0-7: Clearly'
    assert find_adverbs("Please handle the situation carefuly") == '28-36: carefuly'
    assert find_adverbs("Complete the task quickly") == '18-25: quickly'

check(find_adverbs)