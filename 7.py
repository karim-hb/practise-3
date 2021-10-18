number1 = int(input('enter first number : '))
number2 = int(input('enter second number : '))


def gcd(a, b):
      
    if a > b:
        small = b
    else:
        small = a
    for i in range(1, small+1):
        if((a % i == 0) and (b % i == 0)):
            gcd = i
              
    return gcd
  

  
print ("The gcd of {} and {} is : {} ".format(number1,number2,gcd(number1,number2)))
