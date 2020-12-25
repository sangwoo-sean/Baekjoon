
nint = int(input())
na = 1
for i in range(nint):
    mytry = str(i)
    nums = list(map(int, [k for k in mytry]))
    result = i + sum(nums)
    if result == nint:
        print(i)
        na = 0
        break
if na == 1:
    print(0)

