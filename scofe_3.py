n = int(input())

MAP = [input() for _ in range(n)]

sizes = [0]*(n+1)
for size in range(1, n+1):

    for r in range(n-size+1):
        for c in range(n-size+1):
            valid = 0
            for i in range(size):
                if MAP[r+i][c:c+size].count("0"):
                    break
                else:
                    valid += 1
                if valid == size:
                    sizes[size] += 1

print(f"total: {sum(sizes)}")
for i in range(n+1):
    if sizes[i]:
        print(f"size[{i}]: {sizes[i]}")
