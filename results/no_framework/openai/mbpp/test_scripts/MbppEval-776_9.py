def count_vowels(test_str):
    vowels = set('aeiou')
    count = 0

    for i in range(1, len(test_str) - 1):
        if test_str[i] in vowels and (test_str[i-1] in vowels or test_str[i+1] in vowels):
            count += 1

    return count

# Test cases




def check(candidate):
    assert count_vowels('bestinstareels') == 7
    assert count_vowels('partofthejourneyistheend') == 12
    assert count_vowels('amazonprime') == 5

check(count_vowels)