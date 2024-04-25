import heapq

def expensive_items(items, n):
    """
    Find the n most expensive items in a given dataset.
    """
    # Create a max heap to store the n most expensive items
    heap = []

    # Iterate through the items and update the heap
    for item in items:
        if len(heap) < n:
            heapq.heappush(heap, (-item['price'], item))
        elif -heap[0][0] < item['price']:
            heapq.heappop(heap)
            heapq.heappush(heap, (-item['price'], item))

    # Return the n most expensive items
    return [item for _, item in heap]

def check(candidate):
    assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
    assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09}],2)==[{'name': 'Item-2', 'price': 555.22},{'name': 'Item-1', 'price': 101.1}]
    assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09},{'name': 'Item-4', 'price': 22.75}],1)==[{'name': 'Item-2', 'price': 555.22}]

check(expensive_items)