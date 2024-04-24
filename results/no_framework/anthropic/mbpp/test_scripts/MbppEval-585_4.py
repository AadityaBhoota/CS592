import heapq

def expensive_items(items, n):
    """
    Find the n most expensive items in a given dataset.

    Args:
        items (list): A list of dictionaries, where each dictionary represents an item with a 'name' and 'price' key.
        n (int): The number of most expensive items to return.

    Returns:
        list: A list of dictionaries, where each dictionary represents the n most expensive items.
    """
    # Create a min-heap of the items, sorted by price
    heap = [(-item['price'], item) for item in items]
    heapq.heapify(heap)

    # Pop the n most expensive items from the heap
    result = [heapq.heappop(heap)[1] for _ in range(min(n, len(items)))]

    return result

def check(candidate):
    assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
    assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09}],2)==[{'name': 'Item-2', 'price': 555.22},{'name': 'Item-1', 'price': 101.1}]
    assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09},{'name': 'Item-4', 'price': 22.75}],1)==[{'name': 'Item-2', 'price': 555.22}]

check(expensive_items)