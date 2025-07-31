length = int(input( " Enter the length of rectangle " ))
width = int(input( " Enter the width of rectangle " ))
Area_of_Rectangle = length*width
if (length<=0) or (width<=0): 
    print(" length or width  can not be zero")
    exit()
print(Area_of_Rectangle , "sq" )