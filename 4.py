import math 

number = int(input("enter number : "))
def check(num):
    if num == 2 or num == 1:
         return True
    else:
        for i in range(0, int(num/2)):
            if num == math.factorial(i):
                return True
                break
            

if check(number) == True:
    print('yes')
else :
    print('no')