s, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(s)]
Mi = [[1 if i == j else 0 for j in range(s)] for i in range(s)]


def Mmul(A, B):
    result = [[0 for _ in range(s)] for _ in range(s)]
    for r in range(s):
        for c in range(s):
            for k in range(s):
                result[r][c] = (result[r][c]+A[r][k]*B[k][c]) % 1000
    return result


def solve(Mat, n):
    if n == 1:
        return Mmul(Mat, Mi)
    if n % 2 == 0:
        temp = solve(Mat, n//2)
        return Mmul(temp, temp)
    else:
        return Mmul(solve(Mat, n-1), Mat)


ans = solve(arr, b)

for i in ans:
    print(*i)
