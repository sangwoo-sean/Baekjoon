A, B, C, D, E = map(float, input().split())
n, m = map(int, input().split())
Ys, Os = [], []
scoreD = {
    'A': A,
    'B': B,
    'C': C,
    'D': D,
    'E': E,
}

status = [input() for _ in range(n)]
genre = [input() for _ in range(n)]

for i in range(n):
    for j in range(m):
        if status[i][j] == "Y":
            Ys.append([i, j, genre[i][j]])
        if status[i][j] == "O":
            Os.append([i, j, genre[i][j]])

Ys.sort(key=lambda x: scoreD[x[2]], reverse=True)
Os.sort(key=lambda x: scoreD[x[2]], reverse=True)

for i in Ys:
    print(i[2], scoreD[i[2]], i[0], i[1])
for i in Os:
    print(i[2], scoreD[i[2]], i[0], i[1])
