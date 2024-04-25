import heapq

def expensive_items(items, n):
    most_expensive = []

    for item in items:
        if len(most_expensive) < n:
            heapq.heappush(most_expensive, (item['price'], item))
        elif item['price'] > most_expensive[0][0]:
            heapq.heappop(most_expensive)
            heapq.heappush(most_expensive, (item['price'], item))

    return [item[1] for item in most_expensive]

def check(candidate):
    assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
    assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09}],2)==[{'name': 'Item-2', 'price': 555.22},{'name': 'Item-1', 'price': 101.1}]
    assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09},{'name': 'Item-4', 'price': 22.75}],1)==[{'name': 'Item-2', 'price': 555.22}]

check(expensive_items)