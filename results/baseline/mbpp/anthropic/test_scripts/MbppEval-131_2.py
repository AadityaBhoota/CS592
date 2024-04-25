def reverse_vowels(str1):
    """
    Write a python function to reverse only the vowels of a given string (where y is not a vowel).

    Examples:
    reverse_vowels("Python") == "Python"
    reverse_vowels("USA") == "ASU"
    reverse_vowels("ab") == "ab"
    """
    vowels = "aeiou"
    chars = list(str1)
    left, right = 0, len(chars) - 1

    while left < right:
        if chars[left].lower() in vowels and chars[right].lower() in vowels:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        elif chars[left].lower() in vowels:
            right -= 1
        else:
            left += 1

    return ''.join(chars)

def check(candidate):
    assert reverse_vowels("Python") == "Python"
    assert reverse_vowels("USA") == "ASU"
    assert reverse_vowels("ab") == "ab"

check(reverse_vowels)