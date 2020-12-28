n = 1000 - int(input())

def change(money, n, count):
    i = n//money
    if i:
        count += i
        return (n - (i*money)), count
    return n, count

count = 0
while n:
    n, count = change(500, n, count)
    n, count = change(100, n, count)
    n, count = change(50, n, count)
    n, count = change(10, n, count)
    n, count = change(5, n, count)
    n, count = change(1, n, count)

print(count)


    