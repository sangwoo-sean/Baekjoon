ss = input()
bs = input()

ans = []
last = bs[-1]
for s in ss:
    ans.append(s)
    if s == last and bs == ''.join(ans[-len(bs):]):
        del ans[-len(bs):]
if ans:
    print("".join(ans))
else:
    print("FRULA")
