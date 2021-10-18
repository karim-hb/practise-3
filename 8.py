
number1 = int(input('enter first number : '))
number2 = int(input('enter second number : '))

def lcm(a,b):
    g = 0
    for i in range (1, a + 1):
    	if i <= b:
		    if a % i == 0 and b % i == 0:
		    	g = i

    return (a * b) / g




print ("The lcm of {} and {} is : {} ".format(number1,number2,lcm(number1,number2)))
