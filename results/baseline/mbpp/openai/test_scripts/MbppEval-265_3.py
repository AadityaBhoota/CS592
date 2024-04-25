def list_split(S, step):
    result = [[] for _ in range(step)]
    for i, item in enumerate(S):
        result[i % step].append(item)
    return [lst for lst in result if lst]

# Test cases




def check(candidate):
    assert list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],3)==[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
    assert list_split([1,2,3,4,5,6,7,8,9,10,11,12,13,14],3)==[[1,4,7,10,13], [2,5,8,11,14], [3,6,9,12]]
    assert list_split(['python','java','C','C++','DBMS','SQL'],2)==[['python', 'C', 'DBMS'], ['java', 'C++', 'SQL']]

check(list_split)