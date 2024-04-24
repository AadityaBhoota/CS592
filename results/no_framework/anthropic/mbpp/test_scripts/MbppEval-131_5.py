def reverse_vowels(str1):
    """
    Write a python function to reverse only the vowels of a given string (where y is not a vowel).

    Examples:
    reverse_vowels("Python") == "Python"
    reverse_vowels("USA") == "ASU"
    reverse_vowels("ab") == "ab"
    """
    vowels = "aeiou"
    str_list = list(str1)
    left, right = 0, len(str_list) - 1

    while left < right:
        if str_list[left].lower() in vowels and str_list[right].lower() in vowels:
            str_list[left], str_list[right] = str_list[right], str_list[left]
            left += 1
            right -= 1
        elif str_list[left].lower() not in vowels:
            left += 1
        else:
            right -= 1

    return "".join(str_list)

def check(candidate):
    assert reverse_vowels("Python") == "Python"
    assert reverse_vowels("USA") == "ASU"
    assert reverse_vowels("ab") == "ab"

check(reverse_vowels)