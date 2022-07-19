def perimeter_function(a,b):
    if a>0 and b>0:
        area=a*b
        perimeter=2*a + 2*b
        return area
        return perimeter

    else:
        print("Sides can't be <=0")
 
print(perimeter_function(5,3))
