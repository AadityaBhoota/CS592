import re

def find_literals(text, pattern):
    result = re.search(pattern, text)
    if result:
        substring = result.group(0)
        start_index = result.start()
        end_index = result.end() - 1
        return substring, start_index, end_index
    else:
        return None

# Test examples




def check(candidate):
    assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
    assert find_literals('Its been a very crazy procedure right', 'crazy') == ('crazy', 16, 21)
    assert find_literals('Hardest choices required strongest will', 'will') == ('will', 35, 39)

check(find_literals)