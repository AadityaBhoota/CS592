def compare(game, guess):
    return [0 if game[i] == guess[i] else abs(game[i] - guess[i]) for i in range(len(game))]

# Testing the function with the provided examples
print(compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]))  # Output: [0, 0, 0, 0, 3, 3]
print(compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]))  # Output: [4, 4, 1, 0, 0, 6]

def check(candidate):

    # Check some simple cases
    assert candidate([1,2,3,4,5,1],[1,2,3,4,2,-2])==[0,0,0,0,3,3], "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([0,0,0,0,0,0],[0,0,0,0,0,0])==[0,0,0,0,0,0], "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([1,2,3],[-1,-2,-3])==[2,4,6], "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([1,2,3,5],[-1,2,3,4])==[2,0,0,1], "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(compare)