import re
def find_adverb_position(text):
    '''
    Write a function to find the first adverb and their positions in a given sentence.

    Examples:
    find_adverb_position("clearly!! we can see the sky") == (0, 7, 'clearly')
    find_adverb_position("seriously!! there are many roses") == (0, 9, 'seriously')
    find_adverb_position("unfortunately!! sita is going to home") == (0, 13, 'unfortunately')
    '''
    match = re.search(r'\b\w+ly\b', text)
    if match:
        adverb = match.group()
        start_position = match.start()
        end_position = match.end()
        return start_position, end_position, adverb
    return None

def check(candidate):
    assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')
    assert find_adverb_position("seriously!! there are many roses")==(0, 9, 'seriously')
    assert find_adverb_position("unfortunately!! sita is going to home")==(0, 13, 'unfortunately')

check(find_adverb_position)