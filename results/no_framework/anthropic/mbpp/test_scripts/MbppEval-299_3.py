from collections import defaultdict

def max_aggregate(stdata):
    """
    Write a function to calculate the maximum aggregate from the list of tuples.

    Examples:
    max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]) == ('Juan Whelan', 212)
    max_aggregate([('Juan Whelan',50),('Sabah Colley',48),('Peter Nichols',37),('Juan Whelan',22),('Sabah Colley',14)]) == ('Juan Whelan', 72)
    max_aggregate([('Juan Whelan',10),('Sabah Colley',20),('Peter Nichols',30),('Juan Whelan',40),('Sabah Colley',50)]) == ('Sabah Colley', 70)
    """
    # Create a defaultdict to store the aggregates for each name
    aggregates = defaultdict(int)

    # Iterate through the input data and update the aggregates
    for name, score in stdata:
        aggregates[name] += score

    # Find the name with the maximum aggregate
    max_name = max(aggregates, key=aggregates.get)
    max_score = aggregates[max_name]

    return (max_name, max_score)

def check(candidate):
    assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
    assert max_aggregate([('Juan Whelan',50),('Sabah Colley',48),('Peter Nichols',37),('Juan Whelan',22),('Sabah Colley',14)])==('Juan Whelan', 72)
    assert max_aggregate([('Juan Whelan',10),('Sabah Colley',20),('Peter Nichols',30),('Juan Whelan',40),('Sabah Colley',50)])==('Sabah Colley', 70)

check(max_aggregate)