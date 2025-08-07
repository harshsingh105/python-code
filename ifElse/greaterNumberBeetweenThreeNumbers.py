number1 = int(input( " Enter first number " ))
number2 = int(input( " Enter second numbee " ))
number3 = int(input( " Enter third number " ))
if number1==number2==number3:
    print("all number are same ")
    exit()
if number1<number2 and number1<number3:
    print(number1 , "is small")
    exit()
elif number2<number3 and number2<number1:
    print(number2 , " is smaller ")
else:
    print(number3 , " is smaller ")