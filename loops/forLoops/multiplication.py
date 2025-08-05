# n = int(input(" Enter the number "))
# i = n
# counter = 1
# while i<=100:
#     print("10 x" , counter ,"=", i)
#     counter += 1
#     i+=10
    
n = int(input("Enter the number: "))

for i in range(1, 11):
    mul = n * i
    print(n, " x ", i ,"=", mul)
