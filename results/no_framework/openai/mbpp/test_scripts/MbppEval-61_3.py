def count_Substrings(s):
    def getSubstringsCount(s):
        count = 0
        for i in range(len(s)):
            num = 0
            for j in range(i, len(s)):
                num += int(s[j])
                if num == j - i + 1:
                    count += 1
        return count

    return getSubstringsCount(s)

# Test cases




def check(candidate):
    assert count_Substrings('112112') == 6
    assert count_Substrings('111') == 6
    assert count_Substrings('1101112') == 12

check(count_Substrings)