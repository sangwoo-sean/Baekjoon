from itertools import permutations
import sys
input = sys.stdin.readline

N = input()
A = input()
MATH = input()

n = int(N)
numlist = list(map(int, A.split()))
math = list(map(int, MATH.split()))
howmany = sum(math)
mymin, mymax = 1000000000, -10000000000
# math[0] = +
# math[1] = -
# math[2] = x
# math[3] = //

def posbs(myset):
    allps = set(permutations(myset))
    return allps

operators = []
for i, op in enumerate(math):
    for j in range(op):
        if i == 0:
            operators.append("+")
        if i == 1:
            operators.append("-")
        if i == 2:
            operators.append("*")
        if i == 3:
            operators.append("/")

def cal(n, numlist, ops):
    result = numlist[0]

    for i in range(n-1):
        if ops[i] == "+":
            result += numlist[i+1]
        if ops[i] == "-":
            result -= numlist[i+1]
        if ops[i] == "*":
            result *= numlist[i+1]
        if ops[i] == "/":
            result = int(result / numlist[i+1])
        
    return result
    
alltrys = list(posbs(operators))
for each in alltrys:
    result = cal(n, numlist, each)
    if result > mymax:
        mymax = result
    if result < mymin:
        mymin = result
print(mymax)
print(mymin)