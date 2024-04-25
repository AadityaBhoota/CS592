def subject_marks(subjectmarks):
    sorted_list = sorted(subjectmarks, key=lambda x: x[1])
    return sorted_list

# Test cases




def check(candidate):
    assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
    assert subject_marks([('Telugu',49),('Hindhi',54),('Social',33)])==([('Social',33),('Telugu',49),('Hindhi',54)])
    assert subject_marks([('Physics',96),('Chemistry',97),('Biology',45)])==([('Biology',45),('Physics',96),('Chemistry',97)])

check(subject_marks)