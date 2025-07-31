"""a = 4
b = 6 
c = 3

a > b and a > c
    print(a is biggerst number other )
b > c and  b > a
   print( b islls l  lm);

else: {
    print(c is biggerst )
}"""


firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))
thirdNumber = int(input("Enter third number: "))

if (firstNumber > secondNumber and firstNumber > thirdNumber ):
    print("firstNumber is biggest number: ", firstNumber)
elif(secondNumber  > thirdNumber and secondNumber > firstNumber):
     print("secondNumber is biggest number: ", secondNumber)
elif(firstNumber == secondNumber and secondNumber ==thirdNumber): 
     print("All numbers are equals")  
else: 
     print("thirdNumber is biggest number: ", thirdNumber)    