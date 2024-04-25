def numerical_letter_grade(grades):
    """
    It is the last week of the semester and the teacher has to give the grades
    to students. The teacher has been making her own algorithm for grading.
    The only problem is, she has lost the code she used for grading.
    She has given you a list of GPAs for some students and you have to write
    a function that can output a list of letter grades using the following table:
             GPA       |    Letter grade
              4.0                A+
            > 3.7                A
            > 3.3                A-
            > 3.0                B+
            > 2.7                B
            > 2.3                B-
            > 2.0                C+
            > 1.7                C
            > 1.3                C-
            > 1.0                D+
            > 0.7                D
            > 0.0                D-
              0.0                E

    Example:
    grade_equation([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'A', 'C', 'B', 'A-']
    """
    letter_grades = []  # Step 1: Create an empty list to store the letter grades

    # Step 2: Iterate over each GPA and calculate the corresponding letter grade
    for gpa in grades:
        if 0.0 <= gpa <= 4.0:  # Check if GPA is within valid range
            if gpa == 4.0:
                letter_grades.append('A+')
            elif 3.7 < gpa <= 4.0:
                letter_grades.append('A')
            elif 3.3 < gpa <= 3.7:
                letter_grades.append('A-')
            elif 3.0 < gpa <= 3.3:
                letter_grades.append('B+')
            elif 2.7 < gpa <= 3.0:
                letter_grades.append('B')
            elif 2.3 < gpa <= 2.7:
                letter_grades.append('B-')
            elif 2.0 < gpa <= 2.3:
                letter_grades.append('C+')
            elif 1.7 < gpa <= 2.0:
                letter_grades.append('C')
            elif 1.3 < gpa <= 1.7:
                letter_grades.append('C-')
            elif 1.0 < gpa <= 1.3:
                letter_grades.append('D+')
            elif 0.7 < gpa <= 1.0:
                letter_grades.append('D')
            elif 0.0 < gpa <= 0.7:
                letter_grades.append('D-')
        else:
            letter_grades.append('Invalid GPA')  # Handle invalid GPA case
    
    return letter_grades  # Step 5: Return the list of calculated letter grades

def check(candidate):

    # Check some simple cases
    assert candidate([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']
    assert candidate([1.2]) == ['D+']
    assert candidate([0.5]) == ['D-']
    assert candidate([0.0]) == ['E']
    assert candidate([1, 0.3, 1.5, 2.8, 3.3]) == ['D', 'D-', 'C-', 'B', 'B+']
    assert candidate([0, 0.7]) == ['E', 'D-']

    # Check some edge cases that are easy to work out by hand.
    assert True


check(numerical_letter_grade)