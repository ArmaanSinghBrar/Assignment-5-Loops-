#Calculating Area of a triangle using heron's formula and if the combination of given sides is possible
side1 = float(input("Enter first side of the triangle :"))
side2 = float(input("Enter second side of the triangle :"))
side3 = float(input("Enter third side of the triangle :"))
if side1<side2+side3 and side2<side1+side3 and side3<side1+side2:      #A triangle is only possible if sum of two sides is always greater than the other side
    s = (side1 + side2 + side3)/2            #Calculating area using heron's formula
    Area = (s*(s-side1)*(s-side2)*(s-side3))**0.5
    print("The area of the triangle is =",Area)
else:
    print("Error ,A triangle is not possible with given sides")
