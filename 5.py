number = input('enter the number : ')


def check(num):
    sum = 0
    lenght = int(len(num))
    for i in num:
        sum += int(i)** lenght
    if sum == int(num):
        print('yes')
    else:
        print('no')


check(number)