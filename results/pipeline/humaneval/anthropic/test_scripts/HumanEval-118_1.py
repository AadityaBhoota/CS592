def get_closest_vowel(word):
    vowels = 'aeiouAEIOU'
    closest_vowel = ""
    for i in range(len(word)-1, -1, -1):
        if word[i] in vowels:
            if (i == 0 or not word[i-1] in vowels) and (i == len(word)-1 or not word[i+1] in vowels):
                continue
            if i > 0 and i < len(word)-1 and word[i-1] not in vowels and word[i+1] not in vowels:
                closest_vowel = word[i]
                break
    return closest_vowel

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