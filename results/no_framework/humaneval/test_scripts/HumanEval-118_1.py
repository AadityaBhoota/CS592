def get_closest_vowel(word):
    vowels = "aeiouAEIOU"

    last_consonant_idx = None
    closest_vowel = ""
    
    for i in range(len(word) - 1, 0, -1):
        if word[i] not in vowels:
            last_consonant_idx = i
            break
    
    if last_consonant_idx is None or last_consonant_idx == 0:
        return ""
    
    for i in range(last_consonant_idx - 1, 0, -1):
        if word[i] in vowels:
            closest_vowel = word[i]
            break
    
    return closest_vowel

# Test cases





def check(candidate):

    # Check some simple cases
    assert candidate("yogurt") == "u"
    assert candidate("full") == "u"
    assert candidate("easy") == ""
    assert candidate("eAsy") == ""
    assert candidate("ali") == ""
    assert candidate("bad") == "a"
    assert candidate("most") == "o"
    assert candidate("ab") == ""
    assert candidate("ba") == ""
    assert candidate("quick") == ""
    assert candidate("anime") == "i"
    assert candidate("Asia") == ""
    assert candidate("Above") == "o"

    # Check some edge cases that are easy to work out by hand.
    assert True


check(get_closest_vowel)