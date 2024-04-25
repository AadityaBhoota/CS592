from collections import defaultdict

def count_Substrings(s, n):
    def getSubstrings(s):
        substrings = []
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                substrings.append(s[i:j])
        return substrings

    def digitSum(s):
        return sum(int(d) for d in s)

    substrings = getSubstrings(s)
    count = 0
    for sub in substrings:
        if len(sub) == digitSum(sub):
            count += 1

    return count

# Test the function




def check(candidate):
    assert count_Substrings('112112') == 6
    assert count_Substrings('111') == 6
    assert count_Substrings('1101112') == 12

check(count_Substrings)