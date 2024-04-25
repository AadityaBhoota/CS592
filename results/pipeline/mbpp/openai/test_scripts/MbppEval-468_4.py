def max_product(arr):
    dp = [1] * len(arr)  # Initialize the maximum product ending at each index
    subsequences = []    # List to store increasing subsequences

    for i in range(len(arr)):
        # Add the element itself as a subsequence
        subsequences.append([arr[i]])

        for j in range(i):
            if arr[i] > arr[j]:  # If increasing order, update the product
                product = dp[j] * arr[i]
                if product > dp[i]:
                    dp[i] = product
                    # Append the current element to the existing subsequence
                    subsequences[i] = subsequences[j] + [arr[i]]

    max_product = float('-inf')
    for subsequence in subsequences:
        product = 1
        for num in subsequence:
            product *= num
        max_product = max(max_product, product)

    return max_product

def check(candidate):
    assert max_product([3, 100, 4, 5, 150, 6]) == 3000
    assert max_product([4, 42, 55, 68, 80]) == 50265600
    assert max_product([10, 22, 9, 33, 21, 50, 41, 60]) == 2460

check(max_product)