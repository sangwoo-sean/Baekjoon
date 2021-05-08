from collections import deque


def solution(places):
    answer = []
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]

    for place in places:
        valid = True
        ps = []
        for r in range(5):
            for c in range(5):
                if place[r][c] == "P":
                    ps.append([r, c, 0])

        for p in ps:
            print(p)
            if not valid:
                break

            q = deque([p])
            visit = [[False for _ in range(5)] for _ in range(5)]

            while q:
                r, c, d = q.popleft()
                visit[r][c] = True

                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]

                    if 0 <= nr < 5 and 0 <= nc < 5 and not visit[nr][nc] and d < 2:
                        if place[nr][nc] == 'O':
                            q.append([nr, nc, d+1])
                        if place[nr][nc] == 'P':
                            valid = False

        if valid:
            answer.append(1)
        else:
            answer.append(0)

    return answer
