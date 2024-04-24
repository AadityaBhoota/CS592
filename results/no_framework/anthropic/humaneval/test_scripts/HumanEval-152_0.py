def compare(game, guess):
    """
    Compares the actual game scores with the guessed scores and returns an array
    of the absolute difference between each guess and the corresponding game score.
    If a guess is correct, the value in the returned array is 0.

    Args:
        game (list): A list of integers representing the actual game scores.
        guess (list): A list of integers representing the guessed scores.

    Returns:
        list: A list of integers, where each element represents the absolute
        difference between the corresponding guess and game score, or 0 if the
        guess was correct.
    """
    if len(game) != len(guess):
        raise ValueError("Game and guess lists must be of equal length.")

    result = []
    for i in range(len(game)):
        if game[i] == guess[i]:
            result.append(0)
        else:
            result.append(abs(game[i] - guess[i]))

    return result

def check(candidate):

    # Check some simple cases
    assert candidate([1,2,3,4,5,1],[1,2,3,4,2,-2])==[0,0,0,0,3,3], "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([0,0,0,0,0,0],[0,0,0,0,0,0])==[0,0,0,0,0,0], "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([1,2,3],[-1,-2,-3])==[2,4,6], "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([1,2,3,5],[-1,2,3,4])==[2,0,0,1], "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(compare)