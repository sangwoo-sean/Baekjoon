import random


for _ in range(5):
    mylist = "("
    for i in range(12):

        a = random.randint(0,1)
        if a == 0:
            mylist += "("
        else:
            mylist += ")"


    mylist += ")"
    print(mylist)