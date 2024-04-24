def sorted_list_sum(lst):
    # Create a new list to store the filtered and sorted words
    filtered_words = []
    
    # Filter out the words with odd lengths
    for word in lst:
        if len(word) % 2 == 0:
            filtered_words.append(word)
    
    # Sort the filtered words first by length and then alphabetically
    filtered_words.sort(key=lambda x: (len(x), x))
    
    return filtered_words

# Test cases
assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def check(candidate):

    # Check some simple cases
    assert candidate(["aa", "a", "aaa"]) == ["aa"]
    assert candidate(["school", "AI", "asdf", "b"]) == ["AI", "asdf", "school"]
    assert candidate(["d", "b", "c", "a"]) == []
    assert candidate(["d", "dcba", "abcd", "a"]) == ["abcd", "dcba"]

    # Check some edge cases that are easy to work out by hand.
    assert candidate(["AI", "ai", "au"]) == ["AI", "ai", "au"]
    assert candidate(["a", "b", "b", "c", "c", "a"]) == []
    assert candidate(['aaaa', 'bbbb', 'dd', 'cc']) == ["cc", "dd", "aaaa", "bbbb"]


check(sorted_list_sum)