import re

def fix_spaces(text):
    # Step 0: Replace all spaces with underscores
    text = text.replace(' ', '_')
    
    # Step 1: Replace all instances of more than 2 consecutive spaces with a single underscore using regular expressions
    result = re.sub(r'( {2,})', '_', text)
    
    return result

def check(candidate):

    # Check some simple cases
    assert candidate("Example") == "Example", "This prints if this assert fails 1 (good for debugging!)"
    assert candidate("Mudasir Hanif ") == "Mudasir_Hanif_", "This prints if this assert fails 2 (good for debugging!)"
    assert candidate("Yellow Yellow  Dirty  Fellow") == "Yellow_Yellow__Dirty__Fellow", "This prints if this assert fails 3 (good for debugging!)"
    
    # Check some edge cases that are easy to work out by hand.
    assert candidate("Exa   mple") == "Exa-mple", "This prints if this assert fails 4 (good for debugging!)"
    assert candidate("   Exa 1 2 2 mple") == "-Exa_1_2_2_mple", "This prints if this assert fails 4 (good for debugging!)"


check(fix_spaces)