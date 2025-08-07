n = int(input(" Enter the number where you want to print: "))
for i in range (1, n+1):
    if n<=0:
        print("Error")
        break
    print(i)
    i = 1+i