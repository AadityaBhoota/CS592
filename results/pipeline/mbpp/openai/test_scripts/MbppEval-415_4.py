def max_Product(arr): 
    max_product = 0
    pair = ()
    num_neg = 0
    num_zeros = 0

    def max_product_pair(arr):
        nonlocal max_product, pair, num_neg, num_zeros

        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                product = arr[i] * arr[j]
                if product > max_product:
                    max_product = product
                    pair = (arr[i], arr[j])
                if arr[i] < 0 or arr[j] < 0:
                    num_neg += 1
                if arr[i] == 0 or arr[j] == 0:
                    num_zeros += 1

    max_product_pair(arr)

    if num_zeros == len(arr) or (num_neg == 0 and num_zeros > 0):
        pair = (0, 0)
    elif num_neg % 2 != 0:
        max_product = 0

    return pair

def check(candidate):
    assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
    assert max_Product([0,-1,-2,-4,5,0,-6]) == (-4,-6)
    assert max_Product([1,2,3]) == (2,3)

check(max_Product)