def check(r, c):
    global ans
    for i in range(r-1):  # 첫행부터 직전행까지
        if mem_c[i] == c or abs(r-i) == abs(c-mem_c[i]):  # 지금까지 나온 열인지, 대각선이 겹치는지
            return

    if r == (n-1):  # 종료조건 : 마지막행에 도달했는데 검사를 통과하면
        ans += 1
        return

    mem_c[r] = c
    for i in range(n):
        if i == c or i+1 == c or i-1 == c:  # 다음행 검사시 자기랑 같은열, 대각선열은 검사 X
            continue
        check(r+1, i)

    return


n = int(input())
mem_c = [0]*n  # 각 행의 몇번째 column에 퀸을 놨는지 기록
ans = 0
for i in range(n):  # 첫줄의 각 열에 대해서 한칸씩 놨을때 체크
    check(0, i)
print(ans)
