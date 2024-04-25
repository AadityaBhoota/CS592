def reverse_vowels(str1):
    vowels = ['a', 'e', 'i', 'o', 'u']
    char_list = list(str1)
    left, right = 0, len(char_list) - 1

    while left < right:
        if char_list[left].lower() in vowels and char_list[right].lower() in vowels:
            char_list[left], char_list[right] = char_list[right], char_list[left]
            left += 1
            right -= 1
        elif char_list[left].lower() in vowels:
            right -= 1
        elif char_list[right].lower() in vowels:
            left += 1
        else:
            left += 1
            right -= 1

    return ''.join(char_list)

def check(candidate):
    assert reverse_vowels("Python") == "Python"
    assert reverse_vowels("USA") == "ASU"
    assert reverse_vowels("ab") == "ab"

check(reverse_vowels)