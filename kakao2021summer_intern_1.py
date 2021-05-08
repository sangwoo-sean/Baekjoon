def solution(s):
    d = {"zero": "0",
         "one": "1",
         "two": "2",
         "three": "3",
         "four": "4",
         "five": "5",
         "six": "6",
         "seven": "7",
         "eight": "8",
         "nine": "9"}
    w = ["zero", "one", "two", "three", "four",
         "five", "six", "seven", "eight", "nine"]
    flag = True
    while flag:
        flag = False
        for i in w:
            if i in s:
                flag = True
                s = s.replace(i, d[i])

    answer = int(s)
    return answer
