num1 = int(input( " Enter first number " ))
num2 = int(input( " Enter second number " ))
num3 = int(input( " Enter third number " ))

smaller1 = num1
if (num2<num1):
    smaller = num2
smaller2 = num2
if (num3<num2):
    smaller = num3
smaller2 = num3
if (num1<num3):
    smaller = num1


print(smaller , " is smaller ")

