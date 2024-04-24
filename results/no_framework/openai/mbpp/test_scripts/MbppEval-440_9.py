def find_adverb_position(text):
    # Define a regular expression pattern to match adverbs
    pattern = r'\b\w+ly\b'
    
    # Search for the first adverb in the text
    match = re.search(pattern, text)
    
    if match:
        start_index = match.start()
        end_index = match.end()
        adverb = match.group()
        return start_index, end_index, adverb
    else:
        return None

# Testing the function with examples




def check(candidate):
    assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')
    assert find_adverb_position("seriously!! there are many roses")==(0, 9, 'seriously')
    assert find_adverb_position("unfortunately!! sita is going to home")==(0, 13, 'unfortunately')

check(find_adverb_position)