import re

def find_adverb_position(text):
    """
    Write a function to find the first adverb and their positions in a given sentence.

    Examples:
    find_adverb_position("clearly!! we can see the sky") == (0, 7, 'clearly')
    find_adverb_position("seriously!! there are many roses") == (0, 9, 'seriously')
    find_adverb_position("unfortunately!! sita is going to home") == (0, 13, 'unfortunately')
    """
    # Define the regular expression pattern to match adverbs
    pattern = r'\w+ly'
    
    # Search for the first adverb in the text
    match = re.search(pattern, text)
    
    if match:
        # Get the start and end indices of the matched adverb
        start = match.start()
        end = match.end()
        
        # Extract the adverb from the text
        adverb = text[start:end]
        
        # Return the adverb and its positions
        return (start, end, adverb)
    else:
        # If no adverb is found, return None
        return None

def check(candidate):
    assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')
    assert find_adverb_position("seriously!! there are many roses")==(0, 9, 'seriously')
    assert find_adverb_position("unfortunately!! sita is going to home")==(0, 13, 'unfortunately')

check(find_adverb_position)