def remove_length(test_str, K):
    """
    Write a function to remove all the words with length K in the given string.

    Examples:
    remove_length('The person is most value tet', 3) == 'person is most value'
    remove_length('If you told me about this ok', 4) == 'If you me about ok'
    remove_length('Forces of darkeness is come into the play', 4) == 'Forces of darkeness is the'
    """
    words = test_str.split()
    result = []
    for word in words:
        if len(word) != K:
            result.append(word)
    return ' '.join(result)

def check(candidate):
    assert remove_length('The person is most value tet', 3) == 'person is most value'
    assert remove_length('If you told me about this ok', 4) == 'If you me about ok'
    assert remove_length('Forces of darkeness is come into the play', 4) == 'Forces of darkeness is the'

check(remove_length)