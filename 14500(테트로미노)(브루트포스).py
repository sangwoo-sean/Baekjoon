def check(x,y):
    tetris = [
    [(x, y), (x+1, y), (x, y+1), (x+1, y+1)],#ㅁ
    [(x, y), (x+1, y), (x+2, y), (x+3, y)],#ㅣ
    [(x, y), (x, y+1), (x, y+2), (x, y+3)],#ㅡ
    [(x, y), (x+1, y), (x+2, y), (x, y+1)], # ㅣ + .
    [(x, y), (x+1, y), (x+2, y), (x, y-1)],
    [(x, y), (x+1, y), (x+2, y), (x+1, y+1)],
    [(x, y), (x+1, y), (x+2, y), (x+1, y-1)],
    [(x, y), (x+1, y), (x+2, y), (x+2, y+1)],
    [(x, y), (x+1, y), (x+2, y), (x+2, y-1)],
    [(x, y), (x, y+1), (x, y+2), (x+1, y)], # ㅡ + .
    [(x, y), (x, y+1), (x, y+2), (x-1, y)],
    [(x, y), (x, y+1), (x, y+2), (x+1, y+1)],
    [(x, y), (x, y+1), (x, y+2), (x-1, y+1)],
    [(x, y), (x, y+1), (x, y+2), (x+1, y+2)],
    [(x, y), (x, y+1), (x, y+2), (x-1, y+2)],
    [(x, y), (x+1, y), (x+1, y-1), (x+2, y-1)],#z
    [(x, y), (x+1, y), (x+1, y+1), (x+2, y+1)],
    [(x, y), (x, y+1), (x+1, y+1), (x+1, y+2)],
    [(x, y), (x, y+1), (x-1, y+1), (x-1, y+2)]
    ]
    big = 0
    for i in range(19):
        mysum = 0
        for j in range(4):
            a = tetris[i][j][0]
            b = tetris[i][j][1]
            if not 0<=a<n or not 0<=b<m:
                break
            mysum += mylist[a][b]
        big = max(mysum, big)
    return big

n, m = map(int, input().split())
mylist = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, check(i,j))
print(ans)