#Question 8
List =[]
print("Enter ten integers")
for a in range(10):
    Integer = input("Enter an integer :")
    List.append(Integer)

#Postive numbers
print("\nPositive numbers from the entered integers are :",end="")
for i in List:
    if int(i)>=0:
        print(i,end=" ")

#Negative numbers
print("\nNegative numbers from the entered integers are :",end="")
for i in List:
    if int(i)<=0:
        print(i,end=" ")

#Odd numbers
print("\nOdd numbers from the entered integers are :",end="")
for i in List:
    if int(i)%2!=0:
        print(i,end=" ")

#Even Numbers
print("\nEven numbers from the entered integers are :",end="")
for i in List:
    if int(i)%2==0:
        print(i,end=" ")

#Count of each integer
print("\nCount of each entered integer:")
frequency = {}
for Number in List:
  if Number in frequency:
    frequency[Number] += 1
  else:
    frequency[Number] = 1

for Number, count in frequency.items():
  print(f"{Number} occurs {count} times")
