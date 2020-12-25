n = int(input())
mylist = []
for i in range(n):
    mylist.append(list(map(int, input().split())))
sorted_list = sorted(mylist, reverse=True)
st = [[201, 201]]
st.extend(sorted_list)

result = []
for i in range(len(st)-1):
    
    if st[i][1] > st[i+1][1]:
        result.append(i+1)
    else:
        result.append(result[i-1])
ans = []
for i in range(n):
    index = sorted_list.index(mylist[i])
    ans.append(result[index])

strver = list(map(str, ans))
print(" ".join(strver))
print(st,"\n" ,result)