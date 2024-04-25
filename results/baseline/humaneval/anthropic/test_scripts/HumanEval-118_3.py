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
    vowels = 'aeiou'
    
    # Iterate from the right side of the word
    for i in range(len(word)-1, -1, -1):
        # Check if the current character is a consonant
        if word[i].lower() not in vowels:
            # Search for the closest vowel from the right side
            for j in range(i-1, -1, -1):
                if word[j].lower() in vowels:
                    # Check if the vowel is between two consonants
                    if j > 0 and j < len(word)-1 and word[j-1].lower() not in vowels and word[j+1].lower() not in vowels:
                        return word[j]
    
    # If no vowel is found between two consonants, return an empty string
    return ''

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