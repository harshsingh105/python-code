n = int(input(" Enter the number: "))
if (n%3!=0 and n%5!=0) :
    print("this number" ,n ,  "is not divisible by both 3 or 5")
    exit()
if n % 5 == 0 and n % 3 == 0:
     print("fizzbuzz")
elif n%3==0: 
    print("fizz")
elif n%5==0:
    print("buzz")
  
