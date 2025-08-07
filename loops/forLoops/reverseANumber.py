#if i enter 65 then give me output 56
number = int(input(" Enter a number: " ))
x= number%10
print(x)
leftnumber = int(number//10)
print(leftnumber)
y = leftnumber%10
print(y)
againleft = int(leftnumber//10)
print(againleft)
lefts = [x,y,againleft]
print(lefts)
reversed = (lefts)
lefts = [x,y,againleft]
while number 

a, b, c = lefts

print(a)  
print(b) 
print(c)  
print( "final answer is " , a,b,c)