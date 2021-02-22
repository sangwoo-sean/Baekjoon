R, C, T = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(R)]

airF = []
for i in range(R):
    for j in range(C):
        if MAP[i][j] == -1:
            airF.append(i)

directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def create_next_map():
    new_map = [[0]*C for _ in range(R)]
    new_map[airF[0]][0] = -1
    new_map[airF[1]][0] = -1
    return new_map


def dusting(maplist):
    new_map = create_next_map()
    for r in range(R):
        for c in range(C):
            if not maplist[r][c] or maplist[r][c] == -1:
                continue
            dust = maplist[r][c]
            count = 0
            for d in directions:
                dr, dc = d
                nr = r + dr
                nc = c + dc
                if 0 <= nr < R and 0 <= nc < C and maplist[nr][nc] != -1:
                    new_map[nr][nc] += dust // 5
                    count += 1
            new_map[r][c] += maplist[r][c] - (dust//5)*count
    return new_map


def counter_clock(r):
    MAP[r-1][0] = 0
    for i in range(r-2, -1, -1):
        MAP[i+1][0] = MAP[i][0]
    for i in range(1, C):
        MAP[0][i-1] = MAP[0][i]
    for i in range(1, r+1):
        MAP[i-1][C-1] = MAP[i][C-1]
    for i in range(C-2, 0, -1):
        MAP[r][i+1] = MAP[r][i]
    MAP[r][1] = 0
    return


def clock(r):
    MAP[r+1][0] = 0
    for i in range(r+2, R):
        MAP[i-1][0] = MAP[i][0]
    for i in range(1, C):
        MAP[R-1][i-1] = MAP[R-1][i]
    for i in range(R-2, r-1, -1):
        MAP[i+1][C-1] = MAP[i][C-1]
    for i in range(C-2, 0, -1):
        MAP[r][i+1] = MAP[r][i]
    MAP[r][1] = 0
    return


def air_freshening():
    top = airF[0]
    bot = airF[1]
    counter_clock(top)
    clock(bot)
    return


for _ in range(T):
    MAP = dusting(MAP)
    air_freshening()

total = 0
for i in MAP:
    total += sum(i)
print(total+2)
