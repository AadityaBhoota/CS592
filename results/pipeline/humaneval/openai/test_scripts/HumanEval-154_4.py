def cycpattern_check(a, b):
    def rotations(word):
        word_rotations = []
        for i in range(len(word)):
            rotated_word = word[i:] + word[:i]
            word_rotations.append(rotated_word)
        return word_rotations

    word_rotations = rotations(b)
    
    for rotation in word_rotations:
        if rotation in a:
            return True
    
    return False

def check(candidate):

    # Check some simple cases
    #assert True, "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    #assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert  candidate("xyzw","xyw") == False , "test #0"
    assert  candidate("yello","ell") == True , "test #1"
    assert  candidate("whattup","ptut") == False , "test #2"
    assert  candidate("efef","fee") == True , "test #3"
    assert  candidate("abab","aabb") == False , "test #4"
    assert  candidate("winemtt","tinem") == True , "test #5"


check(cycpattern_check)