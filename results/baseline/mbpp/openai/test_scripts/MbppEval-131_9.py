def reverse_vowels(str1):
    vowels = 'aeiouAEIOU'
    str1 = list(str1)
    i, j = 0, len(str1) - 1
    while i < j:
        if str1[i] not in vowels:
            i += 1
        elif str1[j] not in vowels:
            j -= 1
        else:
            str1[i], str1[j] = str1[j], str1[i]
            i += 1
            j -= 1
    return ''.join(str1)

def check(candidate):
    assert reverse_vowels("Python") == "Python"
    assert reverse_vowels("USA") == "ASU"
    assert reverse_vowels("ab") == "ab"

check(reverse_vowels)