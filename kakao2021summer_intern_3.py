def solution(n, k, cmd):
    cut = []
    selected = k
    arr = ["O" for _ in range(n)]

    for i in cmd:
        if i[0] == "D":
            c = int(i.split()[1])
            while c > 0:
                selected = min(selected+1, n-1)
                if arr[selected] == "O":
                    c -= 1
        elif i[0] == "U":
            c = int(i.split()[1])
            while c > 0:
                selected = max(selected-1, 0)
                if arr[selected] == "O":
                    c -= 1

        elif i[0] == "C":
            arr[selected] = "X"
            cut.append(selected)

            while arr[selected] == "X":
                selected = selected+1
                if selected == n:
                    for j in range(n):
                        if arr[j] == "O":
                            selected = j
                    break

        elif i[0] == "Z" and cut:
            idx = cut.pop()
            arr[idx] = "O"

        # print([f"{h}" for h in range(8)])
        # print(arr, selected, i)

    answer = ''.join(arr)
    # print(answer)
    return answer
