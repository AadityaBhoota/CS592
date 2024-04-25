def reverse_vowels(str1):
    """
    Write a python function to reverse only the vowels of a given string (where y is not a vowel).

    Examples:
    reverse_vowels("Python") == "Python"
    reverse_vowels("USA") == "ASU"
    reverse_vowels("ab") == "ab"
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    char_list = list(str1)
    left, right = 0, len(char_list) - 1
    while left < right:
        if char_list[left] in vowels:
            while right > left and char_list[right] not in vowels:
                right -= 1
            if right > left:
                char_list[left], char_list[right] = char_list[right], char_list[left]
                right -= 1
        left += 1
    return ''.join(char_list)

def check(candidate):
    assert reverse_vowels("Python") == "Python"
    assert reverse_vowels("USA") == "ASU"
    assert reverse_vowels("ab") == "ab"

check(reverse_vowels)