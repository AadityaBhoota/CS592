def find_max(words):
    max_unique_word = ""
    max_unique_count = -1
    
    for word in words:
        unique_count = len(set(word))
        if unique_count > max_unique_count:
            max_unique_count = unique_count
            max_unique_word = word
        elif unique_count == max_unique_count and word < max_unique_word:
            max_unique_word = word
            
    return max_unique_word

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