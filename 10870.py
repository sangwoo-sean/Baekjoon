x = int(input())
x = x+1
mylist = [0, 1]

def fib(mylist, n, l):
    if n == l:
        return
    mylist.append(mylist[n-1] + mylist[n-2])
    fib(mylist, n+1, l)
    
if x == 1:
    print(0)
else:
    fib(mylist, 2, x)

    print(mylist[-1])