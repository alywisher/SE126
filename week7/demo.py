#demo week 7 

#sequental search (review) Binery (intro) Bubble sort (intro)

import csv 

#creat 1 D list 
idStud = []
lName = []
fName = []
class1 = []
class2 = []
class3 = []

with open("week7/w7_demoFile.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        idStud.append(rec[0])
        lName.append(rec[1])
        fName.append(rec[2])
        class1.append(rec[3])
        class2.append(rec[4])
        class3.append(rec[5])

for i in range(0, len(idStud)):
    print(f"{idStud[i]}\t{lName[i]}\t{fName[i]}")

searchName = input("Enter the class you are looking for: ")
#found = -1
found = [] #allows multiple of eatch value in list
seqCount += 1 

#loop allows review of eatch value in list (search)
for i in range(0, len(fName)):

    #ask if value matchs current value in list 
    if searchName.lower() == fName[i].lower():

        #store found value location
        found = i

print(f"\n\tSearching complete. Search loop ran {seqCount} iterations.")
if found[0] != "":
    print(f"\n\tWe found {searchName} at index position(s): {found}")
    print("here is thir info: ")

    for i in range(0, len(found)):
        print(f"\t\t{fName[found[i]]}\t{lName[found[i]]}\t{idStud[found[i]]}\t{class1[found[i]]}\t{class2[found[i]]}\t{class3[found[i]]}")
else:
    print(f"\n\tWe could not find {searchName}")
    print("\tplease try again.\n")

#binary search ----> take an ordered list an divide it into 2 sections (high,low) and based on a middle point will countiuesly have a search pool until a unique value is found

searchName = input("enter the last name you are looking for: ")

min = 0 #first position of the list to be searched (ascending)
max = len(lName) - 1 #the last position of the list to be searched (ascending)
#mid = int((0 + len(lName) - 1) / 2)
mid = int((min + max) / 2)

#this is for INCREASING order

while (min < max and searchName != lName[mid]):
    binCount += 1
    if searchName < lName[mid]:
       max = mid - 1
    else:
       min = mid + 1

mid = int((min + max) / 2)

if searchName == lName[mid]:

    print(f"\t\t{fName[found[i]]}\t{lName[found[i]]}\t{idStud[found[i]]}\t{class1[found[i]]}\t{class2[found[i]]}\t{class3[found[i]]}")
    #found them! use 'guess' for index of found search item
else:
    print(f"\n\tWe could not find {searchName}")
    print("\tplease try again.\n")

#BUBBLE SORT----------------------------------------
    
nums = [100, 75, 32, 250, 47, 9, 2, 3, 99, 200]

print(f"current list: {nums}")

for i in range(0, len(nums) - 1):#outter loop

    print("OUTER LOOP! i = ", i)


    for index in range(0, len(nums) - 1):#inner loop

        print("\t INNER LOOP! k = ", index)

        #below if statement determines the sort
        #list used is the list being sorted
        # > is for increasing order, < for decreasing

        if(nums[index] > nums[index + 1]):
            print("\t\t SWAP! ", {nums[index]}, "<-->", {nums[index + 1]})
            #if above is true, swap places!

            temp = name[index]

            name[index] = name[index + 1]

            name[index + 1] = temp

 
            #swap all other values

            temp = age[index]

            age[index] = age[index + 1]

            age[index + 1] = temp

    


