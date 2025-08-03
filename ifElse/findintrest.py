principal = int(input( " Enter the principal " ))
rate = int(input( " Enter the rate " ))
year = int(input( " Enter the year "  )) 
simple_intrest = principal*rate*year//100
if ( principal and rate and year<= 0):
    print ("please eneter principal rate year positive not negative or zero ")
    exit()
print(simple_intrest , " is the simple intrest ") 