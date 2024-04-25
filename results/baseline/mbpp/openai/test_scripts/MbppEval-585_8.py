import heapq

def expensive_items(items, n):
    # Create a max heap to store the items based on price
    max_heap = []
    
    # Push items into the heap with negative price to achieve max heap behavior
    for item in items:
        heapq.heappush(max_heap, (-item['price'], item))
    
    # Get the n most expensive items
    result = []
    for _ in range(n):
        price, item = heapq.heappop(max_heap)
        result.append(item)
    
    return result

# Test cases




def check(candidate):
    assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
    assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09}],2)==[{'name': 'Item-2', 'price': 555.22},{'name': 'Item-1', 'price': 101.1}]
    assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09},{'name': 'Item-4', 'price': 22.75}],1)==[{'name': 'Item-2', 'price': 555.22}]

check(expensive_items)