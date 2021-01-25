import heapq
import sys
input = sys.stdin.readline

q = []

for i in range(int(input())):
    get = int(input())

    if get:
        heapq.heappush(q, get)
    else:
        if q:
            print(heapq.heappop(q))
        else:
            print(0)