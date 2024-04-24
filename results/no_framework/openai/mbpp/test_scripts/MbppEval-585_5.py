import heapq

def expensive_items(items, n):
    # Create a min heap
    min_heap = []
    
    for item in items:
        heapq.heappush(min_heap, (-item['price'], item))
        # Push the negative price to make it a max heap
    
    result = []
    for _ in range(n):
        if min_heap:
            _, expensive_item = heapq.heappop(min_heap)
            result.append(expensive_item)
    
    return result

# Test the function with examples




def check(candidate):
    assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
    assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09}],2)==[{'name': 'Item-2', 'price': 555.22},{'name': 'Item-1', 'price': 101.1}]
    assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09},{'name': 'Item-4', 'price': 22.75}],1)==[{'name': 'Item-2', 'price': 555.22}]

check(expensive_items)