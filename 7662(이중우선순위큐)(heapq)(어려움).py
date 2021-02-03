import heapq
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    minH = []
    maxH = []
    alive = [False]*1000001
    for i in range(int(input())):
        op, n = input().rstrip().split()

        if op == "I":
            heapq.heappush(minH, (int(n), i))
            heapq.heappush(maxH, (-int(n), i))
            alive[i] = True
        
        elif op == "D":
            if n == "1":
                while maxH and not alive[maxH[0][1]]:
                    heapq.heappop(maxH)
                if maxH:
                    alive[maxH[0][1]] = False
                    heapq.heappop(maxH)


            elif n == "-1":
                while minH and not alive[minH[0][1]]:
                    heapq.heappop(minH)
                if minH:
                    alive[minH[0][1]] = False
                    heapq.heappop(minH)

    while maxH and not alive[maxH[0][1]]: # maxH 가 비거나 최대값이 살아있는 노드일때 종료
        heapq.heappop(maxH)
    while minH and not alive[minH[0][1]]: # minH 가 비거나 최소값이 살아있는 노드일때 종료
        heapq.heappop(minH)

    if maxH and minH:
        print(-1*maxH[0][0], minH[0][0])
    else:
        print("EMPTY")