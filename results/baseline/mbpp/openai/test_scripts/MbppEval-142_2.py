def count_samepair(list1, list2, list3):
    count = 0
    for item1, item2, item3 in zip(list1, list2, list3):
        if item1 == item2 == item3:
            count += 1
    return count

# Test cases




def check(candidate):
    assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3
    assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,8],[2,1,3,1,2,6,7,8])==4
    assert count_samepair([1,2,3,4,2,6,7,8],[2,2,3,1,2,6,7,8],[2,1,3,1,2,6,7,8])==5

check(count_samepair)