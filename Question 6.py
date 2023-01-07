#Printing prime numbers in the given range
Lower = int(input("Enter the lower bound of the range :"))
Upper = int(input("Enter the upper bound of the range :"))
if Upper<Lower:
    print("Error,Upper bound can't be less than lower bound. Please enter suitable range")
elif Lower>=2 and Upper>=2:
    for i in range(Lower,Upper+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
elif Lower< 2 <=Upper:
    for i in range(2,Upper+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
elif Upper<2:
    print("Error,The upper bound must be more than equal to 2 as 2 is the smallest prime number.Please enter suitable range")
