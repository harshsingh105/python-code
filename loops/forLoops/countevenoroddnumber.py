number = input("enter a number:")
even = 0
odd = 0
for i in number:
    if int(i) % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even numbers :", even)
print("Odd numbers :", odd)

