#week 7 D2 - binary practice

import csv

#create 1D list
type = []
name = []
meaning = []
origin = []

with open("week7/party.csv") as csvFile:
    file = csv.reader(csvFile)

    for rec in file:
        type.append(rec[0])
        name.append(rec[1])
        meaning.append(rec[2])
        origin.append(rec[3])

print("----ORIGINAL FILE----------------------------------------")
print(f"{'TYPE':8} {'NAME':12} {'MEANING':30} \t{'ORIGIN'} ")
for i in range(0, len(type)):
    print(f"{type[i]:8} {name[i]:12} {meaning[i]:30} {origin[i]}")
print("----------------------------------------------------------")

#sort the file data by first name, ascending (increasing) order
#bubble sort---------------------------------------------------
for i in range(0, len(name) - 1):#outter loop
    for index in range(0, len(name) - 1):#inner loop

        #below if statement determines the sort
        #list used is the list being sorted
        # > is for increasing order, < for decreasing

        if(name[index] > name[index + 1]):
            #if above is true, swap places!
            temp = name[index]
            name[index] = name[index + 1]
            name[index + 1] = temp
            #swap all other values

            #----TYPE----
            temp = type[index]
            type[index] = type[index + 1]
            type[index + 1] = temp

            #----MEANING----
            temp = meaning[index]
            meaning[index] = meaning[index + 1]
            meaning[index + 1] = temp

            #----ORIGIN----
            temp = origin[index]
            origin[index] = origin[index + 1]
            origin[index + 1] = temp
#test data
print("----SORTED FILE------------------------------------------")
print(f"{'TYPE':8} {'NAME':12} {'MEANING':30} \t{'ORIGIN'} ")
for i in range(0, len(type)):
    print(f"{type[i]:8} {name[i]:12} {meaning[i]:30} {origin[i]}")
print("----------------------------------------------------------")

#BINARY SORT-----------------------------------------------------------------------
search = input("\nEnter a name youd like to search")

min = 0
max = len(name) - 1       #can also use len(listName) for 'records' value
mid = int((min + max) / 2)

#this is for INCREASING order 

while (min < max and search.lower() != name[mid].lower()):

   if search < name[guess]:
       max = mid - 1
   else:
       min = mid + 1
   guess = int((min + max) / 2)

if search == name[mid]:
    #found them! use 'guess' for index of found search item
    print(f"We found {search}! here is their info: ")
    print(f"{'TYPE':8} {'NAME':12} {'MEANING':30} \t{'ORIGIN'} ")
    print(f"{type[mid]:8} {name[mid]:12} {meaning[mid]:30} {origin[mid]}")
else:
    #boooo not found
    print(f"\n\tWe did not find {search}! try again :[\n")

answer = input("would you like to search again? [y/n]: ")