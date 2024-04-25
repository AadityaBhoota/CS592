def count_Substrings(s):
    def getSumOfDigits(num):
        return sum(int(digit) for digit in str(num))

    def countSubstringsWithSum(s):
        count = 0
        sumDict = defaultdict(int)
        sumDict[0] = 1
        prefixSum = 0
        for digit in s:
            prefixSum += int(digit)
            diff = prefixSum - getSumOfDigits(prefixSum)
            count += sumDict[diff]
            sumDict[diff] += 1
        return count

    return countSubstringsWithSum(s)

# Examples




def check(candidate):
    assert count_Substrings('112112') == 6
    assert count_Substrings('111') == 6
    assert count_Substrings('1101112') == 12

check(count_Substrings)