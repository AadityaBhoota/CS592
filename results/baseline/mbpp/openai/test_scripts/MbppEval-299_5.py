from collections import defaultdict

def max_aggregate(stdata):
    aggregates = defaultdict(int)
    
    for name, score in stdata:
        aggregates[name] += score
    
    max_name = max(aggregates, key=aggregates.get)
    max_score = aggregates[max_name]
    
    return (max_name, max_score)

# Testing the function




def check(candidate):
    assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
    assert max_aggregate([('Juan Whelan',50),('Sabah Colley',48),('Peter Nichols',37),('Juan Whelan',22),('Sabah Colley',14)])==('Juan Whelan', 72)
    assert max_aggregate([('Juan Whelan',10),('Sabah Colley',20),('Peter Nichols',30),('Juan Whelan',40),('Sabah Colley',50)])==('Sabah Colley', 70)

check(max_aggregate)