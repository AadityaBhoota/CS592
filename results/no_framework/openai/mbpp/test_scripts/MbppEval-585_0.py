import heapq

def expensive_items(items, n):
    # Create a min heap to store items based on price
    min_heap = []
    
    # Insert items into the heap
    for item in items:
        heapq.heappush(min_heap, (-item['price'], item['name']))  # Use negative price for max heap effect
    
    # Get the n most expensive items
    result = []
    for _ in range(n):
        if min_heap:
            price, name = heapq.heappop(min_heap)
            result.append({'name': name, 'price': -price})  # Convert back to positive price
    
    return result

# Test cases




def check(candidate):
    assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
    assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09}],2)==[{'name': 'Item-2', 'price': 555.22},{'name': 'Item-1', 'price': 101.1}]
    assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09},{'name': 'Item-4', 'price': 22.75}],1)==[{'name': 'Item-2', 'price': 555.22}]

check(expensive_items)