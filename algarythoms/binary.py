#(see demo posted above for full documentation!)
 
#Binary Search Algorithm:

search = input("Get search from user!")

min = 0

max = records - 1       #can also use len(listName) for 'records' value


guess = int((min + max) / 2)

#this is for INCREASING order

while (min < max and search != listName[guess]):

   if search < listName[guess]:
       max = mid - 1
   else:
       min = mid + 1
   guess = int((min + max) / 2)

if search == listName[mid]:
    #found them! use 'guess' for index of found search item
    print("")
else:
    #boooo not found
    print("")