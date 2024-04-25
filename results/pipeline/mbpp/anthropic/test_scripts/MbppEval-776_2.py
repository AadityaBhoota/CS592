def count_vowels(test_str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    
    for i in range(len(test_str)):
        if test_str[i] in vowels:
            if (i > 0 and test_str[i-1] in vowels) or (i < len(test_str)-1 and test_str[i+1] in vowels):
                count += 1
    
    return count

def check(candidate):
    assert count_vowels('bestinstareels') == 7
    assert count_vowels('partofthejourneyistheend') == 12
    assert count_vowels('amazonprime') == 5

check(count_vowels)