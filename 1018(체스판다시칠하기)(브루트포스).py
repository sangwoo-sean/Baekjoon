# N, M = 10, 13



# mylist = [
# "WBWBWBWB",
# "BWBWBWBW",
# "WBWBWBWB",
# "BWBBBWBW",
# "WBWBWBWB",
# "BWBWBWBW",
# "WBWBWBWB",
# "BWBWBWBW"
# ]

# mylist = ['BBBBBBBBWBWBW',
# 'BBBBBBBBBWBWB',
# 'BBBBBBBBWBWBW',
# 'BBBBBBBBBWBWB',
# 'BBBBBBBBWBWBW',
# 'BBBBBBBBBWBWB',
# 'BBBBBBBBWBWBW',
# 'BBBBBBBBBWBWB',
# 'WWWWWWWWWWBWB',
# 'WWWWWWWWWWBWB']
N, M = map(int, input().split())
mylist = [input() for _ in range(N)]

strict = [
"WBWBWBWB",
"BWBWBWBW",
"WBWBWBWB",
"BWBWBWBW",
"WBWBWBWB",
"BWBWBWBW",
"WBWBWBWB",
"BWBWBWBW"
]

mymin = 65
for a in range(N-7):#0~2
    for b in range(M-7):#0~5
        case = []
        for c in range(8):
           case.append(mylist[c+a][b:b+8])
        
        # for i in range(8):
        #     print(case[i])


        count = 0
        # if case[0][0] == 'W':
        for i in range(8):
            for j in range(8):
                if case[i][j] != strict[i][j]:
                    count += 1
        if mymin > count:
            mymin = count
        # elif case[0][0] == "B":
        count = 0
        for i in range(8):
            for j in range(8):
                if case[i][j] == strict[i][j]:
                    count += 1
        if mymin > count:
            mymin = count
        # print(count)

print(mymin)

