def solve(s):
    reversed_string = ""
    
    has_letter = False
    for char in s:
        if char.isalpha():
            has_letter = True
            if char.islower():
                reversed_string += char.upper()
            else:
                reversed_string += char.lower()
        else:
            reversed_string += char
    
    if not has_letter:
        return s[::-1]
    
    return reversed_string

# Test the examples




def check(candidate):

    # Check some simple cases
    assert candidate("AsDf") == "aSdF"
    assert candidate("1234") == "4321"
    assert candidate("ab") == "AB"
    assert candidate("#a@C") == "#A@c"
    assert candidate("#AsdfW^45") == "#aSDFw^45"
    assert candidate("#6@2") == "2@6#"

    # Check some edge cases that are easy to work out by hand.
    assert candidate("#$a^D") == "#$A^d"
    assert candidate("#ccc") == "#CCC"

    # Don't remove this line:

check(solve)