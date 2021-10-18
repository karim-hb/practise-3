import random
randomlist = []
number = int(input("how many number do you want in your array?"))
for i in range(0,number):
    n = random.randint(1,300)
    if n in randomlist:
        print('pass')
    else:
        randomlist.append(n)
    print(randomlist)