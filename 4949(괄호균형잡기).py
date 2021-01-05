
# 내 솔루션
while True:
    mystr = input()
    if mystr == '.':
        break

    score1 = 0
    score2 = 0
    valid = True
    temp1 = []
    temp2 = []
    for i in mystr:
        if i == "(":
            score1 += 1
            temp1.append(score2)
        elif i == ")":
            score1 -= 1
            if score1 < 0:
                valid = False
                break
            elif temp1[-1] != score2:
                valid = False
                break
            temp1.pop()

        elif i == "[":
            score2 += 1
            temp2.append(score1)
        elif i == "]":
            score2 -= 1
            if score2 < 0:
                valid = False
                break
            elif temp2[-1] != score1:
                valid = False
                break
            temp2.pop()
    
    if score1 == 0 and score2 == 0 and valid:
        print("yes")
    else:
        print('no')

#구글링한 솔루션
# while True:
#     s = input()
#     if s == '.':
#         break
#     stk = []
#     temp = True
#     for i in s:
#         if i == '(' or i == '[':
#             stk.append(i)
#         elif i == ')':
#             if not stk or stk[-1] == '[':
#                 temp = False
#                 break
#             elif stk[-1] == '(':
#                 stk.pop()
#         elif i == ']':
#             if not stk or stk[-1] == '(':
#                 temp = False
#                 break
#             elif stk[-1] == '[':
#                 stk.pop()
#     if temp == True and not stk:
#         print('yes')
#     else:
#         print('no')