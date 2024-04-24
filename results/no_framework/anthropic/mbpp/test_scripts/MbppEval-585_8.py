import heapq

def expensive_items(items, n):
    """
    Find the n most expensive items in a given dataset.

    Args:
        items (list): A list of dictionaries, where each dictionary represents an item with 'name' and 'price' keys.
        n (int): The number of most expensive items to return.

    Returns:
        list: A list of the n most expensive items.
    """
    # Create a list of (price, item) tuples, sorted by price in descending order
    price_items = [(-item['price'], item) for item in items]
    heapq.heapify(price_items)

    # Get the n most expensive items
    result = [heapq.heappop(price_items)[1] for _ in range(min(n, len(items)))]
    return result

def check(candidate):
    assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
    assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09}],2)==[{'name': 'Item-2', 'price': 555.22},{'name': 'Item-1', 'price': 101.1}]
    assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09},{'name': 'Item-4', 'price': 22.75}],1)==[{'name': 'Item-2', 'price': 555.22}]

check(expensive_items)