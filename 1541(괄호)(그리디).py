sik = input()
sik = sik.split("-")

if sik[0] != "":
    check = sum(list(map(int, sik[0].split("+"))))
else:
    check = 0

sik = sik[1:]

mysum = 0
for i in sik:
    mysum += sum(list(map(int, i.split("+"))))

print(-1*mysum + check)