def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition.

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """
    vowels = "aeiouAEIOU"
    word_len = len(word)
    
    # Iterate from the right side of the word
    for i in range(word_len-1, -1, -1):
        if word[i] in vowels:
            # Check if the vowel is between two consonants
            left = i - 1
            right = i + 1
            while left >= 0 and right < word_len:
                if word[left] not in vowels and word[right] not in vowels:
                    return word[i]
                left -= 1
                right += 1
    
    # If no vowel is found between two consonants, return an empty string
    return ""

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