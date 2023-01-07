#Creating a given pattern of alphabets
Rows = int(input("Enter number of rows :"))
alphabet = 65
for i in range(Rows):
    for j in range(i):
        if alphabet<=90:
            print(chr(alphabet),end=" ")
            alphabet+=1
        else:
            alphabet=65
            i+=2
    print("")
