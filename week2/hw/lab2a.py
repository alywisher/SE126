#allison Wisher, Lab2A
#prompt: The csv file lab2a.csv contains a list of rooms, the maximum number of people that the room can accommodate, and the number of people currently registered for the event. Write a program that displays all rooms that are over the maximum limit of people and the number of people that have to be notified that they will have to be put on the wait list. After the file is completely processed the program should display the number of records processed and the number of rooms that are over the limit

import csv 
#variable dictinary 

total_records = 0

#starting documentation 

#initlaize empty list 

room = []
max_capacity = []
number_registered = [] 


with open ("week2/hw/lab2a.csv") as merp: 
    #acces file

    file = csv.reader(merp)

    for rec in file:

        #display the data value in neat colums
        #print(f"{rec[0]:10} \t{rec[1]:3} \t{rec[2]:10}")

        #store from rec list --> list

        room.append(rec[0])
        max_capacity.append(int(rec[1]))
        number_registered.append(int(rec[2]))

        #keep literal count

        total_records += 1 



#process the list to diplay the text file information
#process list --> for loop

#final display 
        
print(f"{'ROOM':16} \tMAX \tMIN \t OVER")
print("----------------------------------------------------------")

over_count = 0
for index in range(0, total_records):
   over = max_capacity[index] - number_registered[index]
   if (over < 0):
       over_count+=1
       print(f"{room[index]:16}\t{max_capacity[index]}\t{number_registered[index]}\t{abs(over)}")
    
#final display

print(f"TOTAL RECORDS: {total_records}")
print(f"TOTAL OVER: {over_count}")
