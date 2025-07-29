chappal=int(input("Enter the chappals: "))
if (chappal < 0):
    print("Please take chappal always in positive number!")
    
leftchappal = chappal%2
jodi = chappal//2
print(jodi,"jodi" , leftchappal,"chappal left" )
