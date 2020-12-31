from itertools import combinations
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):  
    n = int(input())
    mylist = input().split()

    if n >= 33:
        print(0)
        continue
    
    else:
        cases = combinations(mylist, 3)
        result = []
        for case in cases:
            p_list = [[case[0], case[1]], [case[1], case[2]], [case[0], case[2]]]
            
            score = 0
            for i in range(3):
                for l in range(4):
                    if p_list[i][0][l] != p_list[i][1][l]:
                        score +=1
            result.append(score)
        print(min(result))