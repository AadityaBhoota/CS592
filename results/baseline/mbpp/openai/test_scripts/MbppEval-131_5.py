def reverse_vowels(str1):
    vowels = 'aeiouAEIOU'
    str_list = list(str1)
    left, right = 0, len(str_list) - 1

    while left < right:
        if str_list[left] not in vowels:
            left += 1
        elif str_list[right] not in vowels:
            right -= 1
        else:
            str_list[left], str_list[right] = str_list[right], str_list[left]
            left += 1
            right -= 1

    return ''.join(str_list)

def check(candidate):
    assert reverse_vowels("Python") == "Python"
    assert reverse_vowels("USA") == "ASU"
    assert reverse_vowels("ab") == "ab"

check(reverse_vowels)