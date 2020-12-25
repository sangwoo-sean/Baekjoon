N = int(input())

result = 1
def fact(N):
    global result
    result *= N
    if N-1 >= 1:
        result = fact(N-1)
    return result
        
result = fact(N)
if result == 0:
    result = 1
print(result)