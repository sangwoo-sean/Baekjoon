def toint(st, n):
    result = 0
    for i, e in enumerate(st):
        if D[e] >= n:
            return -1
        result += D[e] * n**(len(st)-1-i)
    return result


A, B = input().split()

D = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "a": 10,
    "b": 11,
    "c": 12,
    "d": 13,
    "e": 14,
    "f": 15,
    "g": 16,
    "h": 17,
    "i": 18,
    "j": 19,
    "k": 20,
    "l": 21,
    "m": 22,
    "n": 23,
    "o": 24,
    "p": 25,
    "q": 26,
    "r": 27,
    "s": 28,
    "t": 29,
    "u": 30,
    "v": 31,
    "w": 32,
    "x": 33,
    "y": 34,
    "z": 35,
}

ans = []
for i in range(2, 37):
    for j in range(2, 37):
        if i == j:
            continue
        NA = toint(A, i)
        NB = toint(B, j)
        if NA == -1 or NA == -1:
            continue
        if NA == NB:
            ans.append([NA, i, j])

if len(ans) == 0:
    print("Impossible")
elif len(ans) > 1:
    print("Multiple")
else:
    print(*ans[0])
