import re

def find_adverb_position(text):
    """
    Write a function to find the first adverb and their positions in a given sentence.

    Examples:
    find_adverb_position("clearly!! we can see the sky") == (0, 7, 'clearly')
    find_adverb_position("seriously!! there are many roses") == (0, 9, 'seriously')
    find_adverb_position("unfortunately!! sita is going to home") == (0, 13, 'unfortunately')
    """
    # Define a regular expression pattern to match adverbs
    adverb_pattern = r'\w+ly'

    # Find the first match of the adverb pattern in the text
    match = re.search(adverb_pattern, text)

    if match:
        # Get the start and end indices of the matched adverb
        start = match.start()
        end = match.end()
        # Get the matched adverb
        adverb = match.group()
        return (start, end, adverb)
    else:
        return None

def check(candidate):
    assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')
    assert find_adverb_position("seriously!! there are many roses")==(0, 9, 'seriously')
    assert find_adverb_position("unfortunately!! sita is going to home")==(0, 13, 'unfortunately')

check(find_adverb_position)