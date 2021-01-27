n = 8

mylist = [
    [1,1,1,1,0,0,0,0],
    [1,1,1,1,0,0,0,0],
    [0,0,0,1,1,1,0,0],
    [0,0,0,1,1,1,0,0],
    [1,1,1,1,0,0,0,0],
    [1,1,1,1,0,0,0,0],
    [1,1,1,1,0,0,1,1],
    [1,1,1,1,0,0,1,1]
]

import sys
input = sys.stdin.readline
n = int(input())
mylist = [[int(i) for i in input().rstrip()] for _ in range(n)]

def show(mat):
    for i in mat:
        print(i)
    print()

def check(array):
    l = len(array)
    start = array[0][0]
    for i in range(l):
        for j in range(l):
            if start != array[i][j]:
                return False
    return True

def solve(arr):
    if check(arr):
        print(arr[0][0], end="")
        return

    l = len(arr) // 2
    print("(", end="")
    for i in range(4):
        temp_arr = []
        for j in range(l):
            temp_arr.append(arr[(i//2)*l+j][(i%2)*l:(i%2)*l+l])
        solve(temp_arr)
    print(")", end="")

solve(mylist)

