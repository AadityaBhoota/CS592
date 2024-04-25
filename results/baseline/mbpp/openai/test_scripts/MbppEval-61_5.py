def count_Substrings(s):
    def calculate_sum(s):
        total = 0
        for char in s:
            total += int(char)
        return total

    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            if len(substring) == calculate_sum(substring):
                count += 1
    return count

# Test cases




def check(candidate):
    assert count_Substrings('112112') == 6
    assert count_Substrings('111') == 6
    assert count_Substrings('1101112') == 12

check(count_Substrings)