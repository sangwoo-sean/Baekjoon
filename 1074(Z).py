

n, r, c = map(int, input().split())

num=0
def solve(n):
    global r, c, num

    if n == 0:
        return num
    x = 2**(n-1)
    y = 2**(n-1)

    if c < x and r < y: # 1사분면
        pass
    elif c >= x and r < y: # 2사분면
        num += 4**(n-1)
        c -= 2**(n-1)
    elif c < x and r >= y: # 3사분면
        num += 4**(n-1)*2
        r -= 2**(n-1)
    else: # 4사분면
        num += 4**(n-1)*3
        r -= 2**(n-1)
        c -= 2**(n-1)
    
    return solve(n-1)
    
print(solve(n))
