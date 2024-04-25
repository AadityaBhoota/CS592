def find_max(words):
    unique_char_count = {}
    
    # Step 1: Iterate through each word and count the number of unique characters in each word
    for word in words:
        unique_chars = set(word)
        unique_char_count[word] = (len(unique_chars), word)
    
    # Step 2: Find the word with the maximum number of unique characters
    max_unique_chars = max(unique_char_count.values(), key=lambda x: (x[0], x[1]))
    
    return max_unique_chars[1]

def check(candidate):

    # Check some simple cases
    assert (candidate(["name", "of", "string"]) == "string"), "t1"
    assert (candidate(["name", "enam", "game"]) == "enam"), 't2'
    assert (candidate(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"), 't3'
    assert (candidate(["abc", "cba"]) == "abc"), 't4'
    assert (candidate(["play", "this", "game", "of","footbott"]) == "footbott"), 't5'
    assert (candidate(["we", "are", "gonna", "rock"]) == "gonna"), 't6'
    assert (candidate(["we", "are", "a", "mad", "nation"]) == "nation"), 't7'
    assert (candidate(["this", "is", "a", "prrk"]) == "this"), 't8'

    # Check some edge cases that are easy to work out by hand.
    assert (candidate(["b"]) == "b"), 't9'
    assert (candidate(["play", "play", "play"]) == "play"), 't10'


check(find_max)