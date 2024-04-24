def minPath(grid, k):
    from heapq import heappush, heappop

    n = len(grid)
    heap = [(grid[i][0], i, 0) for i in range(n)]
    visited = set()

    while k > 0:
        val, i, j = heappop(heap)
        visited.add((i, j))
        k -= 1

        if j+1 < n and (i, j+1) not in visited:
            heappush(heap, (grid[i][j+1], i, j+1))
        if i+1 < n and (i+1, j) not in visited:
            heappush(heap, (grid[i+1][j], i+1, j))

    return [grid[i][j] for i, j in visited]


# Test cases
grid1 = [[1,2,3], [4,5,6], [7,8,9]]
k1 = 3
print(minPath(grid1, k1))  # Output: [1, 2, 1]

grid2 = [[5,9,3], [4,1,6], [7,8,2]]
k2 = 1
print(minPath(grid2, k2))  # Output: [1]

def check(candidate):

    # Check some simple cases
    print
    assert candidate([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3) == [1, 2, 1]
    assert candidate([[5, 9, 3], [4, 1, 6], [7, 8, 2]], 1) == [1]
    assert candidate([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 4) == [1, 2, 1, 2]
    assert candidate([[6, 4, 13, 10], [5, 7, 12, 1], [3, 16, 11, 15], [8, 14, 9, 2]], 7) == [1, 10, 1, 10, 1, 10, 1]
    assert candidate([[8, 14, 9, 2], [6, 4, 13, 15], [5, 7, 1, 12], [3, 10, 11, 16]], 5) == [1, 7, 1, 7, 1]
    assert candidate([[11, 8, 7, 2], [5, 16, 14, 4], [9, 3, 15, 6], [12, 13, 10, 1]], 9) == [1, 6, 1, 6, 1, 6, 1, 6, 1]
    assert candidate([[12, 13, 10, 1], [9, 3, 15, 6], [5, 16, 14, 4], [11, 8, 7, 2]], 12) == [1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6]
    assert candidate([[2, 7, 4], [3, 1, 5], [6, 8, 9]], 8) == [1, 3, 1, 3, 1, 3, 1, 3]
    assert candidate([[6, 1, 5], [3, 8, 9], [2, 7, 4]], 8) == [1, 5, 1, 5, 1, 5, 1, 5]

    # Check some edge cases that are easy to work out by hand.
    assert candidate([[1, 2], [3, 4]], 10) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
    assert candidate([[1, 3], [3, 2]], 10) == [1, 3, 1, 3, 1, 3, 1, 3, 1, 3]


check(minPath)