from collections import defaultdict

def max_aggregate(stdata):
    # Create a dictionary to store the total scores for each student
    student_scores = defaultdict(int)
    
    # Iterate over the list of tuples and aggregate the scores for each student
    for student, score in stdata:
        student_scores[student] += score
    
    # Find the student with the highest total score
    max_student, max_score = max(student_scores.items(), key=lambda x: x[1])
    
    return max_student, max_score

# Test the function with the provided examples




def check(candidate):
    assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
    assert max_aggregate([('Juan Whelan',50),('Sabah Colley',48),('Peter Nichols',37),('Juan Whelan',22),('Sabah Colley',14)])==('Juan Whelan', 72)
    assert max_aggregate([('Juan Whelan',10),('Sabah Colley',20),('Peter Nichols',30),('Juan Whelan',40),('Sabah Colley',50)])==('Sabah Colley', 70)

check(max_aggregate)