def find_max(words):
    unique_char_counts = {}
    max_unique_count = 0
    max_unique_words = []

    for word in words:
        unique_count = len(set(word))
        unique_char_counts[word] = unique_count

        if unique_count > max_unique_count:
            max_unique_count = unique_count
            max_unique_words = [word]
        elif unique_count == max_unique_count:
            max_unique_words.append(word)

    if max_unique_words:
        max_unique_words.sort()
        return max_unique_words[0]
    else:
        return ""

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