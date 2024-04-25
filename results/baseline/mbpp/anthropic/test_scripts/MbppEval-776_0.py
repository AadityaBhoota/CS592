def count_vowels(test_str):
    """
    Write a function to count those characters which have vowels as their neighbors in the given string.

    Examples:
    count_vowels('bestinstareels') == 7
    count_vowels('partofthejourneyistheend') == 12
    count_vowels('amazonprime') == 5
    """
    vowels = 'aeiou'
    count = 0
    for i in range(len(test_str)):
        if i > 0 and test_str[i-1] in vowels and test_str[i] not in vowels:
            count += 1
        if i < len(test_str) - 1 and test_str[i] not in vowels and test_str[i+1] in vowels:
            count += 1
    return count

def check(candidate):
    assert count_vowels('bestinstareels') == 7
    assert count_vowels('partofthejourneyistheend') == 12
    assert count_vowels('amazonprime') == 5

check(count_vowels)