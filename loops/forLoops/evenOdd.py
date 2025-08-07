numbers = [12, 17, 19, 24, 31, 40,44,4565,35555,542432,3554345,344435]

even = 0
odd = 0

for n in numbers:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)
