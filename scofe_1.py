n = int(input())
stimes = []
etimes = []
for _ in range(n):
    s, e = input().split("~")
    sh, sm = map(int, s.split(":"))
    eh, em = map(int, e.split(":"))
    stimes.append([sh, sm])
    etimes.append([eh, em])

stimes.sort()
etimes.sort()

sans = stimes[-1]
eans = etimes[0]
ans = "{:02d}:{:02d} ~ {:02d}:{:02d}".format(
    sans[0], sans[1], eans[0], eans[1])
if sans[0] > eans[0] or (sans[0] == eans[0] and sans[1] > eans[1]):
    ans = -1
print(ans)
