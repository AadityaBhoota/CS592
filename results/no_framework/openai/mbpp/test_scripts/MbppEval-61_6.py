from collections import defaultdict

def count_Substrings(s):
    def count_substrings_helper(s):
        result = 0
        current_sum = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1

        for char in s:
            current_sum += int(char)
            diff = current_sum - len(str(current_sum))
            result += prefix_sums[diff]
            prefix_sums[current_sum - len(str(current_sum))] += 1

        return result

    return count_substrings_helper(s)

# Test cases




def check(candidate):
    assert count_Substrings('112112') == 6
    assert count_Substrings('111') == 6
    assert count_Substrings('1101112') == 12

check(count_Substrings)