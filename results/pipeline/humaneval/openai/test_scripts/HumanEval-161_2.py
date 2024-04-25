def solve(s):
    result = ""
    
    has_letters = any(char.isalpha() for char in s)
    
    for char in s:
        if char.isalpha():
            result += char.swapcase()
        else:
            result += char
    
    if not has_letters:
        result = s[::-1]
    
    return result

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