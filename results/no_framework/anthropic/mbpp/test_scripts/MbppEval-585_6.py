import heapq

def expensive_items(items, n):
    """
    Write a function to find the n most expensive items in a given dataset.

    Examples:
    expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1) == [{'name': 'Item-2', 'price': 555.22}]
    expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09}],2) == [{'name': 'Item-2', 'price': 555.22},{'name': 'Item-1', 'price': 101.1}]
    expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09},{'name': 'Item-4', 'price': 22.75}],1) == [{'name': 'Item-2', 'price': 555.22}]
    """
    # Create a min heap with the negative price as the key
    heap = [(-item['price'], item) for item in items]
    heapq.heapify(heap)

    # Pop the n most expensive items from the heap
    result = [heapq.heappop(heap)[1] for _ in range(n)]

    return result

def check(candidate):
    assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
    assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09}],2)==[{'name': 'Item-2', 'price': 555.22},{'name': 'Item-1', 'price': 101.1}]
    assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09},{'name': 'Item-4', 'price': 22.75}],1)==[{'name': 'Item-2', 'price': 555.22}]

check(expensive_items)