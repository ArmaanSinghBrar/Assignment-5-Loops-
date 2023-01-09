#Occurance of each word in a list entered by a user
List = input("Enter a list").split()
print("Count of each word in the list :")
frequency = {}              #Creating an empty set
for Word in List:           #A loop for each word in the set
  if Word in frequency:     #If word already in dictionary it adds one to the frequency
    frequency[Word] += 1
  else:                     #If word not in dictionary frequency is set to one
    frequency[Word] = 1
for Word,count in frequency.items():
  print(f"{Word} occurs {count} times")
