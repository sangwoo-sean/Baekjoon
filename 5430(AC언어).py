import sys
input = sys.stdin.readline
from collections import deque

for _ in range(int(input())):
    op = input().rstrip()
    n = int(input())
    els = input().rstrip()
    q = deque(els.strip("[]").split(","))

    err = False
    if op.count("D") > n:
        err = True
    else:
        f = 0 # front
        b = n # back
        direction = "ff"
        for i in op:
            if i == "R":
                if direction == "ff": #front first
                    direction = "bf" #back first
                else: direction = "ff"
            else:
                if direction == "ff":
                    f += 1
                else: b -= 1

    if err:
        print("error")
    else:
        if direction == "ff":
            print(f"[{','.join(i for i in list(q)[f:b])}]")
        else:
            print(f"[{','.join(i for i in reversed(list(q)[f:b]))}]")