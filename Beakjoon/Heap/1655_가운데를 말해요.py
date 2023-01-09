import heapq

N = int(input())
max_heap, min_heap = [], []

for _ in range(N):
    num = int(input())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, num * (-1))
    else:
        heapq.heappush(min_heap, num)

    if max_heap and min_heap:
        max_value = max_heap[0] * (-1)
        min_value = min_heap[0]
        if max_value > min_value:
            heapq.heappop(max_heap)
            heapq.heappop(min_heap)
            heapq.heappush(max_heap, min_value * (-1))
            heapq.heappush(min_heap, max_value)

    print(max_heap[0] * (-1))
