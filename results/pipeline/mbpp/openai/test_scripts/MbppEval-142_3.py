def count_samepair(list1, list2, list3):
    count = 0
    if len(list1) != len(list2) or len(list1) != len(list3):
        raise ValueError("Input lists must be of the same length")
    
    for item1, item2, item3 in zip(list1, list2, list3):
        if item1 == item2 == item3:
            count += 1
    
    return count

def check(candidate):
    assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3
    assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,8],[2,1,3,1,2,6,7,8])==4
    assert count_samepair([1,2,3,4,2,6,7,8],[2,2,3,1,2,6,7,8],[2,1,3,1,2,6,7,8])==5

check(count_samepair)