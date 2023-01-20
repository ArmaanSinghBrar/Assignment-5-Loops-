#Creating a right angled pattern of alphabets
Rows = int(input("Enter number of rows :"))
alphabet = 65
for i in range(Rows+1):
    for j in range(i):
        if alphabet==91:
            alphabet=65
        print(chr(alphabet),end=" ")
        alphabet+=1
    print("")
