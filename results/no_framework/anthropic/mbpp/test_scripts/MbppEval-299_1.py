from collections import defaultdict

def max_aggregate(stdata):
    """
    Write a function to calculate the maximum aggregate from the list of tuples.

    Examples:
    max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]) == ('Juan Whelan', 212)
    max_aggregate([('Juan Whelan',50),('Sabah Colley',48),('Peter Nichols',37),('Juan Whelan',22),('Sabah Colley',14)]) == ('Juan Whelan', 72)
    max_aggregate([('Juan Whelan',10),('Sabah Colley',20),('Peter Nichols',30),('Juan Whelan',40),('Sabah Colley',50)]) == ('Sabah Colley', 70)
    """
    # Create a defaultdict to store the cumulative scores for each person
    scores = defaultdict(int)

    # Iterate over the list of tuples
    for name, score in stdata:
        # Add the score to the cumulative score for the person
        scores[name] += score

    # Find the person with the maximum aggregate score
    max_name, max_score = max(scores.items(), key=lambda x: x[1])

    return (max_name, max_score)

def check(candidate):
    assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
    assert max_aggregate([('Juan Whelan',50),('Sabah Colley',48),('Peter Nichols',37),('Juan Whelan',22),('Sabah Colley',14)])==('Juan Whelan', 72)
    assert max_aggregate([('Juan Whelan',10),('Sabah Colley',20),('Peter Nichols',30),('Juan Whelan',40),('Sabah Colley',50)])==('Sabah Colley', 70)

check(max_aggregate)