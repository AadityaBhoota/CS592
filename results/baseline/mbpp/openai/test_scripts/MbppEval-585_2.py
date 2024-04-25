import heapq

def expensive_items(items, n):
    # Create a min heap to store the items based on price
    heap = []
    
    # Iterate over each item in the input list and push the negative price to the heap
    for item in items:
        heapq.heappush(heap, (-item['price'], item))
    
    # Get the n most expensive items from the heap
    result = [heapq.heappop(heap)[1] for _ in range(n)]
    
    return result

# Test cases




def check(candidate):
    assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
    assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09}],2)==[{'name': 'Item-2', 'price': 555.22},{'name': 'Item-1', 'price': 101.1}]
    assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09},{'name': 'Item-4', 'price': 22.75}],1)==[{'name': 'Item-2', 'price': 555.22}]

check(expensive_items)