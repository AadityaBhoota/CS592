import heapq as hq

def heap_sort(iterable):
    # Convert the iterable to a heap
    h = list(iterable)
    hq.heapify(h)

    # Pop elements from the heap and arrange them in ascending order
    sorted_list = []
    while h:
        sorted_list.append(hq.heappop(h))

    return sorted_list

# Test the function with the given examples




def check(candidate):
    assert heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert heap_sort([25, 35, 22, 85, 14, 65, 75, 25, 58])==[14, 22, 25, 25, 35, 58, 65, 75, 85]
    assert heap_sort( [7, 1, 9, 5])==[1,5,7,9]

check(heap_sort)