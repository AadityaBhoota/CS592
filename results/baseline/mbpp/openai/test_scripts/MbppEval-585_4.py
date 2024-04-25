import heapq

def expensive_items(items, n):
    # Create a min heap with negative prices for efficient extraction of largest prices
    max_heap = []
    for item in items:
        heapq.heappush(max_heap, (-item['price'], item['name']))

    # Extract top n expensive items from the max heap
    most_expensive = []
    for _ in range(min(n, len(max_heap))):
        price, name = heapq.heappop(max_heap)
        most_expensive.append({'name': name, 'price': -price})

    return most_expensive

# Test cases




def check(candidate):
    assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
    assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09}],2)==[{'name': 'Item-2', 'price': 555.22},{'name': 'Item-1', 'price': 101.1}]
    assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09},{'name': 'Item-4', 'price': 22.75}],1)==[{'name': 'Item-2', 'price': 555.22}]

check(expensive_items)