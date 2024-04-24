def sorted_list_sum(lst):
    # Create a new list with only the strings that have even lengths
    even_length_strings = [s for s in lst if len(s) % 2 == 0]
    
    # Sort the list by length, and then alphabetically if lengths are equal
    even_length_strings.sort(key=lambda x: (len(x), x))
    
    return even_length_strings

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