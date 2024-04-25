def compare(game, guess):
    differences = []  # Step 0: Create an empty list to store the differences
    
    # Step 1: Iterate over the elements of the game and guess arrays simultaneously using zip
    for score, prediction in zip(game, guess):
        # Step 2: Calculate the absolute difference between the score and prediction
        diff = abs(score - prediction)
        differences.append(diff)
    
    # Step 3: Return the list of differences
    return differences

def check(candidate):

    # Check some simple cases
    assert candidate([1,2,3,4,5,1],[1,2,3,4,2,-2])==[0,0,0,0,3,3], "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([0,0,0,0,0,0],[0,0,0,0,0,0])==[0,0,0,0,0,0], "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([1,2,3],[-1,-2,-3])==[2,4,6], "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([1,2,3,5],[-1,2,3,4])==[2,0,0,1], "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(compare)