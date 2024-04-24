def is_bored(S):
    boredoms = 0
    sentences =S.split(". ")
    sentences = [sent.strip() for sent in sentences]
    for sent in sentences:
        if sent.startswith("I"):
            boredoms += 1
    return boredoms

# Test cases
print(is_bored("Hello world"))
print(is_bored("The sky is blue. The sun is shining. I love this weather"))

def check(candidate):

    # Check some simple cases
    assert candidate("Hello world") == 0, "Test 1"
    assert candidate("Is the sky blue?") == 0, "Test 2"
    assert candidate("I love It !") == 1, "Test 3"
    assert candidate("bIt") == 0, "Test 4"
    assert candidate("I feel good today. I will be productive. will kill It") == 2, "Test 5"
    assert candidate("You and I are going for a walk") == 0, "Test 6"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(is_bored)