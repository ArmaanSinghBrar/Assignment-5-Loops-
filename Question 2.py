#Printing all the numbers in a given range divisible by a given number
Range = int(input("Enter the range :"))
Divisor = float(input("Enter the divisor :"))
for i in range(Range+1):                  #Creating a loop for range [0,Range]
    if i%Divisor==0:                      #Condition for number to be divisible by the divisor
        print(i)
