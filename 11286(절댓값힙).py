import heapq
import sys
input = sys.stdin.readline

q = []

for i in range(int(input())):
    get = int(input())


    if get:
        heapq.heappush(q, [abs(get), get])
    
    else:
        if q:
            print(heapq.heappop(q)[1])
        else:
            print(0)
    print(q)