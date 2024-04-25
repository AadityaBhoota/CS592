import re

def find_literals(text, pattern):
    '''
    Write a function to search a string for a regex pattern. The function should return the matching subtring, a start index and an end index.

    Examples:
    find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
    find_literals('Its been a very crazy procedure right', 'crazy') == ('crazy', 16, 21)
    find_literals('Hardest choices required strongest will', 'will') == ('will', 35, 39)
    '''
    match = re.search(pattern, text)
    if match:
        matched_substr = match.group()
        start_index = match.start()
        end_index = match.end() - 1  # Adjust end index to correctly represent the matched substring
        return matched_substr, start_index, end_index
    else:
        return None

def check(candidate):
    assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
    assert find_literals('Its been a very crazy procedure right', 'crazy') == ('crazy', 16, 21)
    assert find_literals('Hardest choices required strongest will', 'will') == ('will', 35, 39)

check(find_literals)