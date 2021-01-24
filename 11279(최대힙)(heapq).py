import sys
input = sys.stdin.readline
import heapq

n = int(input())
heap = []
for _ in range(n):
    get = int(input())

    if get:
        heapq.heappush(heap, -1*get)
        
    else:
        if heap:
            print(-1* heapq.heappop(heap))
        else:
            print(0)









### 시간초과
# from collections import deque

# n = int(input())
# heap = deque([])
# for _ in range(n):
#     get = int(input())
    
#     if get:
#         heap.append(get)

#     else:
#         if heap:
#             tar = max(heap)
#             print(tar)
#             heap.remove(tar)
#         else:
#             print(0)

    