origin = input()
opers1 = ("+", "-")
opers2 = ("*", "/")
stack = []
answer = ""

for i in origin:

    if i == "(":
        stack.append(i)
    elif i == ")":
        while stack and stack[-1] != "(":
            answer += stack.pop()
        stack.pop()

    elif i in opers1:  # +, - 일때
        while stack and stack[-1] != "(":
            answer += stack.pop()
        stack.append(i)

    elif i in opers2:  # *, / 일때
        while stack and (stack[-1] in opers2):
            answer += stack.pop()
        stack.append(i)

    else:  # 알파벳이면 무조건 추가
        answer += i

while stack:
    answer += stack.pop()
print(answer)
