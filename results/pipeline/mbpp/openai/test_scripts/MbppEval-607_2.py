import re

def find_literals(text, pattern):
    match = re.search(pattern, text)
    if match:
        start_index = match.start()
        end_index = match.end()
        matching_substring = match.group()
        return matching_substring, start_index, end_index

def check(candidate):
    assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
    assert find_literals('Its been a very crazy procedure right', 'crazy') == ('crazy', 16, 21)
    assert find_literals('Hardest choices required strongest will', 'will') == ('will', 35, 39)

check(find_literals)