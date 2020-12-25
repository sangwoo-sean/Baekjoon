def get_each_num(n):
    result = 0
    mul = 1
    mylist = []
    if n < 10:
        mylist.append(n)
    else:
        while mul <= n:
            mylist.append(int(((n % (mul*10)) - (n % mul)) / mul))
            mul *= 10
    
    return mylist

def check_cond(a):
    if len(a) == 1:
        return "y"
    gap = []
    for i in range(len(a)-1):
        gap.append(a[i] - a[i+1])
    for i in range(len(gap)-1):
        if gap[i] == gap[i+1]:
            continue
        else:
            return "n"
    return "y"

def count_han(n):
    count = 0
    for i in range(1, n+1):
        a = get_each_num(i)
        ans = check_cond(a)
        if ans == "y":
            count += 1
    print(count)
num = int(input())
count = count_han(num)