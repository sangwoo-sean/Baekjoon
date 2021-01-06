from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

d = deque([])

for i in range(n):
    a = input().rstrip()

    if a[0:2] == "pu" :
        if a[5] == "f":
            d.appendleft(int(a.split()[1]))
            continue
        else:
            d.append(int(a.split()[1]))
            continue

    elif a[0:3] == "pop":
        if a[4] == "f":
            if len(d) == 0:
                print(-1)
                continue
            else:
                print(d.popleft())
                continue
        else:
            if len(d) == 0:
                print(-1)
                continue
            else:
                print(d.pop())
                continue
    
    elif a == 'size':
        print(len(d))
        continue
    
    elif a == 'empty':
        if len(d) == 0:
            print(1)
            continue
        else:
            print(0)
            continue
    
    elif a == 'front':
        if len(d) == 0:
            print(-1)
            continue
        else:
            print(d[0])
            continue

    elif a == 'back':
        if len(d) == 0:
            print(-1)
            continue
        else:
            print(d[-1])
            continue

