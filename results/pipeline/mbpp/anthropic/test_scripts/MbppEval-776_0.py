def count_vowels(test_str):
    count = 0
    vowels = 'aeiou'

    for i in range(len(test_str)):
        if test_str[i].lower() in vowels:
            if (i > 0 and test_str[i-1].lower() in vowels) or (i < len(test_str)-1 and test_str[i+1].lower() in vowels):
                count += 1

    return count

def check(candidate):
    assert count_vowels('bestinstareels') == 7
    assert count_vowels('partofthejourneyistheend') == 12
    assert count_vowels('amazonprime') == 5

check(count_vowels)