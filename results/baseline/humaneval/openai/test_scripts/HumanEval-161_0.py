def solve(s):
    letters = [c for c in s if c.isalpha()]
    
    if not letters:
        return s[::-1]
    
    result = ''
    for c in s:
        if c.isalpha():
            if c.islower():
                result += c.upper()
            else:
                result += c.lower()
        else:
            result += c
    
    return result

# Test cases




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